class BasePage:

    def __init__(self, page):
        self.page = page

    def navegar(self, url):
        self.page.goto(url)