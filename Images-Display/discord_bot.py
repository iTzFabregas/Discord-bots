import discord
import random

#PUT YOUR BOT TOKEN HERE
TOKEN = 'YOUR-BOT-TOKEN'

client = discord.Client()

arqima = open('images.txt', 'r')
arqcom = open('commands.txt', 'r')
images = arqima.readlines()
commands = arqcom.readlines()
arqima.close()
arqcom.close()

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


    if user_message.startswith('!addimage'):
        enter = str(user_message).split(' ')
        command = '!' + enter[1] + '\n'

        for comms in commands:
            if(comms == command):
                await message.channel.send('There is already an image with this command!')
                return

        image = enter[2] + '\n'
        commands.append(command)
        images.append(image)

        arqima = open('images.txt', 'w')
        arqcom = open('commands.txt', 'w')
        arqima.writelines(images)
        arqcom.writelines(commands)
        arqima.close()
        arqcom.close()

        await message.channel.send('The image has been added!')
        print(commands)
        print(images)
        return


    if user_message.startswith('!delimage'):
        enter = str(user_message).split(' ')
        command = '!' + enter[1] + '\n'

        cnt = 0
        flag = 0
        for comms in commands:
            if(comms == command):
                flag = 1
                break
            cnt+=1

        if flag == 0:
            await message.channel.send('There is no image with this command!')
            return

        del commands[cnt]
        del images[cnt]

        print(images)
        print(commands)

        arqima = open('images.txt', 'w')
        arqcom = open('commands.txt', 'w')
        arqima.writelines(images)
        arqcom.writelines(commands)
        arqima.close()
        arqcom.close()
        await message.channel.send('The image has been deleted!')
        return

    if (user_message + '\n') in commands:
        cnt = 0
        while commands[cnt] != (user_message + '\n'):
            cnt+=1
        await message.channel.send(images[cnt])
        return


    if (user_message.startswith('!listimages')):
        for comms in commands:
            output = str(comms).strip('\n')
            await message.channel.send(output)
    return

client.run(TOKEN)