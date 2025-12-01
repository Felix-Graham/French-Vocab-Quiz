import os
import argparse
import time
import random



def main(files):
    load(10, 0.1)
    files = getfiles(files)
    total = merge(files)
    #print(total)
    tmpfile(total)
    os.chdir("/home/rhemus/french/scipts/")
    os.system("python3 vocab_quiz.py tmp.txt")
    pass




def load(lnum, speed):
    for i in range(0, 100+lnum, lnum):
        print(f"{i}% \r", end="")
        time.sleep(speed)
    print("\r    ", end="")
    print("")
        


def getfiles(choice):
    os.chdir("/home/rhemus/french/vocab/")
    files = os.listdir()
    files = purefiles(files)
    if choice == 'all':
        print("Sorry, this area is still under construcion...")
        exit()
        quit()
        return files
    else:
        for i in range(len(files)):
            print(f"{i+1}: {files[i]}")
        q = False
        chosenfiles = []
        while q == False and (len(files) > 0):
            selection = input("> \r")
            if selection == 'q':
                if len(chosenfiles) > 1:
                    q == True
                    break
                else:
                    print("Illegal move, you must select at least 2 files")
                    pass
            else:
                selection = int(selection)
                chosenfiles.append(files[selection-1])
                files.remove(files[selection-1])
                os.system("clear")
                for i in range(len(files)):
                    print(f"{i+1}: {files[i]}")
        print(chosenfiles) #proof that above selection works
        return chosenfiles


    

def purefiles(files):
    for i in range(0, 3):
        for i in range(len(files)):
            try:
                print(i)
                if "~" in files[i]:
                    print(f"Removed {files[i]}")
                    a.remove(files[i])
                    time.sleep(0.01)
                else:
                    print(f"Allowed {files[i]}")
                    time.sleep(0.01)
            except:
                break
        os.system("clear")
    return files
    


def merge(files):
    os.chdir("/home/rhemus/french/vocab/")
    total = []
    if len(files) > 1:
        for i in range(len(files)):
            f = files[i]
            print(i)
            print(f)
            with open(f, "r") as f:
                l = f.readlines() # in form ['', '']
                l = [s.rstrip() for s in l]
                del l[0:2]
                for x in l:
                    total.append(x)

                f.close()
    else:
        f = str(files).rstrip()
        with open(f, "r") as f:
            l = f.readlines()
            l = [s.rstrip() for s in l]
            del l[0:2]
            for x in l:
                total.append(x)

            
    print(total)
    return total



def tmpfile(total):
    with open("tmp.txt", "w") as f:
        f.write("Merged vocab \n\n")
        for i in total:
            w = (str(i).rstrip())+ "\n"
            f.write(w)
        f.close()
    pass



parser = argparse.ArgumentParser(description='French Vocabulary Quiz')
parser.add_argument('option', help='all or select')
args = parser.parse_args()
inp = args.option
print(inp)
if inp == 'all':
    print("Selected: 'ALL'")
    time.sleep(1)
    main(inp)
else:
    print("Selected: SELECT")
    time.sleep(1)
    main(inp)
