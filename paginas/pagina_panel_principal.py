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
    
    #elementos


    #metodos
    def ingresar_opcion_transferencias(self):
        self.opcion_transferencias.click()