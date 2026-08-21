from acciones.panel_principal_acciones import PanelPrincipalAcciones
from acciones.transferencias_acciones import TransferenciasAcciones
import pytest
from paginas.datos import DatosPanelInicial

@pytest.mark.skip(reason="En construcción") #se utiliza para saltar un test
def test_ingreso_transferencias(hacer_login):
    panel_principal = PanelPrincipalAcciones(hacer_login)
    panel_principal.ingresar_transferencias()
    transferencias = TransferenciasAcciones(hacer_login)
    assert transferencias.validar_titulo()
    transferencias.realizar_transaccion_10("10","vehiel demo")

def test_valiar_mensaje_cuenta_incorrecta(hacer_login_valido):
    panel_principal = PanelPrincipalAcciones(hacer_login_valido)
    assert panel_principal.validar_nombre_usuario(DatosPanelInicial.nombre_usuario_1)
    panel_principal.ingresar_transferencias()
    transferencias = TransferenciasAcciones(hacer_login_valido)
    transferencias.realizar_transaccion_fallida("100","fallida")
    assert transferencias.validar_mesaje_error_transferencia()


