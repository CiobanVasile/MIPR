import spacy
import joblib

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

classifier = joblib.load('trained_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def get_user_responses():
    responses = []
    print("Răspundeți la următoarele întrebări despre simptomele dvs.:")
    for question in questions:
        answer = input(question + " ")
        responses.append(answer)
    return " ".join(responses)

def recommend_specialist_from_responses():
    user_responses = get_user_responses()

    doc = nlp(user_responses)
    extracted_symptoms = [ent.text for ent in doc.ents if ent.label_ == "SYMPTOM"]

    if extracted_symptoms:
        symptoms_text = " ".join(extracted_symptoms)
    else:
        print("Nu s-au identificat simptome specifice. Se vor folosi toate răspunsurile introduse pentru analiză.")
        symptoms_text = user_responses

    symptoms_vector = vectorizer.transform([symptoms_text])

    specialist_recommendation = classifier.predict(symptoms_vector)[0]
    return specialist_recommendation

recommended_specialist = recommend_specialist_from_responses()
if recommended_specialist:
    print(f"Specialist recomandat: {recommended_specialist}")
