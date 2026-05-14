from playwright.sync_api import sync_playwright

def run():
    print("🚀 Iniciando prueba de Playwright...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("🌐 Abriendo página...")
        page.goto("https://example.com")

        title = page.title()
        print(f"✅ Título de la página: {title}")

        print("📸 Tomando screenshot...")
        page.screenshot(path="example.png")

        browser.close()
        print("✅ Prueba completada correctamente!")

if __name__ == "__main__":
    run()