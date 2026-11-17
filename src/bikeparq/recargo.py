RECARGO_NOCTURNO = 2000
HORA_MINIMA = 0
HORA_MAXIMA = 23
INICIO_DE_LA_NOCHE = 20
FIN_DE_LA_NOCHE = 5


def es_horario_nocturno(hora: int) -> bool:
    """Indica si la hora (0 a 23) está en el horario nocturno: de 20 a 23 o de 0 a 5."""
    return hora >= INICIO_DE_LA_NOCHE or hora <= FIN_DE_LA_NOCHE


def aplicar_recargo_nocturno(tarifa: int, hora_entrada: int) -> int:
    """Devuelve el total a pagar: la tarifa más el recargo si entró de noche."""
    if hora_entrada < HORA_MINIMA or hora_entrada > HORA_MAXIMA:
        raise ValueError("La hora de entrada debe estar entre 0 y 23")
    if tarifa == 0 or not es_horario_nocturno(hora_entrada):
        return tarifa
    return tarifa + RECARGO_NOCTURNO
