import pytest

from bikeparq.recargo import aplicar_recargo_nocturno


def test_r1_tarifa_3000_a_las_22_da_5000():
    assert aplicar_recargo_nocturno(3000, 22) == 5000


def test_r1_a_las_20_empieza_la_noche_y_hay_recargo():
    assert aplicar_recargo_nocturno(3000, 20) == 5000


def test_r1_a_las_5_todavia_es_de_noche_y_hay_recargo():
    assert aplicar_recargo_nocturno(3000, 5) == 5000


def test_r2_tarifa_3000_a_las_10_no_cambia():
    assert aplicar_recargo_nocturno(3000, 10) == 3000


def test_r2_a_las_19_todavia_es_de_dia_y_no_hay_recargo():
    assert aplicar_recargo_nocturno(3000, 19) == 3000


def test_r2_a_las_6_empieza_el_dia_y_no_hay_recargo():
    assert aplicar_recargo_nocturno(3000, 6) == 3000


def test_r3_tarifa_0_de_noche_no_tiene_recargo():
    assert aplicar_recargo_nocturno(0, 23) == 0


def test_r4_hora_24_lanza_value_error():
    with pytest.raises(ValueError):
        aplicar_recargo_nocturno(3000, 24)


def test_r4_hora_negativa_lanza_value_error():
    with pytest.raises(ValueError):
        aplicar_recargo_nocturno(3000, -1)
