from transformers import pipeline

emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=False
)

def detect_emotion(text):
    result = emotion_classifier(text)[0]
    label = result['label']
    score = result['score']
    return label, score
