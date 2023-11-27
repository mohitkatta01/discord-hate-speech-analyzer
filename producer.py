"""
producer.py
- Listens to any message sent on the discord channel. (Check Discord documentation on how to create a discord bot on your own channel)
- If there is a message, the producer will send it to a Kafka broker via a Kafka topic.
"""

import discord
from confluent_kafka import Producer

# Discord bot token
bot_token = "ADD YOUR DISCORD BOT TOKEN"

# Kafka producer configuration
producer_config = {
    'bootstrap.servers': 'localhost:9092',  # Replace with your Kafka broker address
    'client.id': 'producer',
}

# Create a Kafka producer instance
producer = Producer(producer_config)

# Create a Discord bot instance
client = discord.Client(intents = discord.Intents.all())

# Define an event handler for when a message is received
@client.event
async def on_message(message):
    # If the message is from a bot, ignore it
    if message.author.bot:
        return

    # Send the message to Kafka
    producer.produce('test-topic', key='key', value=message.content)

# Start the Discord bot
client.run(bot_token)