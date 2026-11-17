def aplicar_recargo_nocturno(tarifa: int, hora_entrada: int) -> int:
    if hora_entrada >= 20 or hora_entrada <= 5:
        return tarifa + 2000
    return tarifa
