from paginas.login import PaginaLogin
from playwright.sync_api import expect
from paginas.datos import DatosLogin


class LoginAcciones:

    def __init__(self, page):
        self.login = PaginaLogin(page)

    def iniciar_sesion(self, usuario, contrasena):
        self.login.go_to()
        self.login.ingresar_usuario(usuario)
        self.login.ingresar_contrasena(contrasena)
        self.login.click_ingresar()

    def validar_pagina_inicial(self):
       expect(self.login.titulo_pagina_login).to_be_visible()

    def validar_mensaje_cuenta_bloqueada(self):
        expect(self.login.mensaje_cuenta_bloqueada).to_be_visible
        return self.login.mensaje_cuenta_bloqueada.text_content() == DatosLogin.texto_mensaje_cuenta_bloqueada

    def validar_mensaje_usuario_incorrecto(self):
            expect(self.login.mensaje_usuario_incorrecto).to_be_visible
            return self.login.mensaje_usuario_incorrecto.text_content() == DatosLogin.texto_mensaje_usuario_incorrecto