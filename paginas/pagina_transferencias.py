class PaginaTransferencias:

    def __init__(self, page):
        self.page = page
        self.campo_monto = page.get_by_role("spinbutton", name="Monto")
        self.campo_descripcion = page.get_by_role("textbox", name="Descripción (opcional)")
        self.boton_transferir = page.get_by_role("button", name="Transferir")
        self.mensaje_error_cuenta_orgigen = page.get_by_text("La cuenta origen y destino no")
        self.combo_cuenta_destino = page.locator("#destination-own-account")
        self.titulo_modal_confirmar_transferencia = page.get_by_role("heading", name="Confirmar Transferencia")
        self.boton_modal_cofirmar = page.get_by_role("button", name="Confirmar")
        self.titulo_pagina_transferencias = page.get_by_role("heading", name="Transferencias")
    #elementos
    
    



    #metodos
    def ingrear_monto(self):
        self.campo_monto.fill("10")
    