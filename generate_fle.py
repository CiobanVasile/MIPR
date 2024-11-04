import pandas as pd
import random

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

answers = {
    "Cât de des ai dureri de cap?": ["Niciodată", "Ocazional", "Frecvent", "Aproape zilnic"],
    "Ai dificultăți în respirație?": ["Nu", "Doar la efort", "Ocazional", "Frecvent"],
    "Cum te simți în legătură cu starea ta emoțională?": ["Calm", "Stresat", "Anxios", "Depresiv"],
    "Ai avut probleme digestive recente?": ["Nu", "Ocazional", "Frecvent", "Sever"],
    "Cum ți-e vederea?": ["Foarte bună", "Bună", "Medie", "Slabă"],
    "Cât de des faci sport?": ["Zilnic", "Săptămânal", "Lunar", "Niciodată"],
    "Ai avut vreo accidentare recentă?": ["Nu", "O accidentare minoră", "Accidentare moderată", "Accidentare severă"],
    "Cum te simți după mese?": ["Bine", "Ușor balonat", "Foarte balonat", "Disconfort mare"],
    "Ai probleme de somn?": ["Nu", "Ocazional", "Frecvent", "Insomnie severă"],
    "Cum ți se pare tensiunea arterială?": ["Normală", "Ușor crescută", "Crescută", "Foarte crescută"]
}

symptom_specialist_map = {
    "dureri de cap": "neurolog",
    "dificultăți în respirație": "pneumolog",
    "stare emoțională": "psihiatru",
    "probleme digestive": "gastroenterolog",
    "vederea": "oftalmolog",
    "sport": "medic sportiv",
    "accidentare": "ortoped",
    "după mese": "gastroenterolog",
    "somn": "psihiatru",
    "tensiunea arterială": "cardiolog"
}

data = []
num_entries = 100000

for _ in range(num_entries):
    entry = {}
    symptoms = []

    for question in questions:
        response = random.choice(answers[question])
        entry[question] = response

        if question == "Cât de des ai dureri de cap?" and response in ["Frecvent", "Aproape zilnic"]:
            symptoms.append("dureri de cap")
        elif question == "Ai dificultăți în respirație?" and response in ["Ocazional", "Frecvent"]:
            symptoms.append("dificultăți în respirație")
        elif question == "Cum te simți în legătură cu starea ta emoțională?" and response in ["Anxios", "Depresiv"]:
            symptoms.append("stare emoțională")
        elif question == "Ai avut probleme digestive recente?" and response in ["Frecvent", "Sever"]:
            symptoms.append("probleme digestive")
        elif question == "Cum ți-e vederea?" and response == "Slabă":
            symptoms.append("vederea")
        elif question == "Cât de des faci sport?" and response == "Niciodată":
            symptoms.append("sport")
        elif question == "Ai avut vreo accidentare recentă?" and response in ["Accidentare moderată",
                                                                              "Accidentare severă"]:
            symptoms.append("accidentare")
        elif question == "Cum te simți după mese?" and response in ["Foarte balonat", "Disconfort mare"]:
            symptoms.append("după mese")
        elif question == "Ai probleme de somn?" and response in ["Frecvent", "Insomnie severă"]:
            symptoms.append("somn")
        elif question == "Cum ți se pare tensiunea arterială?" and response in ["Crescută", "Foarte crescută"]:
            symptoms.append("tensiunea arterială")

    recommended_specialists = list({symptom_specialist_map[symptom] for symptom in symptoms})
    entry["Specialist Recomandat"] = ", ".join(
        recommended_specialists) if recommended_specialists else "medic generalist"

    data.append(entry)

df = pd.DataFrame(data)
df.to_csv("digital_triage_data.csv", index=False, encoding="utf-8")
print("Setul de date a fost generat și salvat în 'digital_triage_data.csv'.")
