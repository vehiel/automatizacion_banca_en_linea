from acciones.loginAcciones import LoginAcciones

#se usa "test_" porque es la estructura para que playwright sepa que este es el test, tanto en el nombre de archivo
#como en el metodo definido acá
def test_login_page_load(page):
    acciones = LoginAcciones(page)

    acciones.cargarPagina()
    text = acciones.verificarElementos()
    assert text == "HOME BANKING"