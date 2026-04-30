import random
import time
import datetime
import os
import argparse
import sys
import fuzzywuzzy
from fuzzywuzzy import fuzz
##################
# Misc Variables #
##################
global configContent
global streak
global date 
global SCORE
global ansWideRangeActive
global ansScoreActive



SCORE = 0

date = (datetime.date.today()).day

with open("config.txt", "r") as f:
    configContent = f.readlines()
    configContent = [s.rstrip() for s in configContent]
    f.close()

###########
# Streaks #
###########

def isNewDayToIncrementStreak():
    updateContent = configContent.index("Streaks")

    #print(configContent[updateContent+3])
    #print(date)
    #time.sleep(1)

    if configContent[updateContent+3] == date:
        return True
    else:
        return False


def incrementStreak():
    with open("config.txt", "r") as d:
        oldContent = d.readlines()
        d.close()
    with open("config.txt", "w") as f:
        niceOldContent = [s.rstrip() for s in oldContent]
        updateContent = niceOldContent.index("Streaks")
        #configContent[updateContent+2] = f"{int(configContent[updateContent+2]) + 1}\n\n"
        streakNum = int(configContent[updateContent+2]) + 1
        oldContent[updateContent+2] = f"{streakNum}\n"
        f.writelines(oldContent)
        print(f"Old Content: {oldContent}")
        
        

        f.close()

def killStreak():
    with open("config.txt", "r") as d:
        oldContent = d.readlines()
        d.close()
    with open("config.txt", "w") as f:
        niceOldContent = [s.rstrip() for s in oldContent]
        updateContent = niceOldContent.index("Streaks")
        #configContent[updateContent+2] = f"{int(configContent[updateContent+2]) + 1}\n\n"
        streakNum = 0
        oldContent[updateContent+2] = f"{streakNum}\n"
        f.writelines(oldContent)
        print(f"Old Content: {oldContent}")

def getStreak():
    with open("config.txt", "r") as f:
        configContent = f.readlines()
        configContent = [s.rstrip() for s in configContent]
        updateContent = configContent.index("Streaks")
        #print(configContent[updateContent+2])
        f.close()
    return configContent[updateContent+2]





###########
# Install #
###########

""" 

Installation is done through either the `install.bat` or `install.sh` files, for windows or chromeOS respectively.
Currently MacOS is not accounted for due to lack of demand.

"""

##############
# menu page  #
##############

def plug():
    os.system("clear")
    print("French Vocabulary Quiz\n")
    print("Written by Felix Graham\n")
    print("https://github.com/Felix-Graham/French-Vocab-Quiz")
    print("\n\n")
    enter = input()
    os.system("clear")

def home():

    


    print(streak)
    print(isNewDayToIncrementStreak())
    if isNewDayToIncrementStreak():
        incrementStreak()
    else:
        pass

    updateContent = configContent.index("Streaks")
    if date -1 > int(configContent[updateContent+3]):
        killStreak()
    #print(streak)
    #time.sleep(5)


    os.system("clear")
    print("""                      Home                    
             
             Streaks: """ + configContent[11] + """


            Commands (c)

            Start (s)
            
            Update (u)

            Settings (i)

            Quit (q)

          """)

    opt = input("\t")
    if opt == "c":
        commands()
    elif opt == "s":
        main(start())
    elif opt == "u":
        update()
    elif opt == "q":
        quit()
    elif opt == "i":
        settings()
        pass
    else:
        home()

############
# Settings #
############

def settings():
    os.system("clear")
    print("                          Settings \n\n")

    print("""                 

            Alias (a)

            Streaks (s)
            
            Updates (u)

            Question Settings (e)

            Quit (q)


          """)
    
    opt = input("\t")
    if opt == "q":
        reload()
        home()
    elif opt == "a":
        aliasMenu()
    elif opt == "s":
        streaks()
    elif opt == "u":
        updateMenu()
    elif opt == "e":
        questionSettings()
    else:
        settings()

def questionSettings():
    os.system("clear")

    with open("config.txt", "r+") as f:
        print("        Question Settings Menu \n\n")
        #configContent = f.readlines()
        try:
            updateContent = configContent.index("Answers")
            # display current settings 
            print(f"Answers\nScore\n{configContent[updateContent+1].strip()}\nAnsWideRange\n{configContent[updateContent+3].strip()}\n\n")

            # update settings 
            print("Score (y/n)")
            update = input("> ")
            if update == "y":
                configContent[updateContent+1] = f"{True}\n"
            elif update == "n":
                configContent[updateContent+1] = f"{False}\n"

            print("Accept a Wide Range of Answers (y/n)")
            update = input("> ")
            if update == "y":
                configContent[updateContent+3] = f"{True}\n\n"
            elif update == "n":
                configContent[updateContent+3] = f"{False}\n\n"

        except:
            autoconf(questionSettings)
          
        f.close()
    settings()
    pass


def aliasMenu():
    os.system("clear")
    print("        Alias Menu \n\n")
           
    print("Tired of typing in a lengthy command? \nYou may be eligible for greatness. Introducing 'alias'. Sign below to continue.\n(q to quit)\n\n")
    signature = input("_________\r")
    if signature == "q":
        home()
    elif len(signature) < 3:
        print("That's not your fucking name.")
        quit()
    os.system("clear")
    print("        Device Alias \n\n")
    alias()


def streaks():
    os.system("clear")

    with open("config.txt", "r+") as f:
        print("        Streaks Menu \n\n")
        #configContent = f.readlines()
        updateContent = configContent.index("Streaks")
        # display current settings 
        print(f"Streaks\n{configContent[updateContent+1].strip()}\n")

        # update settings 
        print("Enable Streaks (y/n)")
        update = input("> ")
        if update == "y":
            configContent[updateContent+1] = f"{True}\n\n"
        elif update == "n":
            configContent[updateContent+1] = f"{False}\n\n"

        f.close()
    settings()
    pass

def updateMenu():
    os.system("clear")

    with open("config.txt", "r+") as f:
        print("        Update Menu \n\n")
        #configContent = f.readlines()
        try:
            updateContent = configContent.index("Updates")
            # display current settings 
            print(f"Updates\nAlwaysUpdate\n{configContent[updateContent+1].strip()}\nAskBeforeUpdate\n{configContent[updateContent+3].strip()}\n\n")

            # update settings 
            print("Always Update (y/n)")
            update = input("> ")
            if update == "y":
                configContent[updateContent+1] = f"{True}\n"
            elif update == "n":
                configContent[updateContent+1] = f"{False}\n"

            print("Ask Before Update (y/n)")
            update = input("> ")
            if update == "y":
                configContent[updateContent+3] = f"Updates\nAskBeforeUpdate\n{True}\n\n"
            elif update == "n":
                configContent[updateContent+3] = f"Updates\nAskBeforeUpdate\n{False}\n\n"

        except:
            autoconf(updateMenu)
          
        f.close()
    settings()
    pass

def alias():
    with open("config.txt", "r+") as f:
        print("What Operating System are you using? \n")
        bos = input("Windows (w) \nMacOS (m) \nChromeOS (c) \n> ")
        if bos == 'q':
            home()
        name = input("Choose a name for this command: ")

        if bos == "c":
            bashrc_path = os.path.expanduser("~/.bashrc")
            script_path = os.path.abspath(sys.argv[0])
            with open(bashrc_path, "a") as f:
                f.write(f"\nalias {name}='python3 {script_path}'\n")
            print(f"Alias '{name}' added. Run 'source ~/.bashrc' or restart your terminal for it to take effect.")
            input()
            f.write("""Alias\n
                    True\n
                    \n""")

        elif bos == 'm':
            #os.system(f"alias {name}='python3 quiz.py start'")
            print("I can't help you")
            input()
        elif bos == 'w':
            #os.system(f"alias {name}='python3 quiz.py start'")
            with open("quizAlias.bat", "w") as g:
                g.write("python3 quiz.py start")
                g.close()
            f.write("""Alias\n
                    True\n
                    \n""")

        else:
            print("Invalid option")
            time.sleep(2)
            os.system("clear")
            settings()

            f.close()
    home()

    




def start():
    os.system("clear")
    
    print("Select quiz type:")
    print("1) Traditional (type answer)")
    print("2) Multiple choice")
    type = input("> ")

    return type


def commands():
    os.system("clear")
    print("""   Basic commands for people who want to bypass the menu:
    
            These are for typing in the command to the terminal.

            python3 quiz.py select -> starts the quiz in select mode
            python3 quiz.py all -> starts the quiz in all 
            python3 quiz.py load -> loads the config file 
            python3 quiz.py update -> updates the script 
            python3 quiz.py start -> opens to main menu

            
          """)
    x = input()
    os.system("clear")
    home()
    pass


##############
# autoupdate #
##############

def autoupdate():
    try:
        os.system("git pull")
        #os.system("python3 quiz.py select")
    except:
        pass

def update():
    try:
        os.system("git pull")
    except:
        try:
            os.chdir("")
            os.system("git clone https://github.com/Felix-Graham/French-Vocab-Quiz.git")
        except:
            os.chdir("")
            os.system("gh repo clone Felix-Graham/French-Vocab-Quiz")
    finally:
        #print("Updated (in theory)")
        time.sleep(1)
    home()



############
# autoconf #
############
CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "config.txt")

def autoconf(returnLocation):
    homedir = os.path.dirname(os.path.abspath(sys.argv[0]))
    #print(homedir)
    #print(CONFIG_PATH)

    with open(CONFIG_PATH, "r+") as f:
        f.seek(0)
        if homedir in configContent:
            pass
        else:
            load(10, 0.1, "Configuring Launch Directory")
            f.write(f"Directory\n{homedir}\n\n")

        #setting defaults (can be overwritten)

        if "Updates" not in configContent:
            print("No Updates Found")
            time.sleep(1)
            f.write("""Updates\nAlwaysUpdate\nTrue\nAskBeforeUpdate\nFalse\n\n""")

        if "Streaks" not in configContent:
            f.write(f"""Streaks\nTrue\n0\n{date}\n\n""")
        
        if "Alias" not in configContent:
            f.write("""Alias\nFalse\n\n""")

        if "Answers" not in configContent:
            f.write("""Answers\nScore\nFalse\nWideRange\nTrue\n\n""")

        f.close()

        try:
            exec(f"{returnLocation}()")
        except TypeError:
            home()
 
def getconf():
    try:
        with open(CONFIG_PATH, "r") as f:
            l = f.readlines()
            f.close()
            l = l[1]
            script_location = ''.join(l).strip()
            #print(script_location)
            vocab_location = script_location+"/vocab"
            #print(vocab_location)
            return script_location, vocab_location
    except Exception as e:
        print(f"Config not loaded: {e}. Please re-run with 'load' as a keyword")
        exit()
    return None, None

def reload():
    with open("config.txt", "r") as f:
        configContent = f.readlines()
        configContent = [s.rstrip() for s in configContent]
        f.close()

    updateContent = configContent.index("Answers")
    ansWideRange = bool(configContent[updateContent+3])
    #ansWideRangeActive = bool(configContent[updateContent+3])
    ansScoreActive = bool(configContent[updateContent+1])

    return configContent, ansWideRange, ansScoreActive

#################
# miscellaneous #
#################

def pront(string, t):
    string = list(string)
    for i in range(len(string)):
        print(f"{string[i]}", end='')
        time.sleep(t)
    print()

def load(lnum, speed, text="Loading"):
    for i in range(0, 100+lnum, lnum):
        print(f"{text} {i}% \r", end="")
        time.sleep(speed)
    print("\r    ", end="")
    print("")

def ran(num, vocab_list):
    r = random.randint(0, len(vocab_list)-1)
    while (r % 2) == 0:  # loop for odd
        r = random.randint(0, len(vocab_list)-1)
    return r

def ran_multi(vocab_list):
    # multi choice for french
    r = random.randint(0, len(vocab_list)-1)
    while (r % 2) != 0:  # continuous for french
        r = random.randint(0, len(vocab_list)-1)
    return r

###########
#  files  #
###########

def getfiles(choice):
   # autoupdate()
    scritpt_location, vocab_location = getconf()
    os.chdir(vocab_location)
    files = os.listdir()
    files = sorted(purefiles(files))
    
    if choice == 'all':
        return files
    else:


        #for i in range(len(files)):
            #print(f"{i+1}: {files[i]}")

        prev_prefix = None
        for i in range(len(files)):
            prefix = files[i].split('-')[0]
            if prev_prefix is not None and prefix != prev_prefix:
                print()
            print(f"{i+1}: {files[i]}")
            prev_prefix = prefix

        q = False
        chosenfiles = []


        print("\nSingle (s) or Multiple (m) files?")
        mode = input("> ")

        if mode == 's':
            try:
                selection = int(input("Select file: ")) - 1
                chosenfiles.append(files[selection])
            except:
                print("Invalid selection")
        else:
            print("\nSelect files (enter number), type 'q' when done:")
            while q == False and (len(files) > 0):
                selection = input("> ")
                if selection == 'q':
                    if len(chosenfiles) >= 1:
                        q = True
                        break
                else:
                    try:
                        selection = int(selection)
                        chosenfiles.append(files[selection-1])
                        files.remove(files[selection-1])
                        os.system("clear")
                        prev_prefix = None
                        for i in range(len(files)):
                            prefix = files[i].split('-')[0]
                            if prev_prefix is not None and prefix != prev_prefix:
                                print()
                            print(f"{i+1}: {files[i]}")
                            prev_prefix = prefix
                    except:
                        print("Invalid selection")
        return chosenfiles




def purefiles(files):
    clean_files = []
    for f in files:
        if "~" not in f and f.endswith('.txt'):
            clean_files.append(f)
    return clean_files

def merge(files):
    script_location, vocab_location = getconf()
    os.chdir(vocab_location)
    total = []
    
    for file in files:
        with open(file, "r") as f:
            l = f.readlines()
            l = [s.rstrip() for s in l]
            if len(l) > 2:
                del l[0:2]
            for x in l:
                if x.strip():
                    total.append(x)
    
    return total


#########
# Score #
#########

def incrementScore(SCORE):
    SCORE += 1
    return SCORE



###################
# Answer Widening #
###################

replacementList = [
        ["the ", ""],
        ["a ", ""],
        ["an ", ""],
        ["a ", ""],
        ["an ", ""],
        ["and ", ""],
        ["and ", ""],
        ["of ", ""],
        ["for ", ""],
        ["to ", ""],
        ["to be ", ""],
        ]

def fuzzy_widening(ansUser, ansCorrect):
    ansUser = ansUser.strip().lower()
    ansCorrect = ansCorrect.strip().lower()

    if fuzzywuzzy.fuzz.ratio(ansUser, ansCorrect) > 80:
        return True
    else:
        return False


def answer_widening(ansUser, ansCorrect):
    ansWideRange = bool(configContent[updateContent+3])

    if ansWideRange:
        ansUser = ansUser.strip().lower()
        ansCorrect = ansCorrect.strip().lower()

        for i in range(len(replacementList)):
            try:
                ansUser = ansUser.replace(replacementList[i][0], replacementList[i][1])
                ansCorrect = ansCorrect.replace(replacementList[i][0], replacementList[i][1])
            except:
                pass
            
        
        fuzzyCorrect = fuzzywuzzy.fuzz.ratio(ansUser, ansCorrect)
        

        print(f"Fuzzy correct: {fuzzyCorrect}")
        if ansUser == ansCorrect:
            return True
        elif fuzzyCorrect > 80:
            return True
        else:
            return False

    else:
        if ansUser.strip().lower() != ansCorrect.strip().lower():
            return False
        elif ansUser.strip().lower() == ansCorrect.strip().lower():
            return True
        else:
            return True


    


#################
# quizing/modes #
#################

SCORE = 0

def regular_quiz(num, vocab_list):
    SCORE = 0
    vocab_copy = vocab_list.copy()
    questions_asked = 0
    
    if num == 'max':
        num = int(len(vocab_copy)/2)
    else:
        num = int(num)
    
    print(f"\nTotal questions: {num}\n")
    
    for i in range(num):
        if len(vocab_copy) < 2:
            print("\nNo more questions available!")
            break
            
        r = ran(len(vocab_copy), vocab_copy)
        if r >= len(vocab_copy):
            r = len(vocab_copy) - 1
            if r % 2 == 0:
                r -= 1
            
        # r is odd (English), r-1 is even (French)
        print(f"Question {i+1}: Translate '{vocab_copy[r-1]}'")
        ans = input("Answer: ")
        
        #if ans.strip().lower() != vocab_copy[r].strip().lower():
        if not answer_widening(ans, vocab_copy[r]):
            print(f"Incorrect. Correct answer: {vocab_copy[r]}\n")
        else:
            print("Correct!\n")
            if ansScoreActive:
                SCORE = incrementScore(SCORE)
                print(f"Score: {SCORE}\n")
        
        #time.sleep(0.5)
    home()

def continuous_quiz(vocab_list):
    SCORE = 0
    print("Continuous Mode - Press Ctrl+C to exit\n")
    
    try:
        while True:
            vocab_copy = vocab_list.copy()
            if len(vocab_copy) < 2:
                break
                
            r = ran(len(vocab_copy), vocab_copy)
            if r >= len(vocab_copy):
                r = len(vocab_copy) - 1
                if r % 2 == 0:
                    r -= 1
                
            # r - English; r-1 - french
            # Ask french, expect English answer
            print(f"Translate '{vocab_copy[r-1]}'")
            ans = input("Answer: ")
            
#            if ans.strip().lower() != vocab_copy[r].strip().lower():
            if not answer_widening(ans, vocab_copy[r]):
                print(f"Incorrect. Correct answer: {vocab_copy[r]}\n")
            else:
                print("Correct!\n")
                if ansScoreActive:
                    SCORE = incrementScore(SCORE)
                    print(f"Score: {SCORE}\n")
            
            #time.sleep(0.3)
    except KeyboardInterrupt:
        print("\n\nQuiz ended!")
        home()

def multi_choice_quiz(vocab_list, num_questions):
    SCORE = 0
    def get_qa_pair(questions):
        # find q & a for mchoice
        r = ran_multi(questions)
        if r >= len(questions) - 1:
            r = len(questions) - 2
        
        question = questions[r]      # French 
        answer = questions[r + 1]     # English
        
        return question, answer
    
    def get_wrong_answers(questions, correct_answer):
        wrong = []
        attempts = 0
        while len(wrong) < 3 and attempts < 50:
            _, potential = get_qa_pair(questions)
            if potential != correct_answer and potential not in wrong:
                wrong.append(potential)
            attempts += 1
        return wrong
    
    def display_question(question, options, answer):
        SCORE =0
        print(f"\nWhat is the translation of '{question}'?\n")
        for i in range(len(options)):
            print(f"{i+1}) {options[i]}")
        
        try:
            guess = int(input("\n> "))
            if 1 <= guess <= len(options):
                if options[guess-1] == answer:
                    print("Correct!\n")
                    if ansScoreActive:
                        SCORE = incrementScore(SCORE)
                        print(f"Score: {SCORE}\n")
                else:
                    print(f"Incorrect. The answer was: {answer}\n")
            else:
                print(f"Invalid selection. The answer was: {answer}\n")
        except:
            print(f"Invalid input. The answer was: {answer}\n")
        
        #time.sleep(0.8)
    
    if num_questions == 'max':
        num_questions = int(len(vocab_list)/2)
    else:
        num_questions = int(num_questions)
    
    print(f"\nMultiple Choice Quiz - {num_questions} questions\n")
    
    for i in range(num_questions):
        question, answer = get_qa_pair(vocab_list)
        options = [answer]
        options.extend(get_wrong_answers(vocab_list, answer))
        random.shuffle(options)
        
        print(f"Question {i+1}/{num_questions}")
        display_question(question, options, answer)

def multi_choice_continuous(vocab_list):
    SCORE = 0
    print("Multiple Choice Continuous Mode - Press Ctrl+C to exit\n")
    
    def get_qa_pair(questions):
        r = ran_multi(questions)
        if r >= len(questions) - 1:
            r = len(questions) - 2
        
        question = questions[r]      # French 
        answer = questions[r + 1]     # English        
        return question, answer
    
    def get_wrong_answers(questions, correct_answer):
        wrong = []
        attempts = 0
        while len(wrong) < 3 and attempts < 50:
            _, potential = get_qa_pair(questions)
            if potential != correct_answer and potential not in wrong:
                wrong.append(potential)
            attempts += 1
        return wrong
    
    def display_question(question, options, answer):
        SCORE =0
        print(f"\nWhat is the translation of '{question}'?\n")
        for i in range(len(options)):
            print(f"{i+1}) {options[i]}")
        
        try:
            guess = int(input("\n> "))
            if 1 <= guess <= len(options):
                if options[guess-1] == answer:
                    print("Correct!\n")
                    if ansScoreActive:
                        SCORE = incrementScore(SCORE)
                        
                        print(f"Score: {SCORE}\n")
                else:
                    print(f"Incorrect. The answer was: {answer}\n")
            else:
                print(f"Invalid selection. The answer was: {answer}\n")
        except:
            print(f"Invalid input. The answer was: {answer}\n")
        
        #time.sleep(0.5)
    
    try:
        while True:
            question, answer = get_qa_pair(vocab_list)
            options = [answer]
            options.extend(get_wrong_answers(vocab_list, answer))
            random.shuffle(options)
            
            display_question(question, options, answer)
    except KeyboardInterrupt:
        print("\n\nQuiz ended!")


def timedQuiz(Mtime, Stime, vocab_list):
    # Time as int minutes/seconds. 
    # Set time as var clock  
    # while clockMins < time:
    import time
    SCORE = 0
   
    clockSecsStart = int(time.perf_counter())
    currentTime = int(Mtime * 60 + Stime)
   
    while int(time.perf_counter() - clockSecsStart) < currentTime:
         vocab_copy = vocab_list.copy()
         if len(vocab_copy) < 2:
             break
            
         r = ran(len(vocab_copy), vocab_copy)
         if r >= len(vocab_copy):
             r = len(vocab_copy) - 1
             if r % 2 == 0:
                 r -= 1
            
         # r - English; r-1 - french
         # Ask french, expect English answer
         print(f"Translate '{vocab_copy[r-1]}'")
         ans = input("Answer: ")
        
#         if ans.strip().lower() != vocab_copy[r].strip().lower():
         if not answer_widening(ans, vocab_copy[r]):
             print(f"Incorrect. Correct answer: {vocab_copy[r]}\n")
         else:
             print("Correct!\n")
             if ansScoreActive:
                SCORE = incrementScore(SCORE)
                
                print(f"Score: {SCORE}\n")
         remaining = currentTime - int(time.perf_counter() - clockSecsStart)
         if remaining < 0:
             remaining = 0
             break 
         print(f"Time remaining: {remaining//60}:{remaining%60} seconds")

    print("\n\nQuiz ended!")
    time.sleep(1)
    home()

       

########
# main #
########

def main(option, **kwargs):
    os.system("clear")
    #pront("Welcome to French Vocabulary Quiz", 0.05)
    
    opttype = kwargs.get("fromMenu")
    print("Test")
    

    global script_location
    global vocab_location
    script_location, vocab_location = getconf()
    #exit()
    # Get files
    files = getfiles(option)
    vocab_list = merge(files)
    
    if len(vocab_list) < 2:
        print("Error: Not enough vocabulary words loaded!")
        return
    
    print(f"\nLoaded {int(len(vocab_list)/2)} vocabulary pairs\n")
    
    # Select quiz type
    #print("Select quiz type:")
    #print("1) Traditional (type answer)")
    #print("2) Multiple choice")
    quiz_type = option
    
    # Select mode
    print("\nSelect mode:")
    print("1) Continuous")
    print("2) Set number of questions")
    print("3) Maximum (all questions)")
    print("4) Timed Quiz")
    mode = input("> ")
    
    os.system("clear")
    
    if quiz_type == "1":  # Traditional
        if mode == "1":  # Continuous
            continuous_quiz(vocab_list)
        elif mode == "3":  # Max
            regular_quiz('max', vocab_list)
        elif mode == "4":
            Mtime = int(input("Minutes: "))
            Stime = int(input("Seconds: "))
            timedQuiz(Mtime, Stime, vocab_list)
        else:  # Set number
            num = input("How many questions? ")
            regular_quiz(num, vocab_list)
            

    
    elif quiz_type == "2":  # Multiple choice
        if mode == "1":  # Continuous
            multi_choice_continuous(vocab_list)
        elif mode == "3":  # Max
            multi_choice_quiz(vocab_list, 'max')
        else:  # Set number
            num = input("How many questions? ")
            multi_choice_quiz(vocab_list, num)
    time.sleep(1)
    print("\nThank you for practicing!")

###########
# parsing #
###########

if __name__ == "__main__":

    try:
        updateContent = configContent.index("Streaks")
        streak = int(configContent[updateContent+2])
    except:
        autoconf(home)

    try:
        updateContent = configContent.index("Answers")
        ansWideRange = bool(configContent[updateContent+3])
        #ansWideRangeActive = bool(configContent[updateContent+3])
        ansScoreActive = bool(configContent[updateContent+1])
    except:
        autoconf(home)



    parser = argparse.ArgumentParser(description='French Vocabulary Quiz')
    parser.add_argument('option', help="'all' to use all files, or 'select' to choose files")
    args = parser.parse_args()
    inp = args.option
    
    if inp == 'all':
        print("Selected: ALL files")
        #time.sleep(1)
        autoupdate()
        main(inp)
    elif inp == "load":
        print("Generating...")
        autoconf(None)
        exit()
    elif inp == "update":
        print("Updating...")
        update()
        exit()
    else:
        
        #time.sleep(1)
        #autoupdate()
        if random.randint(0, 10) == 10:
            plug()
        autoconf(None)
        home()
