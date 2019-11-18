from invoke import task, run
import os

@task
def install(c):
    print("Instalando paquetes...")
    c.run("pip install -r requirements.txt")
    print("Instalación finalizada.")


@task
def test(c):
    print("Ejecutando tests...")
    c.run("pytest -q tests/test_*.py")
    print("Ejecución de tests finalizada.")


@task
def coverage(c):
    print("Test de cobertura...")
    c.run("pytest --cov=Mercado --cov=Portfolio tests/")
    print("Test de cobertura finalizado.")


@task
def clean(c):
    print("Limpiando proyecto...")

    files_to_delete = [".coverage"]

    folders_to_delete = [".pytest_cache"]
    folders_to_delete.append("./tests/__pycache__")
    folders_to_delete.append("./Portfolio/__pycache__")
    folders_to_delete.append("./Mercado/__pycache__")

    for file in files_to_delete:
        if os.path.isfile(file):
            c.run("rm " + file)

    for folder in folders_to_delete:
        if os.path.isdir(folder):
            c.run("rm -r " + folder)

    print("Limpieza finalizada.")
