# Automatización Banca en Línea

Framework de automatización desarrollado con **Python**, **Playwright** y **Pytest**, utilizando una arquitectura basada en **Page Object Model (POM)** complementada con una capa de **Acciones** para separar la lógica de negocio de la interacción con los elementos de la interfaz.

---

## Objetivo

Automatizar los principales flujos funcionales de la aplicación de Banca en Línea, garantizando:

- Validación de funcionalidades críticas.
- Reducción del esfuerzo manual de pruebas.
- Ejecución repetible y confiable.
- Integración con herramientas de reportería.
- Escalabilidad para nuevos módulos.

---

## Tecnologías utilizadas

- Python 3
- Playwright
- Pytest
- Allure Reports
- Git
- GitHub Codespaces
- Visual Studio Code

---

## Arquitectura del proyecto

```text
automatizacion_banca_en_linea/
│
├── acciones/
│   ├── login_acciones.py
│   ├── panel_principal_acciones.py
│   └── transferencias_acciones.py
│
├── paginas/
│   ├── basePage.py
│   ├── login.py
│   ├── pagina_panel_principal.py
│   ├── pagina_transferencias.py
│   └── datos.py
│
├── pruebas/
│   ├── conftest.py
│   ├── test_login.py
│   └── test_realizar_transferencia.py
│
├── allure-results/
├── screenshots/
├── pytest.ini
└── README.md
```

---

## Patrón utilizado

### POM (Page Object Model)

La carpeta:

```text
paginas/
```

contiene:

- Localizadores.
- Elementos.
- Métodos simples de interacción.

Ejemplo:

```python
self.campo_usuario.fill(usuario)
```

---

### Acciones

La carpeta:

```text
acciones/
```

contiene:

- Flujos funcionales.
- Casos de negocio.
- Navegación entre pantallas.

Ejemplo:

```python
iniciar_sesion()
realizar_transferencia()
```

---

### Pruebas

La carpeta:

```text
pruebas/
```

contiene:

- Casos de prueba.
- Validaciones.
- Assertions.

Ejemplo:

```python
transferencias.realizar_transaccion_fallida("100","fallida")
assert transferencias.validar_mesaje_error_transferencia()
```

---

## Fixtures

El proyecto utiliza Pytest Fixtures para reutilizar funcionalidades comunes.
Además de poder tener flexibilidad para usar diferencias escenarios/usuarios sin tener que modificar una prueba por completo.

### Login válido

```python
hacer_login_valido
```

Realiza el inicio de sesión antes de ejecutar la prueba.

### Login incorrecto

```python
hacer_login_incorrecto
```

Utilizado para escenarios negativos.

### Usuario bloqueado

```python
hacer_login_bloqueado
```

Permite validar escenarios de acceso restringido.

---

## Ejecución de pruebas

Ejecutar todas las pruebas:

```bash
python -m pytest
```

Ejecutar una prueba específica:

```bash
python -m pytest pruebas/test_realizar_transferencia.py -v
```

Mostrar mensajes por consola:

```bash
python -m pytest -v -s
```

---

## Reportería

El proyecto utiliza Allure Reports.

### Generación de resultados

Los resultados se generan automáticamente en:

```text
allure-results/
```

gracias a la configuración de:

```ini
[pytest]
addopts = --alluredir=allure-results
```

### Visualización del reporte

```bash
allure serve allure-results
```

---

## Captura automática de errores

Cuando una prueba falla:

- Se captura una imagen.
- Se almacena en la carpeta:

```text
screenshots/
```

- Se adjunta automáticamente al reporte Allure.

Esto facilita el análisis y la identificación de defectos.

---

## Configuración automática de entorno

El proyecto cuenta con:

```text
postCreateCommand.sh
```

que instala automáticamente:

- Java
- Allure Commandline
- Playwright
- Dependencias del sistema
- Navegadores soportados

Esto permite reconstruir un Codespace completamente funcional sin configuraciones manuales.

---

## Flujo de trabajo Git

Crear una nueva rama:

```bash
git checkout -b nombre-rama
```

Actualizar desde main:

```bash
git checkout main
git pull origin main

git checkout nombre-rama
git merge main
```

Subir cambios:

```bash
git add .
git commit -m "Descripción del cambio"
git push origin nombre-rama
```

Posteriormente crear un Pull Request hacia:

```text
main
```

---


## Levantar codegen
```bash
python -m playwright codegen https://homebanking-demo-tests.netlify.app/
```


---
## Buenas prácticas del proyecto

- Mantener localizadores en la carpeta `paginas`.
- Mantener flujos funcionales en `acciones`.
- Mantener assertions únicamente en `pruebas`.
- Evitar quemar datos cuando sea posible.
- Utilizar locators robustos de Playwright usando codegen.
- Utilizar fixtures para funcionalidades reutilizables.
- Mantener las pruebas independientes entre sí.

---

## Próximas mejoras

- Screenshots en éxitos y fallos.
- Evidencias adicionales en Allure.
- Datos de prueba externos (JSON).
- Ejecución por tags.
- Métricas y dashboard de ejecución.

---

## Autor

**Vehiel Alemán Campos**

Quality Assurance Functional Specialist II

Proyecto de Automatización de Banca en Línea