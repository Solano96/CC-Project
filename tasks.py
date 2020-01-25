from invoke import task, run
import os
import sys

@task
def install(c):
    """
    Función para instalar las dependencias del proyecto
    """
    print("Instalando paquetes...")
    c.run("pip3 install -r requirements.txt")
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
def start_market(c):
    """
    Función para desplegar el microservicio mercado
    """
    with c.cd("src/"):
        host_market = os.environ['HOST_MARKET']
        port_market = os.environ['PORT_MARKET']
        c.run("gunicorn --workers=9 --worker-class eventlet Mercado.server:app --bind " + host_market + ":" + port_market + " -p pid_server_market")

@task
def start_portfolio(c):
    """
    Función para desplegar el microservicio portfolio
    """
    with c.cd("src/"):
        host_portfolio = os.environ['HOST_PORTFOLIO']
        port_portfolio = os.environ['PORT_PORTFOLIO']
        c.run("gunicorn --workers=9 --worker-class eventlet Portfolio.server:app --bind " + host_portfolio + ":" + port_portfolio + " -p pid_server_portfolio")

@task
def stop(c):
    """
    Función para detener el servidor
    """
    c.run('kill -9 $(cat src/pid_server_market)')
    c.run('rm src/pid_server_market')

    c.run('kill -9 $(cat src/pid_server_portfolio)')
    c.run('rm src/pid_server_portfolio')
