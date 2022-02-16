import discord
intents = discord.Intents.default()
intents.presences = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('ONLINE: {0.user}\n'.format(client))
    return


@client.event
async def on_member_update(before, after):
  print(f'{after.name} is now {after.status}')
  if str(after.name) == 'member_name':
    if str(after.status) != 'offline':
      channel = client.get_channel(943303600854167552)
      await channel.send(f'>>>>>> {after.name} ESTÁ ONLINE! <<<<<<')
    elif str(after.status) == 'offline':
      channel = client.get_channel(943303600854167552)
      await channel.send('https://tenor.com/view/sad-cry-crying-tears-broken-gif-15062040')
      await channel.send(f'\>\>\> {after.name} SE DESCONECTOU! <<<')


@client.event
async def on_message(message):
    user_message = str(message.content)

    if message.author == client.user:  
      return
    
    if user_message.startswith('!status'):
      await message.channel.send('(Bot) Ainda to rodando no vscode...')
    return 

client.run('BOT_TOKEN')
