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
      channel = client.get_channel('channel_id')
      await channel.send(f'>>>>>> {after.name} IS ONLINE! <<<<<<')
    elif str(after.status) == 'offline':
      channel = client.get_channel('channel_id')
      await channel.send(f'\>\>\> {after.name} IS OFFLINE! <<<')


@client.event
async def on_message(message):
    user_message = str(message.content)

    if message.author == client.user:  
      return
    
    if user_message.startswith('!status'):
      await message.channel.send('(Bot) Online...')
    return 

client.run('BOT_TOKEN')
