"""
Conxunto de funcións de lóxica e validación para a aplicación de xestión
de repostaxes.

Non contén interacción co usuario nin operacións de entrada/saída.
"""

from datetime import datetime
from typing import Any


def crear_repostaxe(
    data: str,
    litros: float,
    precio_litro: float,
    kilometraxe: int,
    existentes: list[dict[str, Any]]
) -> tuple[dict | None, str | None]:
    """
    Crea unha nova repostaxe validando os datos introducidos.

    Regras:
        - litros > 0
        - precio_litro > 0
        - kilometraxe > 0
        - a quilometraxe debe ser maior que a última rexistrada
        - a data (YYYY-MM-DD) e non debe ser anterior a da última repostaxe
    """

    # Validación da data de repostaxe
    try:
        data_nova =datetime.strptime(data, "%Y-%m-%d").date()
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

    if precio_litro <= 0:
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
        "precio_litro": precio_litro,
        "kilometraxe": kilometraxe
    }

    return repostaxe, None


def calcular_gasto_total(repostaxes: list[dict[str, Any]]) -> float:
    """Calcula o gasto total en combustible."""
    
    return sum(r["litros"] * r["precio_litro"] for r in repostaxes)


def calcular_consumo_medio(repostaxes: list[dict[str, Any]]) -> float | None:
    """
    Calcula o consumo medio en L/100 km.
    Precísanse polo menos dúas repostaxes válidas.
    """
    if len(repostaxes) < 2:
        return None

    distancia = repostaxes[-1]["kilometraxe"] - repostaxes[0]["kilometraxe"]
    if distancia <= 0:
        return None

    litros_totais = sum(r["litros"] for r in repostaxes)
    return (litros_totais / distancia) * 100
