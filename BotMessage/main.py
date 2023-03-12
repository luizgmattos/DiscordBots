import discord
import os
import requests
import json

TOKEN = 'OTQ2NDg2NzMxMTExMjkyOTY4.YhfadQ.KqvEgC4RQUG_zkgT2uYOHfchXWg'

client = discord.Client()

## Loggin up with bot on server
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


## Fuction for grabbing the quote
def get_quote():
    response = requests.get("https://zenquotes.io/api/quotes/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote

## Creating answer log for bot on server
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    
    if message.channel.name == 'chat_teste':

        ## Answering normal messages
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        if user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        if user_message.lower() == '!random':
            await message.channel.send(f'{username} is random!')
            return       
        if user_message.lower() == '$play':
            await message.channel.send(f'{username} I cant play music!')
            return    

        ## Answering with internet messages
        if user_message.lower() == '$inspire':
            quote = get_quote()
            await message.channel.send(f'{username}, ' + quote)
            return


client.run(TOKEN)