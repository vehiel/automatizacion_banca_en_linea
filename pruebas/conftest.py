import pytest
from playwright.sync_api import sync_playwright
from acciones.login_acciones import LoginAcciones
from acciones.panel_principal_acciones import PanelPrincipalAcciones
from paginas.datos import DatosLogin


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
def hacer_login_valido(page):
    login = LoginAcciones(page)
    panelprincipal = PanelPrincipalAcciones(page)
    login.iniciar_sesion(DatosLogin.usuario_valido,DatosLogin.contrasenna_valido)
    yield page
    panelprincipal.salir()

@pytest.fixture
def hacer_login_incorrecto(page):
    login = LoginAcciones(page)
    panelprincipal = PanelPrincipalAcciones(page)
    login.iniciar_sesion(DatosLogin.usuario_incorrecto,DatosLogin.usuario_incorrecto)
    yield page
    panelprincipal.salir()

@pytest.fixture
def hacer_login_bloqueado(page):
    login = LoginAcciones(page)
    panelprincipal = PanelPrincipalAcciones(page)
    login.iniciar_sesion(DatosLogin.usuario_bloq,DatosLogin.contrasenna_bloq)
    yield page
    panelprincipal.salir()