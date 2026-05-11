@echo off

Rem install python (latest version)
winget configure -f https://aka.ms/python-config

Rem this install file assumes cloning to C:\Users\%username%\ and running inside C:\Users\%username%\French-Vocab-Quiz\

python -m ensurepip --upgrade
Rem should install pip (for python module dependencies)

pip install -r requirements.txt

touch C:\Users\%username%\French-Vocab-Quiz\.config.txt
python C:\Users\%username%\French-Vocab-Quiz\quiz.py load


doskey frenchQuiz=python C:\Users\%username%\French-Vocab-Quiz\quiz.py start

Rem Write a persistent alias batch file to a folder on PATH
echo @echo off > C:\Users\%username%\AppData\Local\Microsoft\WindowsApps\frenchQuiz.bat
echo python C:\Users\%username%\French-Vocab-Quiz\quiz.py start >> C:\Users\%username%\AppData\Local\Microsoft\WindowsApps\frenchQuiz.bat

move install.bat C:\Users\%username%\French-Vocab-Quiz\.install.bat
move install.sh C:\Users\%username%\French-Vocab-Quiz\.install.sh
