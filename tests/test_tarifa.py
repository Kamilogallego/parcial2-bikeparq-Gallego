import pytest

from bikeparq.tarifa import calcular_tarifa


def test_cp01_carro_que_permanece_60_minutos_paga_3000():
    # Preparar
    minutos = 60
    tipo = "carro"

    # Ejecutar
    resultado = calcular_tarifa(minutos, tipo)

    # Verificar
    assert resultado == 3000


def test_cp02_moto_que_permanece_10_minutos_no_paga_por_tiempo_de_gracia():
    # Preparar
    minutos = 10
    tipo = "moto"

    # Ejecutar
    resultado = calcular_tarifa(minutos, tipo)

    # Verificar
    assert resultado == 0


def test_cp03_tipo_bicicleta_lanza_value_error():
    # Preparar
    minutos = 60
    tipo = "bicicleta"

    # Ejecutar y verificar
    with pytest.raises(ValueError):
        calcular_tarifa(minutos, tipo)


def test_minutos_negativos_lanzan_value_error():
    with pytest.raises(ValueError):
        calcular_tarifa(-1, "carro")


def test_mas_de_1440_minutos_lanzan_value_error():
    with pytest.raises(ValueError):
        calcular_tarifa(1441, "moto")


def test_carro_no_paga_mas_que_el_tope_diario():
    assert calcular_tarifa(1440, "carro") == 25_000
