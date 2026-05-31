from acciones.loginAcciones import LoginAcciones

def test_login_page_load(page):
    acciones = LoginAcciones(page)

    acciones.cargarPagina()
    acciones.verificarElementos()