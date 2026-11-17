TIPOS_COBRADOS = ("carro", "moto")


def resumen_del_dia(registros: list[dict]) -> dict:
    """Resume la caja del día: total cobrado y cantidad de carros y motos."""
    cobrados = [registro for registro in registros if registro["tipo"] in TIPOS_COBRADOS]
    return {
        "total": sum(registro["valor"] for registro in cobrados),
        "carros": _contar_por_tipo(cobrados, "carro"),
        "motos": _contar_por_tipo(cobrados, "moto"),
    }


def _contar_por_tipo(registros: list[dict], tipo: str) -> int:
    return sum(1 for registro in registros if registro["tipo"] == tipo)


def mayor_cobro(registros: list[dict]) -> int:
    """Devuelve el mayor valor cobrado en el día, o 0 si no hubo cobros."""
    return max((registro["valor"] for registro in registros), default=0)
