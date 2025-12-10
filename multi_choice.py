
                #######################################
                #                                     #
                # Multiple Choice Question Framework  #
                #                                     #
                #######################################

# french/english question to set i for answers or questions [ even-1 = french | even = english ]
# set as an extra option in vocab quiz, with ID as `mult`
# assumes vocab already sanitised and ready
# necessary functions:
# - random for question; gen even and if q for french then -1
# - find answer as even english/e-1 french
# - find incorrect options
# - randomise order of options
# - correct and incorrect answer handling
# - os clear & next question

import random
import time
import os

questions = ['accueillir', 'to welcome', "l'actualité (f)", 'the news', 'assister à', 'to take part in', "l'avant-première (f)", 'preview', 'avoir pour but', 'to intend to', 'au cœur de', 'in the heart of', 'dépasser', 'to exceed', 'le dérivé', 'by product', 'durable', 'lasting', 'échouer', 'to fail', 'exposer', 'to exhibit', 'de plusierus façons (fpl)', 'in several ways', 'frappant(e)', 'striking', 'la garantie', 'guarantee', 'garantir', 'to guarantee', 'gonfler les rangs', 'to swell the ranks', 'intégré', 'integrated', "l'intérêt (m) commun", 'common interest', 'la/la lauréat(e)', 'prize winner', 'lors de', 'at the time', 'manquer de moyens', 'to lack the means', 'de même', 'likewise', 'le moment clef', 'key moment', 'la moyenne annuelle', 'yearly average', 'de multiples manières', 'in many ways', "l'offre (f) privilège", 'exclusive offer', 'pédagogique', 'educational', 'se poser la question', 'to ask oneself the question', 'posséder', 'to possess', 'prendre en charge', 'to take charge of', 'remettre en question', 'to question', 'la rencontre', 'meeting', 'se rendre à', 'to go to', 'restaurer', 'to restore', 'réunir', 'to bring together', 'la salle de projection', 'prejection room', 'la série télévisée', 'television series', 'la soirée thématique', 'themed evening', 'sous 15 jours', 'within a fortnight', 'le tapis rouge', 'red carpet', 'touch-à-tout', 'jack of all trades', 'le trophée', 'trophy', 'la valeur', 'value', 'attendu', 'expected', "l'applaudissement (m)", 'applause', "l'avancement (m) technologique", 'technological advancement', 'le cinéaste', 'film maker', 'le/la comédien(-ienne)', 'actor', 'concevoir', 'to conceive', 'le court-métrage', 'short film', 'décevant', 'dissapointing', 'déclencher', 'to set in motion', 'la durée', 'duration', "l'écran (m) plat", 'flat screen', 'en permanence', 'permanently', "l'exposition (f)", 'exhibition', 'le long-métrage', 'feature length film', 'mériter', 'to be worth', 'le mode de règlement', 'means of payment', 'le monopole', 'monopoly', 'le montage', 'editing', 'en noir et blanc', 'in black and white', 'nuire à', 'to be harmful to', 'la projection', 'projection', 'projeter', 'to project', 'proposer', 'to propose', 'la renaissance', 'rebirth', 'restreint', 'limited', 'le tournage', 'filming', 'à travers le monde', 'throughout the world', 'la version du réalisateur', "director's cut", 'vieux jeu', 'old fashioned']
lang = 0 # 0/1 where 0 is french
question = 0 # question index number

def franglais():
    #l = input("French (f) or English (e) questions?")
    #if l == 'f':
    #    lang = 0
    #else:
    lang = 1
    return lang
            

def qanswer(questions, question):
    if int(questions.index(question)) % 2 == 0:# question index
        # is even ∴ english and answe -= 1
        return False
    else:
        # is odd ∴ french and answer += 1
        return True

def bqanswer(num):
    if int(num) % 2 == 0:# question index
        # is even ∴ english and answe -= 1
        return False
    else:
        # is odd ∴ french and answer += 1
        return True

def randar(questions, lang):
    #print(len(questions))
    if lang == 0: # if french questions:
        target = False
        num = random.randint(0, (len(questions)))
    else:
        target = True
        num = random.randint(0, len(questions))
        
    while bqanswer(num) != target: # whilst num is not desired
        num = random.randint(0, len(questions))
    #print(num)
    return num
    
def qa(questions):
    num = randar(questions, lang)
    question = questions[num]
    #print(question)
    if qanswer(questions, question) == True:
        answer = questions[num-1]
    else:
        answer = questions[num]
    return question, answer

def misinformation(questions, ansptions):
    for i in range(3):
        time.sleep(0.001)
        x, misnaswer = qa(questions)
        
        ansptions.append(misnaswer)
    return ansptions

def display(question ,options, answer):
    print("What is the translation of", question+"?\n")
    for i in range(len(options)):
        print(f"{i+1}) {options[i]}")
    guess = int(input("\n> \r"))
    if options[guess-1] == answer:
        print("Correct")
        time.sleep(0.4)
    else:
        print(f"Incorrect, the answer was {answer}")
        time.sleep(0.4)
    os.system("clear")

lang = franglais()
while True:
    question, answer = qa(questions)
    ansptions = []
    ansptions.append(answer)
    ansptions = misinformation(questions, ansptions)
    #print(ansptions)
    random.shuffle(ansptions)
    #print(ansptions)
    
    display(question, ansptions, answer)




















