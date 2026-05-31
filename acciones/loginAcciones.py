from paginas.login import PaginaLogin

class LoginAcciones:
    def __init__(self, page):
        self.loginPage = PaginaLogin (page)

    def cargarPagina(self):
        self.loginPage.go_to()

    def verificarElementos(self):
        self.loginPage.etiquetaTitulo.wait_for()
        assert self.loginPage.etiquetaTitulo.is_visible()
        text = self.loginPage.etiquetaTitulo.inner_text()
        print(f"el titulo es: {text}")
        return text