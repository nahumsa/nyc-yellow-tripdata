import nox

PROJECT_FOLDERS = [
    "tests", "etl"
]

@nox.session(name="tests")
def tests_coverage(session):
    """ Run pytest and create coverage report.
    """
    session.install("pipenv")
    session.run("pipenv", "install", "--dev")
    session.run("pytest", "--cov=./")

@nox.session(name="style")
def check_style(session):
    """ Install black and test if the linting is correct.
    """
    session.install("black")
    session.install("isort")
    session.run("black", "--check", "--diff", *PROJECT_FOLDERS)
    session.run("isort", "--profile", "black", *PROJECT_FOLDERS)
    
@nox.session(name="fmt")
def apply_style(session):
    """ Install black and test if the linting is correct.
    """
    session.install("black")
    session.install("isort")
    session.run("black", *PROJECT_FOLDERS)
    session.run("isort", "--profile", "black", *PROJECT_FOLDERS)