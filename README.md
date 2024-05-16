# INSTALLING VIRTUAL ENVIRONMENT BEFORE OPENING VSCODE

```bash
cd /Desktop/Annicka/reservation-system
echo 'export PIPENV_VENV_IN_PROJECT=1' >> ~/.bashrc
source ~/.bashrc
pipenv --rm
pipenv lock
pipenv install
pipenv shell
code .
```

### Sometimes there can be opened cached terminal window in vscode project, one needs to close them all and open new one

### Then every opening of vscode in project folder runs virtual environment automatically

### Virtual environment is in .venv folder in the project folder and can be removed again by pipenv --rm from OUTSIDE of VSCODE
### but there is no specific reason to remove that when not installing upgrades of some python packages or installing new

### When one adds some new packages in Pipfile, one can just run pipenv lock, pipenv install from outside of virtual environment
### one can just exit that with command exit

### When one needs to remove some packages, one needs to always remove virtual environment, and Pipfile.lock,
### Remove packages from Pipfile and run again pipenv lock, pipenv install, pipenv shell

### -------------------------------------------------------------------------------------------


# DJANGO DOCUMENTATION 
### This application enables to use and administrating the reservation system

### https://docs.djangoproject.com/en/5.0/intro/tutorial04/

```python
import requests

def some_function():
    return
# this is just showing how in this documentation README.md file works so called MARKDOWN
# when one can for example document code with python or bash syntaxt markdown
# one can see the preview of the file while now pressing CTRL+SHIFT+v
```