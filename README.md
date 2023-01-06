# python-jacoco-android-coverage  
## Dependencies
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
## Installation  
- Clone this repository in your folder (git clone git@github.com:AMarturelo/python-jacoco-android-coverage.git)  
## Run  
- Ejecutar `python3 -b <branch> --verbose` para mostrar la cobertura de la rama seleccionada.  
- Ejecutar `python3 -h` para mostrar ayuda referente a los argumentos de entrada.
## Configuration
- Variable `repo_path` se modifica para especificar el path donde está el proyecto local. Si el script esta en la misma ruta se cambia por `./`.
- Variable `jacoco_html_report_path` se modifica para especificar el path donde se genera el reporte de jacoco. El reporte varía en función de la task de generación del mismo.