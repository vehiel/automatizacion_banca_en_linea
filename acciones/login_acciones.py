from paginas.login import PaginaLogin


class LoginAcciones:

    def __init__(self, page):
        self.login = PaginaLogin(page)

    def iniciar_sesion(self, usuario, contrasena):
        self.login.go_to()
        self.login.ingresar_usuario(usuario)
        self.login.ingresar_contrasena(contrasena)
        self.login.click_ingresar()