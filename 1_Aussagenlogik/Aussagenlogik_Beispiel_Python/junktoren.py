#!/usr/bin/python3

import string

def satz_woerter():
    """
    Takes a sentence as input and returns a list of words.
    """
    satz = input("Enter a sentence: ")        
    woerter = satz.split()
    
    while(len(woerter) != 4): # Wenn es nicht 4 woerter gibt, ist der Satz ungültig
        satz = input("Please enter a sentences in one of the following forms 'Can I <verb> <noun>' or 'Kann ich <Nomen> <Verb>': ")
        woerter = satz.split()
        
    woerter[-1] = woerter[-1].rstrip(string.punctuation) # Fragenzeichen weg!
    woerter = [x.lower() for x in woerter] # Make sure the words are all lowercase
    return woerter


def woerter_satz(woerter, en, de):
    if (en and not(de)):
        print("Yes, you can " + woerter[2] + " " + woerter[3] + ".")
    elif (de and not(en)):
        print("Ja, können Sie " + woerter[2].capitalize() + " " + woerter[3] + ".")
    else:
        print("Please try again.")


def nomen_test(wort):
    if (wort in nomen_list):
        return True
    else:
        return False


def verb_test(wort):
    if (wort in verb_list):
        return True
    else:
        return False


def welt_verb_nomen(woerter_list, verb_list, nomen_list):
    """
    Wir finden hier die index von der verb und nomen, und gebe eine Welt mit die Wahrheitswerte von v un n aus
    """
    verb_pos = 0
    nomen_pos = 0
    
    for verb in verb_list:
        if (verb in woerter_list):
            verb_pos = (woerter_list.index(verb) - 2) # Wir lassen die Position der erster 2 woerter weg (position - 2)

    for nomen in nomen_list:
        if (nomen in woerter_list):
            nomen_pos = (woerter_list.index(nomen) - 2) # Wir lassen die Position der erster 2 woerter weg (position - 2)

    if (verb_pos == 1):
        verb_pos = True
    else:
        verb_pos = False

    if (nomen_pos == 1):
        nomen_pos = True
    else:
        nomen_pos = False

    return {"V": verb_pos, "N": nomen_pos}


def negation(f):
    return not(f)


def konjunktion(f, g):
    return (f and g)


def disjunktion(f, g):
    return (f or g)


def implikation(f, g):
    if (f==True and g==False):
        return True
    else:
        return False


def bi_implikation(f, g):
    if (f == g):
        return True
    else:
        return False


def interpretations_funktion(formel, welt):
    return(formel(welt))
    