# automatizacion_banca_en_linea
automatización de banca en línea

se utiliza codegen para buscar selectores
se utiliza fixtures para tener un codigo más limpio y escalable
se utiliza metodologia POM al inicio, pensando migrar a Screenplay pattern si el proyecto se vuelve demasiado grande

comandos
python -m pytest pruebas/test_login.py -v
python -m pytest pruebas/test_realizar_transferencia.py -v

levantar codegen
python -m playwright codegen https://homebanking-demo-tests.netlify.app/