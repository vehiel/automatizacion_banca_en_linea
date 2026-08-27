import pytest
from playwright.sync_api import sync_playwright
from acciones.login_acciones import LoginAcciones
from acciones.panel_principal_acciones import PanelPrincipalAcciones
from paginas.datos import DatosLogin
import os
import allure


@pytest.fixture
def page(request):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        yield page

       #print("Entrando a validación de fallo")
        #print(request.node.rep_call)
        #print(request.node.rep_call.failed)
        if request.node.rep_call.failed:

            #print("La prueba falló")

            os.makedirs("screenshots", exist_ok=True)

            screenshot = (
                f"screenshots/{request.node.name}.png"
            )

            page.screenshot(path=screenshot)
            #print("Screenshot generado")

            allure.attach.file(
                screenshot,
                name="Screenshot Error",
                attachment_type=allure.attachment_type.PNG
            )

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
    return page

@pytest.fixture
def hacer_login_bloqueado(page):
    login = LoginAcciones(page)
    panelprincipal = PanelPrincipalAcciones(page)
    login.iniciar_sesion(DatosLogin.usuario_bloq,DatosLogin.contrasenna_bloq)
    return page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    rep = outcome.get_result()

    setattr(
        item,
        "rep_" + rep.when,
        rep
    )