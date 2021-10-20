import requests
import json
import discord

TOKEN = 'YOUR-BOT-TOKEN'
client = discord.Client()

url = 'http://api.giphy.com/v1/gifs/random'

@client.event
async def on_ready():
    print('ONLINE!!!\n')

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    if client.user == message.author:
        return
    
    elif user_message.startswith('!gif'):

        gif_name = str(user_message).split(' ')[1]

        params = {'api_key': 'YOUR-GIPHY-API-KEY', 'tag': gif_name, 'rating': 'r'}
        response = requests.get(url, params=params)
        giphy = response.json()
        url_giphy = giphy['data']['embed_url']
        if response.status_code != 200:
            await message.channel.send(response.status_code)    
        else:
            await message.channel.send(url_giphy)
        return
    

client.run(TOKEN)
