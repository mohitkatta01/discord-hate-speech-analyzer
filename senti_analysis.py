"""
senti_analysis.py
- The brains of the entire code function, this is where the model lives.
- The predict_sentiment(sentence) function will be called in the consumer.py file which sends the message.

This code is from : https://huggingface.co/ctoraman/hate-speech-bert
"""


from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

pipe = pipeline("text-classification", model="ctoraman/hate-speech-bert")

tokenizer = AutoTokenizer.from_pretrained("ctoraman/hate-speech-bert")
model = AutoModelForSequenceClassification.from_pretrained("ctoraman/hate-speech-bert")

# "0": Neutral
# "1": Offensive
# "2": Hate

def predict_sentiment(sentence):
    inputs = tokenizer(sentence, return_tensors="pt")
    outputs = model(**inputs)
    predicted = pipe(sentence)[0]['label']
    return predicted
