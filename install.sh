#!/bin/bash

cd /home/$USER/ # go to user home directory

if [ python --version == "Python 3.12.12"]; then
 else 
    sudo apt install python
fi 
python -m ensurepip --upgrade
pip install -r requirements.text

python3 /home/$USER/french-quiz/quiz.py load
alias frenchQuiz = "python3 /home/$USER/french-quiz/quiz.py start"

mv install.sh /home/$USER/french-quiz/.install.sh
mv install.bat /home/$USER/french-quiz/.install.bat
