class PaginaTransferencias:

    
    def __init__(self, page):
        self.page = page
        #elementos
        self.campo_monto = page.get_by_role("spinbutton", name="Monto")
        self.campo_descripcion = page.get_by_role("textbox", name="Descripción (opcional)")
        self.boton_transferir = page.get_by_role("button", name="Transferir")
        self.mensaje_error_cuenta_origen = page.get_by_text("La cuenta origen y destino no")
        self.combo_cuenta_destino = page.locator("#destination-own-account")
        self.titulo_modal_confirmar_transferencia = page.get_by_role("heading", name="Confirmar Transferencia")
        self.boton_modal_cofirmar = page.get_by_role("button", name="Confirmar")
        self.titulo_pagina_transferencias = page.get_by_role("heading", name="Transferencias")
        self.mensaje_transferencia_realizada= page.get_by_text("Transferencia realizada")
        self.mensaje_bienvenido_bytext = page.get_by_text("¡Bienvenido! Inicio de sesión")
        self.mensaje_bienvenido_div = page.locator("div").nth(1)
    
    



    #metodos
    def ingrear_monto(self,monto):
        self.campo_monto.fill(monto)

    def seleccionar_segunda_cuenta_destino(self):
        self.combo_cuenta_destino.select_option("ACC002")

    def seleccionar_primera_cuenta_destino(self):
        self.combo_cuenta_destino.select_option("ACC001")

    def ingresar_descripcion(self,descripcion):
        self.campo_descripcion.fill(descripcion)

    def presionar_boton_transferir(self):
        self.boton_transferir.click()

    def presionar_boton_confirmar(self):
        self.boton_modal_cofirmar.click()

    