## A Real-Time hate speech analyzer on Discord channels
A simple implementation of a real-time hate speech analyzer on Discord servers using Apache Kafka, HuggingFace and Streamlit. 

## What does this project do?
This is a very simple implementation of a Hate speech analyzer which takes messages from any Discord channel and analyzes the text fir hate/offensive speech, in real-time and with low latency.

A HuggingFace pre trained ML model is used to identify hate or offensive speech. A kafka producer will be sending all the data to a kafka cluster; any kafka consumer subscribed to a particular topic within the Kafka broker network will be listening to all the data transmitted.

As and when the data is transmitted, it will be sent to the ML model which will return whether the message contains hate/offensive speech.

After that, the message along with the sentiment will be displayed on the frontend in real time, with negligible latency, making it a perfect choice for transmitting huge amounts of data where time is of the essence.

### Why Apache Kafka?
With the addition of Apache Kafka between the message delivery and the Frontend, we can perform many operations asyncronously which allows for a faster delivery of content.

Apache Kafka is does not have a persistent disk; although it has fault-tolerant servers which makes sure no data gets lost even if a broker (kafka server) goes down. It can be deployed on the cloud such as AWS and can be connected to a proper database such as AWS S3 or a data warehousing tool such as Amazon Redshift. 

Apache Kafka is currently maintained by the Apache Software foundation as an open sourced software.

The link to my medium article to learn more about the code and basics of Apache Kafka: *[Medium article](https://medium.com/@mohit-katta/apache-kafka-real-time-hate-speech-analysis-on-discord-servers-ca052ea75e5c)*
