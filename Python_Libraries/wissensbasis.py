#!/usr/bin/python3

# Define a simple class for logical expressions
class AtomareFormel:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class Negation:
    def __init__(self, ausdruck):
        self.ausdruck = ausdruck

    def __repr__(self):
        return f"¬{self.ausdruck}"

class Konjunktion:
    def __init__(self, *args):
        self.args = args

    def __repr__(self):
        return f"({' ∧ '.join(map(str, self.args))})"

class Disjunktion:
    def __init__(self, *args):
        self.args = args

    def __repr__(self):
        return f"({' ∨ '.join(map(str, self.args))})"

class Implikation:
    def __init__(self, voraussetzung, folge):
        self.voraussetzung = voraussetzung
        self.folge = folge

    def __repr__(self):
        return f"({self.voraussetzung} → {self.folge})"

# Function to create a propositional logic knowledge base
def erstelle_wissensbasis():
    # Erstellen atomare Formeln
    P = AtomareFormel("P")  #Beispiel: "Es regnet"
    Q = AtomareFormel("Q")  #Beispiel: "Ich nehme einen Regenschirm mit"
    R = AtomareFormel("R")  #Beispiel: "Der Boden ist nass"

    # Definieren Sie Ihre logischen Regeln (Formeln)
    wissensbasis = [
        Implikation(P, Q),  # Wenn es regnet, dann nehme ich einen Regenschirm mit
        Implikation(Q, R),  # Wenn es regnet, dann ist der Boden nass
        Negation(P)           # Es regnet nicht
    ]
    
    return wissensbasis

# Function to apply Modus Ponens
def wende_modus_ponens_an(wb, bekannte_fakten):
    abgeleitete_fakten = set(str(fact) for fact in bekannte_fakten)  # Store string representations of facts
    geaendert = True
    while geaendert:
        geaendert = False
        for regel in wb:
            if isinstance(regel, Implikation) and str(regel.voraussetzung) in abgeleitete_fakten:
                if str(regel.folge) not in abgeleitete_fakten:
                    print(f"Modus Ponens ausgeführt: {regel.voraussetzung} → {regel.folge}")
                    abgeleitete_fakten.add(str(regel.folge))
                    geaendert = True
    return abgeleitete_fakten
