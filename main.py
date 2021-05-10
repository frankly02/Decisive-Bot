import os
import discord
import random
from replit import db
from run import keep_running

client = discord.Client()

if not "games" in db.keys():
  db["games"] = []

def add_game(game):
  games = db["games"]
  if game in games:
    return 0
  else:
    games.append(game)
    db["games"] = games
    return 1

def remove_game(game):
  games = db["games"]
  if game in games:
    new_games = []
    for x in games:
      if x != game:
        new_games.append(x)
    db["games"] = new_games
    return 1
  else:
    return 0

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  content = message.content
  
  if content.startswith(']add'):
    game = content.split(']add ', 1)[1]
    i = add_game(game)
    if i == 0:
      await message.channel.send('game already there')
    else:
      await message.channel.send('success')
  
  if content.startswith(']del'):
    game = content.split(']del ', 1)[1]
    i = remove_game(game)
    if i == 0:
      await message.channel.send('game not found')
    else:
      await message.channel.send('success')

  if content.startswith(']play'):
    games = db["games"]
    await message.channel.send('@here' + random.choice(games))

keep_running()
client.run(os.environ['token'])
