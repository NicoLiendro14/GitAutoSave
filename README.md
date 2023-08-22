# AutoCommit and AutoPush Script

Este proyecto consiste en un script en Python que realiza commits automáticos y pushes en un repositorio local de Git cada 5 minutos, en caso de haber cambios no confirmados o archivos nuevos.

## Requisitos previos

- Python 3.8 o superior instalado en tu sistema.
- Git instalado en tu sistema.
- Virtualenv (para crear un entorno virtual aislado).

## Configuración

1. Clona este repositorio o copia el contenido del script en tu máquina.

2. En la terminal, navega a la ubicación del proyecto.

3. Crea un entorno virtual (venv) para aislar las dependencias:

   ```bash
   python3 -m venv venv
    ```
4. Activa el entorno virtual:

    En Windows:

    ```bash 
    venv\Scripts\activate
    ```

5. En macOS y Linux:
    ```bash
    source venv/bin/activate
    ```

6. Instala la dependencia necesaria (GitPython):

```bash
pip install gitpython
```

## Uso

Asegúrate de estar en el entorno virtual antes de ejecutar el script.

Configura la ruta de tu repositorio local en el archivo auto_commit_push.py modificando la variable repo_path.

Ejecuta el script:

```bash
python auto_commit_push.py
```

El script comenzará a monitorear el repositorio cada 5 minutos y realizará commits y pushes automáticos si hay cambios no confirmados o archivos nuevos.

Detén el script manualmente cuando desees finalizar el proceso.

## Notas

    Este script fue creado para propósitos educativos y de demostración. No se recomienda su uso en entornos de producción sin modificaciones y configuraciones adicionales.
    Asegúrate de no almacenar información sensible, como contraseñas, en el repositorio antes de utilizar este script en un entorno real.
