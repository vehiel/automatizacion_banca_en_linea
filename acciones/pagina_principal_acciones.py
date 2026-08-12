from paginas.pagina_panel_principal import PaginaPanelInicial


class PanelPrincipalAcciones:

    def __init__(self, page):
        self.PanelPrincipal = PaginaPanelInicial(page)

    def ingresar_transferencias(self):
        self.PanelPrincipal.ingresar_opcion_transferencias()