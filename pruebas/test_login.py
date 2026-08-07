from acciones.login_acciones import LoginAcciones

def test_login_page_load(page):
    acciones = LoginAcciones(page)
    acciones.iniciar_sesion(
        "admin",
        "admin123"
    )
    assert page.url !=""