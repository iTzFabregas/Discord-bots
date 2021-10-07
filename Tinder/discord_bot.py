import discord
import random

TOKEN = 'YOUR-BOT-TOKEN'

client = discord.Client()

arqin = open('members.txt', 'r')
members = arqin.readlines()
arqin.close()


@client.event
async def on_ready():
    print('ONLINE: {0.user}\n'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    if message.author == client.user:
        return  

    if user_message.startswith('!addname'):
        nome = str(user_message).split(' ')[1]
        nome += '\n'
        members.append(nome)
        arqout = open('members.txt', 'w')
        arqout.writelines(members)
        arqout.close()

        await message.channel.send('New name added!')
        print(members)
        return
    
    if user_message == '!match':
        name0 = random.choice(members)
        name1 = random.choice(members)
        while name0 == name1:
            name1 = random.choice(members)
        
        namo0 = name0.strip('\n')
        namo1 = name1.strip('\n')
        await message.channel.send(f'\>>> {namo0} <<< MATCH >>> {namo1} <<<')


client.run(TOKEN)
