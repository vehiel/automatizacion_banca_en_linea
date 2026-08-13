from paginas.login import PaginaLogin
from playwright.sync_api import expect


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