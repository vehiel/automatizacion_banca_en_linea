from paginas.pagina_transferencias import PaginaTransferencias
from playwright.sync_api import expect
from paginas.datos import DatosTransferencias


class TransferenciasAcciones:

    def __init__(self, page):
        self.transferencias = PaginaTransferencias(page)

    def validar_titulo(self):
        texto = self.transferencias.titulo_pagina_transferencias.text_content()
        #print(f"Título obtenido: {texto}")
        return "Transferencias" == texto

    def realizar_transaccion_10(self, monto, descripcion):
        expect(self.transferencias.boton_transferir).to_be_visible() #se le tuvo que agregar un expect para que espere el botón, porque lo hacia demasiado rápido y daba error
        self.transferencias.seleccionar_segunda_cuenta_destino()
        self.transferencias.ingrear_monto(monto)
        self.transferencias.ingresar_descripcion(descripcion)
        self.transferencias.presionar_boton_transferir()
        expect( self.transferencias.titulo_modal_confirmar_transferencia).to_be_visible()
        self.transferencias.presionar_boton_confirmar()
        expect(self.transferencias.mensaje_transferencia_realizada).to_be_visible()

    def realizar_transaccion_fallida(self,monto, descripcion):
        expect(self.transferencias.mensaje_bienvenido_bytext).not_to_be_visible() #se agrega con la intensión de esperar algun tiempo, para que no de error
        expect(self.transferencias.boton_transferir).to_be_visible() #se le tuvo que agregar un expect para que espere el botón, porque lo hacia demasiado rápido y daba error
        self.transferencias.ingrear_monto(monto)
        self.transferencias.ingresar_descripcion(descripcion)
        self.transferencias.presionar_boton_transferir()

    def validar_mesaje_error_transferencia(self):
            texto = self.transferencias.mensaje_error_cuenta_origen.text_content()
            #print(f"texto obtenido: {texto}")
            expect(self.transferencias.mensaje_error_cuenta_origen).to_be_visible()
            return DatosTransferencias.dato_mensaje_error_cuenta_origen == texto