"""
Módulo de entrada e saída da aplicación.

Encárgase de xestionar as interaccións co usuario a través da consola
(menús, petición de datos e visualización de resultados) e das operacións
de persistencia en ficheiros JSON.

Funcionalidades principais:
    - Mostrar o menú principal e solicitar opcións ao usuario.
    - Pedir e validar entradas básicas por teclado.
    - Mostrar historial, gasto total e consumo medio.
    - Cargar e gardar a lista de repostaxes en data/datos.json.

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
    calcular_consumo_medio
)

RUTA_DATOS = Path("data") / "datos.json"


# -----------------------------
# Persistencia
# -----------------------------
def cargar_repostaxes() -> list[dict[str, Any]]:
    """Carga os repostaxes dende data/datos.json."""
    
    if not RUTA_DATOS.exists():
        return []

    try:
        with RUTA_DATOS.open("r", encoding="utf-8") as f:
            datos = json.load(f)
            return datos if isinstance(datos, list) else []
    except (OSError, json.JSONDecodeError):
        return []


def gardar_repostaxes(repostaxes: list[dict[str, Any]]) -> None:
    """Garda os repostaxes en data/datos.json."""
    
    RUTA_DATOS.parent.mkdir(parents=True, exist_ok=True)
    try:
        with RUTA_DATOS.open("w", encoding="utf-8") as f:
            json.dump(repostaxes, f, ensure_ascii=False, indent=4)
    except OSError:
        print("Erro ao intentar gardar os datos.")


# -----------------------------
# Interface textual
# -----------------------------
def mostrar_menu() -> None:
    print("\n--- XESTOR DE REPOSTAXES ---")
    print("----------------------------")
    print("1. Rexistrar repostaxe")
    print("2. mostrar historial")
    print("3. Calcular gasto total")
    print("4. Calcular consumo medio")
    print("5. Gardar datos")
    print("6. Saír")


def pedir_opcion() -> int:
    try:
        return int(input("Escolle unha opción: "))
    except ValueError:
        print("Erro: introduce un número.")
        return -1


def pedir_data() -> str:
    hoxe = date.today().isoformat()
    entrada = input(f"Data [{hoxe}]: ").strip()
    return entrada if entrada else hoxe


def rexistrar_repostaxe_desde_input(repostaxes: list[dict[str, Any]]) -> None:
    print("\n--- Rexistrar repostaxe ---")
    print("---------------------------")


    data = pedir_data()

    try:
        litros = float(input("Litros: "))
        prezo = float(input("Prezo por litro (€): "))
        km = int(input("Quilometraxe: "))
    except ValueError:
        print("Erro: valores numéricos incorrectos.")
        return

    repostaxe, erro = crear_repostaxe(data, litros, prezo, km, repostaxes)

    if erro:
        print(f"Erro: {erro}")
        return

    repostaxes.append(repostaxe)
    print("Repostaxe rexistrada correctamente.")


def mostrar_historial(repostaxes: list[dict[str, Any]]) -> None:
    print("\n--- Historial de repostaxes ---")
    print("-------------------------------")

    if not repostaxes:
        print("Non hai datos.")
        return

    for r in repostaxes:
        print(f"{r['data']} | {r['litros']} L | {r['precio_litro']} €/L | {r['kilometraxe']} km")


def mostrar_gasto_total(repostaxes: list[dict[str, Any]]) -> None:
    print("\n--- Calcular gasto total ---")
    print("----------------------------")
    
    if not repostaxes:
        print("Non hai datos para calcular o gasto.")
        return

    total = calcular_gasto_total(repostaxes)
    print(f"Gasto total: {total:.2f} €")


def mostrar_consumo_medio(repostaxes: list[dict[str, Any]]) -> None:
    print("\n--- Calcular consumo medio ---")
    print("------------------------------")

    consumo = calcular_consumo_medio(repostaxes)
    if consumo is None:
        print("Non se pode calcular o consumo medio.")
        return

    print(f"Consumo medio: {consumo:.2f} L/100 km")
