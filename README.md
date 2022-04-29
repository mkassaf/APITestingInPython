# API Testing In Python


# Setup
- Create a dirctory for the app: ie  
```console
mkdir testing
cd testing 
```
- Clone the project: 
```console
git clone git@github.com:mkassaf/APITestingInPython.git
```
- Go to the app:  
```console 
cd APITestingInPython 
```
- Creating virtual environments:  
```console
python3 -m venv vnev
```
- Activate virtual environment: 
```console
source vnev/bin/activate 
```
- install the dependanceies:  
```console
pip3 install -r requirements.txt 
```
# or using pipenv
Ensure you have
[pipenv already installed](https://automationhacks.io/2020/07/12/how-to-manage-your-python-virtualenvs-with-pipenv/):

```zsh

# Activate virtualenv
pipenv shell
# Install all dependencies in your virtualenv
pipenv install

```
# How to run
 
```zsh

 # Run tests via pytest (single threaded)
python -m pytest -s tests_api.py

# Run tests in parallel
python -m pytest -n auto tests_api.py 

# Report results to report portal
python -m pytest -n auto tests_api.py --reportportal 

```


# Refernces 

