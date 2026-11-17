def aplicar_recargo_nocturno(tarifa: int, hora_entrada: int) -> int:
    if tarifa == 0:
        return 0
    if hora_entrada >= 20 or hora_entrada <= 5:
        return tarifa + 2000
    return tarifa
