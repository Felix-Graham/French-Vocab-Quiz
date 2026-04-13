#!/bin/bash

cd /home/$USER/ # go to user home directory

# Check if Python 3 is installed, install if not
if ! command -v python3 &> /dev/null; then
    sudo apt install -y python3
fi

python3 -m ensurepip --upgrade

pip install -r requirements.txt

python3 /home/$USER/French-Vocab-Quiz/quiz.py load

# Write persistent alias to ~/.bashrc
echo 'alias frenchQuiz="python3 /home/$USER/French-Vocab-Quiz/quiz.py start"' >> /home/$USER/.bashrc
source /home/$USER/.bashrc

mv install.sh /home/$USER/French-Vocab-Quiz/.install.sh
mv install.bat /home/$USER/French-Vocab-Quiz/.install.bat
