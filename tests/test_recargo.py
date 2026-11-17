from bikeparq.recargo import aplicar_recargo_nocturno


def test_r1_tarifa_3000_a_las_22_da_5000():
    assert aplicar_recargo_nocturno(3000, 22) == 5000
