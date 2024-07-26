# Steps:

## Create a new repository in Github: First Flask App

-	Public
-	Do not check: Add a README file
-	Do not choose: Add .gitignore
-	Do not choose: Choose a license

## Start Windows PowerShell with the "Run as administrator":

?> Set-ExecutionPolicy Unrestricted

## Go to your favorite path…

?> mkdir FirstFlaskApp \
?> cd FirstFlaskApp

## Create .gitignore file:

-	In Linux: ?> touch .gitignore
-	In Windows PowerShell: ?> ni .gitignore
-	In Windows Command Prompt: ?> type nul > .gitignore

FirstFlaskApp> echo ".vscode/" >> .gitignore \
FirstFlaskApp> echo ".venv/" >> .gitignore \
FirstFlaskApp> echo "\_\_pycache\_\_/" >> .gitignore \
FirstFlaskApp> cat .gitignore

### Note: Open .gitignore file in NotePad and choose Save As and change the Encoding from UTF-16 LE to UTF-8! &rarr; https://stackoverflow.com/questions/24410208/gitignore-does-not-ignore-folder

FirstFlaskApp> git init \
FirstFlaskApp> dir -Attributes:h \
FirstFlaskApp> git status \
FirstFlaskApp> git add -A \
FirstFlaskApp> git status \
FirstFlaskApp> git commit -m "First Commit" \
FirstFlaskApp> git status \
FirstFlaskApp> git branch -M main \
FirstFlaskApp> git remote add origin git@github.com:Dariush-Tasdighi/First-Flask-App.git \
FirstFlaskApp> git push -u origin main \
FirstFlaskApp> git status

## Browse: https://github.com/Dariush-Tasdighi/First-Flask-App

FirstFlaskApp> python -m venv .venv \
FirstFlaskApp> .venv\Scripts\activate \
(.venv) FirstFlaskApp> pip list \
(.venv) FirstFlaskApp> python.exe -m pip install --upgrade pip \
(.venv) FirstFlaskApp> pip install flask \
(.venv) FirstFlaskApp> code .

##	Create file: app.py
## Write your code in app.py
##	run and debug app.py!
-	F5 &rarr; Python Debugger &rarr; Python File
## Exit VSCode

(.venv) FirstFlaskApp> pip freeze > requirements.txt \
(.venv) FirstFlaskApp> pip install -r requirements.txt \
(.venv) FirstFlaskApp> dir \
(.venv) FirstFlaskApp> deactivate \
FirstFlaskApp> git status \
FirstFlaskApp> git add -A \
FirstFlaskApp> git status \
FirstFlaskApp> git commit -m "Version 1.0" \
FirstFlaskApp> git status \
FirstFlaskApp> git push \
FirstFlaskApp> git status
