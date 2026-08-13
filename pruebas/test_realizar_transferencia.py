from acciones.login_acciones import LoginAcciones
from acciones.panel_principal_acciones import PanelPrincipalAcciones
from acciones.transferencias_acciones import TransferenciasAcciones
import pytest
from acciones.login_acciones import LoginAcciones

@pytest.mark.skip(reason="En construcción")
def test_ingreso_transferencias(hacer_login):
    panel_principal = PanelPrincipalAcciones(hacer_login)
    panel_principal.ingresar_transferencias()
    transferencias = TransferenciasAcciones(hacer_login)
    assert transferencias.validar_titulo()
    transferencias.realizar_transaccion_10("10","vehiel demo")

def test_valiar_mensaje_cuenta_incorrecta(hacer_login):
    panel_principal = PanelPrincipalAcciones(hacer_login)
    panel_principal.ingresar_transferencias()
    transferencias = TransferenciasAcciones(hacer_login)
    transferencias.realizar_transaccion_fallida("100","fallida")
    assert transferencias.validar_mesaje_error_transferencia()
    panel_principal.salir()