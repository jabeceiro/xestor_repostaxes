"""
Conxunto de funcións de lóxica e validación para a aplicación de xestión
de repostaxes.

Non contén interacción co usuario nin operacións de entrada/saída.
Encárgase solo de cálculos, validacións e manipulación de datos.
"""

from datetime import datetime
from typing import Any


# ------------------------------------------------------------ 
# Funcións de validación e creación 
# ------------------------------------------------------------

def crear_repostaxe(
    data: str,
    litros: float,
    prezo_litro: float,
    kilometraxe: int,
    existentes: list[dict[str, Any]]
) -> tuple[dict | None, str | None]:
    """
    Crea unha nova repostaxe validando os datos introducidos.

    Regras de validación:
        - litros > 0
        - prezo_litro > 0
        - kilometraxe > 0
        - a quilometraxe debe ser maior que a última rexistrada
        - a data debe ter formato YYYY-MM-DD
        - a data non pode ser anterior á data da última repostaxe rexistrada

    Args:
        data (str): Data da repostaxe no formato YYYY-MM-DD.
        litros (float): Cantidade de litros repostados.
        prezo_litro (float): Prezo por litro de combustible.
        quilometraxe (int): Quilometraxe actual do vehículo.
        existentes (list[dict]): Lista de repostaxes anteriores.

    Returns:
        tuple[dict | None, str | None]: 
            - dict con datos válidos se todo é correcto.
            - Mensaxe de erro se hai algún problema de validación.

    """

    # Validación da data de repostaxe
    try:
        data_nova = datetime.strptime(data, "%Y-%m-%d").date()
    except ValueError:
        return None, "A data debe ter o formato YYYY-MM-DD."
    
    # Validación de data non anterior á última rexistrada 
    if existentes:
        try:
            data_ultima = datetime.strptime(existentes[-1]["data"], "%Y-%m-%d").date() 
            if data_nova < data_ultima:
                return None, "A data non pode ser anterior á data da última repostaxe rexistrada." 
        except ValueError:
            return None, "Erro ao intentar recuperar a data da última repostaxe."
    
    # Validación de valores positivos
    if litros <= 0:
        return None, "Os litros deben ser positivos."

    if prezo_litro <= 0:
        return None, "O prezo por litro debe ser positivo."

    if kilometraxe <= 0:
        return None, "A quilometraxe debe ser positiva."
    
    # Validación de quilometraxe maior que a última rexistrada
    if existentes and kilometraxe <= existentes[-1]["kilometraxe"]:
        return None, "A quilometraxe debe ser maior que a última rexistrada."
    
    # Se todo é correcto, construímos a repostaxe
    repostaxe = {
        "data": data,
        "litros": litros,
        "prezo_litro": prezo_litro,
        "kilometraxe": kilometraxe
    }

    return repostaxe, None


# ------------------------------------------------------------ 
# Funcións de cálculo 
# ------------------------------------------------------------

def calcular_litros_totais(repostaxes: list[dict[str, Any]]) -> float: 
    """
    Calcula a suma total de litros repostados.

    Args:
        repostaxes (list[dict]): Lista de repostaxes.

    Returns:
        float: Total de litros repostados.
    """ 
    return sum(r["litros"] for r in repostaxes)


def calcular_gasto_total(repostaxes: list[dict[str, Any]]) -> float:
    """
    Calcula o gasto total en combustible.

    Args:
        repostaxes (list[dict]): Lista de repostaxes.

    Returns:
        float: Cantidade total gastada en combustible.
    """
    
    return sum(r["litros"] * r["prezo_litro"] for r in repostaxes)

def calcular_km_totais(repostaxes: list[dict[str, Any]]) -> int: 
    """ 
    Calcula os quilómetros totais percorridos.

    Args:
        repostaxes (list[dict]): Lista de repostaxes en orde cronolóxica.

    Returns:
        int: Diferenza entre a quilometraxe da última e da primeira repostaxe.
    """ 

    if len(repostaxes) < 2:
        return 0 
    
    primeiro, ultimo = obter_repostaxes_extremos(repostaxes) 
    
    return ultimo["kilometraxe"] - primeiro["kilometraxe"]


def calcular_consumo_medio(repostaxes: list[dict[str, Any]]) -> float | None:
    """
   Calcula o consumo medio en L/100 km.
   Precísanse polo menos dúas repostaxes válidas. 
   
    Args:
        repostaxes (list[dict]): Lista de repostaxes en orde cronolóxica.

    Returns:
        float | None: Consumo medio se hai datos suficientes, ou None se non se pode calcular.  
    """
    
    if len(repostaxes) < 2:
        return None

    distancia = calcular_km_totais(repostaxes)
    if distancia <= 0:
        return None

    litros_totais = calcular_litros_totais(repostaxes)
    
    return (litros_totais / distancia) * 100


def calcular_km_totais(repostaxes: list[dict]) -> int:
    """
    Calcula os quilómetros totais percorridos.

    Args:
        repostaxes (list[dict]): Lista de repostaxes en orde cronolóxica.

    Returns:
        int: Diferenza entre a quilometraxe da última e da primeira repostaxe.
    """
    
    if len(repostaxes) < 2:
        return 0  # Non hai kilometraxe medible

    primeiro,  ultimo = obter_repostaxes_extremos(repostaxes)
    
    return ultimo["kilometraxe"] - primeiro["kilometraxe"]


def obter_repostaxes_extremos(repostaxes: list[dict]) -> tuple[dict, dict]:
    """
    Devolve o primeiro e o último rexistro de repostaxe.

    Args:
        repostaxes (list[dict]): Lista de repostaxes en orde cronolóxica.

    Returns:
        tuple[dict | None, dict | None]: Primeiro e último rexistro, ou None se a lista está baleira.
    """
   
    if not repostaxes:
        return None, None

    primeiro, *_, ultimo = repostaxes
    
    return primeiro, ultimo
