@echo off
Rem install python (latest version)
winget configure -f https://aka.ms/python-config

Rem this install file assumes cloning to C:\Users\%username%\ and running inside C:\Users\%username%\french-quiz\

python -m ensurepip --upgrade Rem should install pip (for python module dependencies)
pip install -r requirements.text

python3 C:\Users\%username%\french-quiz\quiz.py load
doskey frenchQuiz = "python3 C:\Users\%username%\french-quiz\quiz.py start"

mv install.bat C:\Users\%username%\french-quiz\.install.bat
mv install.sh C:\Users\%username%\french-quiz\.install.sh
