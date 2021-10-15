import discord 
import os
import random
from quotelist import quotes
from questionlist import questions

client = discord.Client()

TOKEN = input(token here please: )

quotes()
questions()

@client.event
async def on_ready():
  print('Time for {0.user}'.format(client))
  await client.change_presence(activity=discord.Game(name='Existentialism 2.0'))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('hi'):
    await message.channel.send('hello there')

  if message.content.startswith('*quote'):
    n = random.randint(0,len(L))
    await message.channel.send(L[n]) 

  if message.content.startswith('*daily quote'):
   n = random.randint(0,len(L))
   await message.channel.send(L[n])
   r = random.randint (0,len(R))
   await message.channel.send(R[r])
   await message.channel.send('<@&839612636983197716>')
     


client.run(os.getenv('TOKEN'))
