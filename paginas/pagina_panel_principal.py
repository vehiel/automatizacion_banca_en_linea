class PaginaPanelInicial:
    def __init__(self, page):
        self.page = page
        self.titulo_pagina_panel_principal = page.get_by_role("heading", name="Panel Principal")
        self.opcion_transferencias = page.get_by_role("listitem").filter(has_text="Transferencias")
        self.opcion_mis_datos = page.get_by_role("listitem").filter(has_text="Mis Datos")
        self.opcion_plazos_fijos = page.get_by_role("listitem").filter(has_text="Plazos Fijos")
        self.opcion_prestamos = page.get_by_role("listitem").filter(has_text="Préstamos")
        self.opcion_pago_servicios = page.get_by_role("listitem").filter(has_text="Pago de Servicios")
        self.opcion_tarjetas_virtuales = page.locator("#menu-item-virtual-card")
        self.boton_salir = page.get_by_role("button", name="Salir")
        self.boton_cancelar_salir = page.get_by_role("button", name="Cancelar")
        self.boton_confirmar_salir = page.get_by_role("button", name="Confirmar")

    
    #elementos


    #metodos
    def ingresar_opcion_transferencias(self):
        self.opcion_transferencias.click()

    def presionar_salir(self):
        self.boton_salir.click()

    def confirmar_salir(self):
        self.boton_confirmar_salir.click()