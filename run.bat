@echo off

set VENV_FOLDER=venv
set MAIN_SCRIPT=main.py

rem Verificar si la carpeta "venv" existe
if not exist %VENV_FOLDER% (
    echo Creando entorno virtual...
    python -m venv %VENV_FOLDER%
)

rem Activar el entorno virtual
call %VENV_FOLDER%\Scripts\activate

rem Instalar GitPython
pip install gitpython

rem Ejecutar el script principal
python %MAIN_SCRIPT%

rem Finalizar el entorno virtual
deactivate
