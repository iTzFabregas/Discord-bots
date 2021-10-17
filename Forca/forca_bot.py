import requests
import json
import discord

client = discord.Client()

divided_word = []
divided_player_word = []
player_word = ''
is_the_game_running = 0
total_lifes = 5
right_letters = 0
num_letters = 0
word = ''

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='voce pelado >:)'))
    print('ONLINE: {0.user}\n'.format(client))

@client.event
async def on_message(message):
    # username = str(message.author).split('#')[0]
    user_message = str(message.content)
    # channel = str(message.channel.name)

    global divided_word 
    global divided_player_word    
    global player_word
    global num_letters
    global right_letters
    global total_lifes
    global is_the_game_running
    global word

    if message.author == client.user:
        return
    
    if user_message.startswith('!status'):
        await message.channel.send('(Forca) Ainda to rodando no replit...')

    if(user_message.startswith('!start')):
        while True:
            response_word = requests.get('https://random-word-api.herokuapp.com/word?number=1')
            word = response_word.json()[0]
            response_tip = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
            print(response_tip.status_code)
            if response_tip.status_code == 200:
                break

        tip = response_tip.json()
        tip_definition = tip[0]['meanings'][0]["definitions"][0]['definition']

        num_letters = len(word)
        divided_player_word = ["-"] * num_letters
        for i in word:
            divided_word.append(i)
            player_word = player_word + '\_\_   '

        # await message.channel.send('\nDEFINITION: ' + tip_definition)
        # await message.channel.send(word)
        print(word)
        print(player_word)
        await message.channel.send(player_word)

        is_the_game_running = 1
        await message.channel.send('\nTO PLAY TYPE: \"!play <lower letter>\"')
        return

    elif user_message.startswith('!play'):

        inletter = str(user_message).split(' ')[1]
        if is_the_game_running == 1:
            flag = 0
            while True:
                if inletter in divided_word:
                    index = divided_word.index(inletter)
                    divided_player_word[index] = inletter
                    divided_word[index] = '-'
                    flag = 1
                    right_letters += 1
                else:
                    break

            if flag == 0:
                total_lifes -= 1
                await message.channel.send(f"YOU STILL HAVE {total_lifes} LIFE(S)!")
            else:
              player_word = ""
              for i in divided_player_word:
                  if i == '-':
                      player_word += '\_\_   '
                      continue
                  player_word += i.upper() + '  '
              await message.channel.send(player_word)
            the_game_is_over = 0
            if total_lifes <= 0:
              await message.channel.send("CONGRATULATIONS!!! YOU LOSE :)")
              await message.channel.send(f"The word was {word}")
              the_game_is_over = 1

            elif right_letters == num_letters:
              await message.channel.send(f"CONGRATULATIONS!!! YOU WIN WITH {total_lifes} LIFE(S)")
              the_game_is_over = 1
          
            if the_game_is_over == 1:
              divided_word = []
              divided_player_word = []
              player_word = ''
              is_the_game_running = 0
              total_lifes = 5
              right_letters = 0
              num_letters = 0
              word = ''
              return
        else:
            await message.channel.send('THERE IS NO GAME RUNNING AT THE MOMENT!')
            await message.channel.send('START A NEW GAME TYPING \"!start\"')

        return

client.run('YOUR-BOT-TOKEN')
