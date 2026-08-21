from paginas.pagina_panel_principal import PaginaPanelInicial
from playwright.sync_api import expect
from acciones.login_acciones import LoginAcciones
from paginas.datos import DatosPanelInicial

class PanelPrincipalAcciones:

    def __init__(self, page):
        self.PanelPrincipal = PaginaPanelInicial(page)
        self.loginacciones = LoginAcciones(page)

    def ingresar_transferencias(self):
        self.PanelPrincipal.ingresar_opcion_transferencias()

    def salir(self):
        expect(self.PanelPrincipal.boton_salir).to_be_visible()
        expect(self.PanelPrincipal.boton_salir).to_be_enabled()
        self.PanelPrincipal.presionar_salir()
        expect(self.PanelPrincipal.boton_confirmar_salir).to_be_visible
        self.PanelPrincipal.confirmar_salir()
        self.loginacciones.validar_pagina_inicial()

    def validar_nombre_usuario(self, nombre_usuario_login):
        elemento_dinamico = self.PanelPrincipal.obtener_nombre_usuario(DatosPanelInicial.nombre_usuario_1)
        expect(elemento_dinamico).to_be_visible
        segundo = elemento_dinamico.text_content()
        print(f"segundo: {segundo}")
        return segundo == DatosPanelInicial.nombre_usuario_1
