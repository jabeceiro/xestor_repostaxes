"""
Módulo de entrada e saída da aplicación.

Encárgase de xestionar as interaccións co usuario a través da consola
(menús, petición de datos e visualización de resultados) e das operacións
de persistencia en ficheiros JSON.

Funcionalidades principais:
    - Mostrar o menú principal e solicitar opcións ao usuario.
    - Pedir e validar entradas básicas por teclado.
    - Mostrar historial, gasto total e consumo medio, resumo xeral.
    - Cargar e gardar a lista de repostaxes en data/datos.json.

Este módulo só se encarga da interface textual e da persistencia.
Este módulo non contén lóxica de negocio: os cálculos e validacións
complexas levanse a cabo en app/funciones.py.
"""

import json
from pathlib import Path
from typing import Any
from datetime import date

from .funciones import (
    crear_repostaxe,
    calcular_gasto_total,
    calcular_consumo_medio,
    calcular_km_totais,
    calcular_litros_totais,
    obter_repostaxes_extremos
)

RUTA_DATOS = Path("data") / "datos.json"


# ------------------------------------------------------------
# Persistencia
# ------------------------------------------------------------

def cargar_repostaxes() -> list[dict[str, Any]]:
    """
    Carga os repostaxes dende data/datos.json.

    Returns:
        list[dict]: Lista de repostaxes cargada do ficheiro, ou lista baleira.
    """
    
    if not RUTA_DATOS.exists():
        return []

    try:
        with RUTA_DATOS.open("r", encoding="utf-8") as f:
            datos = json.load(f)
            return datos if isinstance(datos, list) else []
    except (OSError, json.JSONDecodeError):
        return []


def gardar_repostaxes(repostaxes: list[dict[str, Any]]) -> None:
    """
    Garda os repostaxes en data/datos.json.

    Args:
        repostaxes (list[dict]): Lista de repostaxes a gardar.
    """
    
    RUTA_DATOS.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        with RUTA_DATOS.open("w", encoding="utf-8") as f:
            json.dump(repostaxes, f, ensure_ascii=False, indent=4)
    except OSError:
        print("Erro ao intentar gardar os datos.")


# ------------------------------------------------------------
#  Interface textual
# ------------------------------------------------------------
def mostrar_menu(modificado: bool = False) -> None:
    """
    Mostra o menú principal da aplicación.

    Args:
        modificado (bool): Indica se existen cambios sen gardar.
                           Cando é True, móstrase un asterisco (*) no menú.
    """
    
    indicador = " *" if modificado else ""
    
    print("╔════════════════════════════╗")
    print(f"║    XESTOR DE REPOSTAXES {indicador:<3}║")
    print("╚════════════════════════════╝")
    print(" 1. Rexistrar repostaxe")
    print(" 2. Mostrar historial")
    print(" 3. Calcular gasto total")
    print(" 4. Calcular consumo medio")
    print(" 5. Mostrar resumen")
    if modificado:
        print(" 6. Gardar datos *")
    else:    
        print(" 6. Gardar datos")
    print(" 0. Saír")
    print("═"*32)


def pedir_opcion_menu() -> int:
    """ 
    Solicita ao usuario unha opción do menú. 
    
    Returns: 
        int: Número introducido polo usuario, ou -1 se non é válido. 
    """
    try:
        return int(input("Escolle unha opción: "))
    except ValueError:
        # print("Erro: introduce un número.")
        return -1


def pedir_data() -> str:
    """ 
    Pide ao usuario unha data, ofrecendo a de hoxe como valor por defecto. 
    
    Returns: 
        str: Data introducida polo usuario ou a data actual. 
    """
    hoxe = date.today().isoformat()
    entrada = input(f"Data [{hoxe}]: ").strip()
    return entrada or hoxe


def rexistrar_repostaxe_desde_input(repostaxes: list[dict[str, Any]]) -> None:
    """ 
    Solicita ao usuario os datos dunha repostaxe e rexístraa se é válida. 

    Args: 
        repostaxes (list[dict]): Lista de repostaxes existente. 
    """
    
    mostrar_encabezado("REXISTRAR REPOSTAXE", 40)

    data = pedir_data()

    try:
        litros = float(input("Litros: "))
        prezo = float(input("Prezo por litro (€): "))
        km = int(input("Quilometraxe: "))
    except ValueError:
        print("\n❌ Erro: valores numéricos incorrectos.")
        return

    repostaxe, erro = crear_repostaxe(data, litros, prezo, km, repostaxes)

    if erro:
        print(f"\n❌ Erro: {erro}")
        return

    repostaxes.append(repostaxe)
    
    print("\n✅ Repostaxe rexistrada correctamente.")


def mostrar_encabezado(titulo: str, lonxitude: int = 32) -> None:
    """
    Mostra un encabezado centrado cunha liña superior e inferior.

    Args:
        titulo (str): Texto que se mostrará centrado.
        lonxitude (int): Ancho total da liña decorativa.
    """
    liña = "=" * lonxitude
    print("\n" + liña)
    print(titulo.center(lonxitude))
    print(liña)


def mostrar_historial(repostaxes: list[dict[str, Any]]) -> None:       
    """
    Mostra unha lista co historial de repostaxes.

    Args:
        repostaxes (list[dict]): Lista de repostaxes.
    """
    
    mostrar_encabezado("HISTORIAL DE REPOSTAXES", 50)
    
    if not repostaxes:
        print("Non hai datos.")
        return

    # Cabeceiras aliñadas
    print(f"{'Data':<12} {'Litros':>8} {'€/L':>8} {'Km':>10}")
    print("-" * 50)

    for i, r in enumerate(repostaxes, start=1):
        try:
            print(f"{r['data']:<12} {r['litros']:>8.2f} {r['prezo_litro']:>8.2f} {r['kilometraxe']:>10}")
        except KeyError as e: 
            print(f"[Rexistro {i}] Erro: falta a clave {e.args[0]!r}. Rexistro ignorado.") 
        except (TypeError, ValueError): 
            print(f"[Rexistro {i}] Erro: datos corruptos. Rexistro ignorado.")    


def mostrar_gasto_total(repostaxes: list[dict[str, Any]]) -> None:
    """
    Mostra o gasto total en combustible.

    Args:
        repostaxes (list[dict]): Lista de repostaxes.
    """
    
    mostrar_encabezado("CALCULAR GASTO TOTAL", 32)

    if not repostaxes:
        print("Non hai datos para calcular o gasto.")
        return
    try:
        total = calcular_gasto_total(repostaxes)
    
        primeiro, ultimo = obter_repostaxes_extremos(repostaxes)
        data_inicio = primeiro["data"] 
        data_fin = ultimo["data"]
    
        ancho = 18   # ancho da columna esquerda
        print(f"{'Data inicio:':{ancho}} {data_inicio}") 
        print(f"{'Data fin:':{ancho}} {data_fin}") 
        print(f"{'Gasto total:':{ancho}} {total:>10.2f} €")
    
    except (KeyError, TypeError, ValueError): 
        print("Erro: datos corruptos en datos.json.")
        
        
def mostrar_consumo_medio(repostaxes: list[dict[str, Any]]) -> None:
    """
    Mostra o consumo medio en L/100 km.

    Args:
        repostaxes (list[dict]): Lista de repostaxes.
    """
    
    mostrar_encabezado("CALCULAR CONSUMO MEDIO", 40)

    consumo = calcular_consumo_medio(repostaxes)
    if consumo is None:
        print("Non se pode calcular o consumo medio.")
        return
    try:
        primeiro,ultimo =obter_repostaxes_extremos(repostaxes) 
        data_inicio = primeiro["data"] 
        data_fin = ultimo["data"]
       
        ancho = 18    # ancho da columna esquerda
        print(f"{'Data inicio:':{ancho}} {data_inicio}") 
        print(f"{'Data fin:':{ancho}} {data_fin}") 
        print(f"{'Consumo medio:':{ancho}} {consumo:>10.2f} L/100 km")
    
    except (KeyError, TypeError, ValueError):
            print("Erro: datos corruptos en datos.json.")
    
def mostrar_resumo(repostaxes: list[dict[str, Any]]) -> None:
    """
    Mostra un resumo xeral dos datos de repostaxes.
     - Gasto total (€)
     - Kms totais percorridos (km)
     - Consumo total de combustible (L)
     - Consumo medio (L/100 km)

    Args:
        repostaxes (list[dict]): Lista de repostaxes.
    """
    
    mostrar_encabezado("RESUMO XERAL", 40)

    if not repostaxes:
        print("Non hai datos para mostrar o resumo.")
        return
    
    try:
       # Km totais
       km_totais = calcular_km_totais(repostaxes)
    
       # Gasto total
       gasto_total = calcular_gasto_total(repostaxes)
    
       # Consumo total en litros
       litros_totais = calcular_litros_totais(repostaxes)
       
       # Consumo medio en L/100 km
       consumo = calcular_consumo_medio(repostaxes)
       
       primeiro, ultimo = obter_repostaxes_extremos(repostaxes) 
       data_inicio = primeiro["data"] 
       data_fin = ultimo["data"]
       
       ancho = 20  # ancho da columna esquerda
       print(f"{'Data inicio:':<{ancho}} {data_inicio}") 
       print(f"{'Data fin:':<{ancho}} {data_fin}")
       print(f"{'Gasto total:':<{ancho}} {gasto_total:.2f} €")
       print(f"{'Km totais:':<{ancho}} {km_totais:>5} km")
       print(f"{'Litros totais:':<{ancho}} {litros_totais:.2f} L")
       print(f"{'Consumo medio:':<{ancho}} {consumo:.2f} L/100 km")
       print()
    
    except (KeyError, TypeError, ValueError):
        print("Erro: datos corruptos en datos.json.")
        