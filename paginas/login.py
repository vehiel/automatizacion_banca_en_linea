class PaginaLogin:
    def __init__(self, page):
        self.page = page

        # localizadores
        self.inputUsuario = page.get_by_role("textbox", name="Usuario")
        self.inputContrasena = page.get_by_role("textbox", name="Contraseña")
        self.bntIngresar = page.get_by_role("button", name="Ingresar")
        self.etiquetaTitulo = page.get_by_role("heading", name="HOME BANKING")

    # Métodos 
    def go_to(self):
        self.page.goto("https://homebanking-demo-tests.netlify.app/")

    def ingresarUsuarioContrasena(self, usuario: str, contrasena: str):
        self.inputUsuario.fill(usuario)
        self.inputContrasena.fill(contrasena)

    def clickIngresar(self):
        self.bntIngresar.click()
