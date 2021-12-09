import discord
import os
import requests
import json
import random
from replit import db

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

angry_stuff = [
  "Fuck You!",
  "I cant believe you said that!.",
  "Delete this right now!",
  "You fucking Ginger Bitch!",
  "You should have been a blowjob!"
]

nice_stuff = [
  "You are so pretty!",
  "I am glad that bitch Tyler Pate didn't send that or I'd be really pissed. Fucking swine.",
  "I really love that you message in this discord. You are amazing",
  "Hey, it's you again, nice!",
  "*whistles in sexy*"
]

dad_stuff = [
  "Can we play catch father?",
  "How many years does it take to go to the grocery for milk???? :(",
  "Are we there yet??",
  "Father, change me!"
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


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  print(message)
  msg = message.content

  if message.author.id == (263405587704971264) or message.author.id == (264505493656043520):
    options = nice_stuff
    await message.channel.send(random.choice(options))

  if message.author.id == (293904621821231104):
    options = nice_stuff
    await message.channel.send(random.choice(options))

  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

client.run(os.getenv('TOKEN'))