from acciones.login_acciones import LoginAcciones
from acciones.panel_principal_acciones import PanelPrincipalAcciones
from acciones.transferencias_acciones import TransferenciasAcciones
import pytest

#@pytest.mark.skip(reason="En construcción") #se utiliza para saltar un test
def test_validar_usuario_incorrecto(hacer_login_incorrecto):
    #este test funciona solo 1 o 2 veces, luego de eso la cuenta se bloquea y el mensaje cambia
    login = LoginAcciones(hacer_login_incorrecto)
    assert login.validar_mensaje_usuario_incorrecto()

@pytest.mark.skip(reason="En construcción") #se utiliza para saltar un test
def test_validar_usuario_bloqueado(hacer_login_bloqueado):
    login = LoginAcciones(hacer_login_bloqueado)
    assert login.validar_mensaje_cuenta_bloqueada()
