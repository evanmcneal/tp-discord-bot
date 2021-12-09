import discord
import os
import requests
import json
import time
import random
from replit import db
from keep_alive import keep_alive


client = discord.Client()

angry_stuff = [
  "Fuck You!",
  "I cant believe you said that!.",
  "Delete this right now!",
  "You fucking Ginger Bitch!",
  "You should have been a blowjob!",
  "Fucking Nerd...",
  "I sure do hate knowing you were conceived",
  "Uh Oh, I smell a bitch",
  "t(-_-t)"
]

nice_stuff = [
  "You are so pretty!",
  "I am glad that bitch Tyler Pate didn't send that or I'd be really pissed. Fucking swine.",
  "I really love that you message in this discord. You are amazing",
  "Hey, it's you again, nice!",
  "*whistles in sexy*",
  "DAYYYUMMM, you fine as hell",
  "My savior!",
  "**NICE COCK!**"
]

dad_stuff = [
  "Can we play catch father?",
  "How many years does it take to go to the grocery for milk???? :(",
  "Are we there yet??",
  "Father, change me!",
  "Why do you love your other family more than me!!!???"
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

@client.event
async def on_ready():
  print('I have logged in as {0.user}'.format(client))
  await client.change_presence(status=discord.Status.invisible)

@client.event
async def on_voice_state_update(member, before,after):
  channel = await client.fetch_channel(644300965117165589)
  if db["responding"]:
    if before.channel == None:
      if member.id == (263405587704971264) or member.id == (264505493656043520):
        await channel.send("Welcome to the voice chat " + member.name + "! You are so amazing!!!")
      if member.id == (293904621821231104) or member.id == (390261906058772480):
        await channel.send("Here we go, some idiot name "+  member.name +" joined the voice chat...")
    else:
      print("Didn't join.")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  if db["responding"]:
    if message.author.id == (263405587704971264) or message.author.id == (264505493656043520):
      options = nice_stuff
      time.sleep(2)
      await message.channel.send(random.choice(options))

    if message.author.id == (293904621821231104):
      options = angry_stuff
      time.sleep(2)
      await message.channel.send(random.choice(options))

    if message.author.id == (390261906058772480):
      options = dad_stuff
      time.sleep(2)
      await message.channel.send(random.choice(options))
    
    if message.author.id == (264554889726656513):
      time.sleep(2)
      await message.channel.send("Slow ya roll Cammy Poo")

  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

keep_alive()
client.run(os.getenv('TOKEN'))