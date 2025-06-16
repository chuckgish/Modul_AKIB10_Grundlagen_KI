import torch

# Settings
DIM = 10000  # high dimensionality
device = "cuda" if torch.cuda.is_available() else "cpu"

# Helper: create random bipolar vector (+1/-1)
def random_bipolar(dim):
    return torch.where(torch.rand(dim, device=device) > 0.5, 1, -1)

# Bind (element-wise multiply)
def bind(a, b):
    return a * b

# Bundle (sum and bipolarize)
def bundle(vectors):
    s = torch.sum(torch.stack(vectors), dim=0)
    return torch.where(s >= 0, 1, -1)

# Cosine similarity for classification
def similarity(a, b):
    a = a.float()
    b = b.float()
    return torch.dot(a, b) / (torch.norm(a) * torch.norm(b))

# Define categories and attributes (in German)
categories = ["Wein", "Bier", "Limonade"]
attributes = {
    "Farbe": ["rot", "gelb", "klar", "braun", "grün"],
    "Geschmack": ["süß", "bitter", "herb", "sauer", "fruchtig"],
    "Alkoholgehalt": ["alkoholfrei", "niedrig", "hoch"],
    "Temperatur": ["kalt", "warm"]
}

# Create random vectors for attribute values and categories
attr_vectors = {}
for attr, vals in attributes.items():
    attr_vectors[attr] = {val: random_bipolar(DIM) for val in vals}
cat_vectors = {cat: random_bipolar(DIM) for cat in categories}

# Create prototype vectors by binding category with attributes and bundling
prototypes = {}

# Beispiel für jede Kategorie (kann beliebig erweitert werden)
prototypes_data = {
    "Wein": [("Farbe", "rot"), ("Geschmack", "herb"), ("Alkoholgehalt", "hoch"), ("Temperatur", "warm")],
    "Bier": [("Farbe", "braun"), ("Geschmack", "bitter"), ("Alkoholgehalt", "niedrig"), ("Temperatur", "kalt")],
    "Limonade": [("Farbe", "klar"), ("Geschmack", "süß"), ("Alkoholgehalt", "alkoholfrei"), ("Temperatur", "kalt")]
}

for cat in prototypes_data:
    bound_vectors = []
    for attr, val in prototypes_data[cat]:
        bound_vectors.append(bind(cat_vectors[cat], attr_vectors[attr][val]))
    prototypes[cat] = bundle(bound_vectors)

# Classification function for a new drink (given attribute values)
def classify(drink_attrs):
    # Bind category vector with attribute vectors and bundle
    # Here, we don’t know category, so we bind attribute vectors only
    bound_vectors = []
    for attr, val in drink_attrs.items():
        bound_vectors.append(attr_vectors[attr][val])
    query = bundle(bound_vectors)

    # Find category with max similarity
    sims = {cat: similarity(query, prototypes[cat]) for cat in categories}
    return max(sims, key=sims.get), sims

# Neue unbekannte Getränke (Kombinationen, die nicht exakt den Prototypen entsprechen)
test_drinks = [
    {"Farbe": "grün", "Geschmack": "fruchtig", "Alkoholgehalt": "alkoholfrei", "Temperatur": "kalt"},  # wahrscheinlich Limonade
    {"Farbe": "braun", "Geschmack": "bitter", "Alkoholgehalt": "hoch", "Temperatur": "kalt"},        # Mischtyp Bier/Wein
    {"Farbe": "rot", "Geschmack": "sauer", "Alkoholgehalt": "alkoholfrei", "Temperatur": "warm"},    # ungewöhnlich, evtl. keine klare Zuordnung
]

for drink in test_drinks:
    predicted, sims = classify(drink)
    print(f"Getestetes Getränk: {drink}")
    print(f"Vorhergesagte Kategorie: {predicted}")
    for cat, sim in sims.items():
        print(f"  {cat}: {sim:.4f}")
    print()