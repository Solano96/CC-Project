from invoke import task, run

@task
def install(c):
    c.run("pip install -r requirements.txt")

@task
def test(c):
    c.run("pytest -q tests/test_*.py")
