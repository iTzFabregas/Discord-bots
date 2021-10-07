import discord
import random

#PUT YOUR BOT TOKEN HERE
#TOKEN = 'YOUR-BOT-TOKEN'
TOKEN = 'ODk1NDgzNTI5MzczMzE5MTg5.YV5OBg.Z4NuyfrDhuPOBHLARrYgMhtfhzY'

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

        for name in members:
            if(name == nome):
                await message.channel.send('There is already this name!')
                return

        members.append(nome)
        arqout = open('members.txt', 'w')
        arqout.writelines(members)
        arqout.close()

        await message.channel.send('New name added!')
        print(members)
        return
    

    if user_message.startswith('!delname'):
        nome = str(user_message).split(' ')[1]
        nome += '\n'
        flag = 0
        cnt = 0
        for name in members:
            if(name == nome):
                flag = 1
                break
            cnt+=1

        if(flag == 0):
            await message.channel.send('There is no member with this name!')
            return

        del members[cnt]
        arqout = open('members.txt', 'w')
        arqout.writelines(members)
        arqout.close()
        print(members)
        await message.channel.send('The name has been deleted!')
        return


    if user_message.startswith('!listname'):
        for name in members:
            output = str(name).strip('\n')
            await message.channel.send(output)
        return


    if user_message == '!match':
        name0 = random.choice(members)
        name1 = random.choice(members)
        while name0 == name1:
            name1 = random.choice(members)
        
        namo0 = name0.strip('\n')
        namo1 = name1.strip('\n')
        await message.channel.send(f'\>>> {namo0} <<< MATCH >>> {namo1} <<<')
        return

client.run(TOKEN)
