import spacy
import random

nlp = spacy.load("ro_core_news_sm")

questions = [
    "Cât de des ai dureri de cap?",
    "Ai dificultăți în respirație?",
    "Cum te simți în legătură cu starea ta emoțională?",
    "Ai avut probleme digestive recente?",
    "Cum ți-e vederea?",
    "Cât de des faci sport?",
    "Ai avut vreo accidentare recentă?",
    "Cum te simți după mese?",
    "Ai probleme de somn?",
    "Cum ți se pare tensiunea arterială?"
]

medici_scores = {
    "medic generalist": 0,
    "psihiatru": 0,
    "cardiolog": 0,
    "gastroenterolog": 0,
}

def procesare_raspuns(raspuns):
    doc = nlp(raspuns.lower())

    for ent in doc.ents:
        if ent.label_ in ["EMOTIE", "STRES", "ANXIETATE", "DEPRESIE"]:
            medici_scores["psihiatru"] += 1
        elif ent.label_ in ["DIGESTIE", "STOMAC", "BALONARE"]:
            medici_scores["gastroenterolog"] += 1
        elif ent.label_ in ["RESPIRATIE", "INIMA", "TENSIUNE"]:
            medici_scores["cardiolog"] += 1
        else:
            medici_scores["medic generalist"] += 1

for question in questions:
    print(question)
    raspuns = input("Scrie răspunsul tău: ")

    procesare_raspuns(raspuns)

medici_disponibili = list(medici_scores.keys())

medicul_random = random.choice(medici_disponibili)

print(f"\nPe baza răspunsurilor tale, medicul ales este: {medicul_random}.")
