from invoke import task, run
import os

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
    folders_to_delete.append("./Portfolio/__pycache__")
    folders_to_delete.append("./Mercado/__pycache__")

    for f in files_to_delete:
        if os.path.isfile(f):
            c.run("rm " + f)

    for d in folders_to_delete:
        if os.path.isdir(d):
            c.run("rm -r " + d)

    print("Limpieza finalizada.")
