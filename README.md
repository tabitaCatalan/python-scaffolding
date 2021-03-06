# Practical MLOps: Chapter 1 - Exercises 1 and 2 

## Objetive
1. Create a new GitHub repository with necessary Python scaffolding using a Make file, linting, and testing. Then, perform additional steps such as code formatting in your Makefile.
2. Using GitHub Actions, test a GitHub project with two or more Python versions.

## Resources 
Some interesting resources I read while working on this repo.
1. [Creating a Python Makefile](https://earthly.dev/blog/python-makefile/)
2. [A Simple Makefile Tutorial](https://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/)
3. [Run tests for multiple language versions in GitHub actions in a Docker container](https://stackoverflow.com/a/61428673/14970034)
## What did I do 
1. Instalar `pip` en Ubuntu siguiendo [esto](https://packaging.python.org/guides/installing-using-linux-tools/#debian-ubuntu)
```
$ sudo apt update
$ sudo apt install python3-venv python3-pip
```
2. Crear virtual environment
```
$ python3 -m venv env
```
3. Activar ambiente 
```
$ source env/bin/activate
```
4. Verificar que se esté usando la versión correcta de python
```
(env) $ which python
.../env/bin/python
```
5. Instalar requerimientos usando `requirements.txt`
```
$ pip install -r requirements.txt
```
6. Instalar `pylint`
```
pip install pylint --upgrade
```
7. Instalar `pytest` y el plugin `pytest-cov` para test y coverage
```
pip install -U pytest
pip install pytest-cov
```

8. Desactivar ambiente 
```
$ deactivate
```

