from invoke import task, run
import os
import sys

@task
def install(c):
    """
    Función para instalar las dependencias del proyecto
    """
    print("Instalando paquetes...")
    c.run("pip install -r requirements.txt")
    print("Instalación finalizada.")


@task
def test(c):
    """
    Función para ejecutar los tests unitarios
    """
    print("Ejecutando tests...")
    c.run("pytest -q tests/test_*.py")
    print("Ejecución de tests finalizada.")


@task
def coverage(c):
    """
    Función para ejecutar los tests de cobertura
    """
    print("Test de cobertura...")
    c.run("pytest --cov=Mercado --cov=Portfolio tests/")
    print("Test de cobertura finalizado.")


@task
def clean(c):
    """
    Función para limpiar el proyecto
    """
    print("Limpiando proyecto...")
    files_to_delete = [".coverage"]

    folders_to_delete = [".pytest_cache"]
    folders_to_delete.append("./tests/__pycache__")
    folders_to_delete.append("./src/__pycache__")
    folders_to_delete.append("./src/Portfolio/__pycache__")
    folders_to_delete.append("./src/Portfolio/.pytest_cache")
    folders_to_delete.append("./src/Mercado/__pycache__")

    for f in files_to_delete:
        if os.path.isfile(f):
            c.run("rm " + f)

    for d in folders_to_delete:
        if os.path.isdir(d):
            c.run("rm -r " + d)

    c.run("rm -r src/Portfolio/portfolio_db.pyc")

    print("Limpieza finalizada.")

@task
def start(c, host="0.0.0.0", port="8000", db = 'localhost:27017'):
    sys.path.append('src')
    os.environ['DB_URI'] = db
    c.run("gunicorn server:app --bind " + host + ":" + port + " -p pid_server")

@task
def stop(c):
    c.run('kill -9 $(cat pid_server)')
    c.run('rm pid_server')
