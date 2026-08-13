import pytest
from playwright.sync_api import sync_playwright
from acciones.login_acciones import LoginAcciones
from acciones.panel_principal_acciones import PanelPrincipalAcciones


@pytest.fixture
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        yield page

        browser.close()

@pytest.fixture
def hacer_login(page):
    login = LoginAcciones(page)
    panelprincipal = PanelPrincipalAcciones(page)
    login.iniciar_sesion("demo","demo123")
    return page
    panelprincipal.salir()
