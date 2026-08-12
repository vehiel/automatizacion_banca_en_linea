from paginas.pagina_transferencias import PaginaTransferencias


class TransferenciasAcciones:

    def __init__(self, page):
        self.transferencias = PaginaTransferencias(page)

    def validar_titulo(self):
        texto = self.transferencias.titulo_pagina_transferencias.text_content()
        print(f"Título obtenido: {texto}")
        return "Transferencias" == texto