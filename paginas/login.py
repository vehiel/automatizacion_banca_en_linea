class PaginaLogin:
    def __init__(self, page):
        self.page = page

#elementos
        self.input_usuario = page.get_by_role("textbox",name="Usuario")
        self.input_contrasena = page.get_by_role("textbox",name="Contraseña")
        self.btn_ingresar = page.get_by_role("button",name="Ingresar")
        self.titulo_pagina_login = page.get_by_role("heading", name="HOME BANKING")


#metodos
    def go_to(self):
        self.page.goto(
            "https://homebanking-demo-tests.netlify.app/"
        )

    def ingresar_usuario(self, usuario):
        self.input_usuario.fill(usuario)

    def ingresar_contrasena(self, contrasena):
        self.input_contrasena.fill(contrasena)

    def click_ingresar(self):
        self.btn_ingresar.click()
