"""
consumer.py
- listens to the data transmitted by the producer via the subscribed topic
- Send the message to the hate speech analyzer
- Receives the sentiment, send it along with the message to the frontend, where it is called.
"""

from confluent_kafka import Consumer, KafkaError
import senti_analysis
import streamlit as st

def process_kafka_messages():
    # Kafka consumer configuration
    consumer_config = {
        'bootstrap.servers': 'localhost:9092',  # Replace with your Kafka broker address
        'group.id': 'my-group',
        'auto.offset.reset': 'earliest'
    }

    # Create a Kafka consumer instance
    consumer = Consumer(consumer_config)

    # Subscribe to the topic
    consumer.subscribe(['test-topic'])

    # Poll for new messages
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print('Error: {}'.format(msg.error()))
                break

        sentiment = senti_analysis.predict_sentiment(msg.value().decode('utf-8'))
        print('Received message: {}'.format(msg.value()))
        st.metric("Message", msg.value().decode())
        if(sentiment == "LABEL_0"):
            print('Neutral')
            st.write('Neutral')
        elif(sentiment == "LABEL_1"):
            print('Offensive')
            st.write('Offensive')
        elif(sentiment == "LABEL_2"):
            print('Hate')
            st.write('Hate')
        else:
            print('Unknown')
            st.write('Oops! Unknown')

    # Close the consumer
    consumer.close()

if __name__ == "__main__":
    process_kafka_messages()