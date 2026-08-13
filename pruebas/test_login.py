from acciones.login_acciones import LoginAcciones
from acciones.panel_principal_acciones import PanelPrincipalAcciones
from acciones.transferencias_acciones import TransferenciasAcciones


def test_ingreso_transferencias(page):

    login = LoginAcciones(page)

    login.iniciar_sesion(
        "demo",
        "demo123"
    )

    pp = PanelPrincipalAcciones(page)

    pp.ingresar_transferencias()

    transferencias = TransferenciasAcciones(page)

    assert transferencias.validar_titulo()