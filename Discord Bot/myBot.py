import discord
import os
import requests
import json
import random
import replit as db
client = discord.Client()

sad_words = ['Kötü','berbat','ağlayacam','üzgünüm','yardım et']

starter_encouragements = [
  "Biraz dinlenmeye ne dersin?",
  "Gelde iki satır kod yazalım",
  "Hadi ama iyi olmanı istiyorum."
]


if "responding" not in db.keys():
  db["responding"] = True

def get_hi():
  return "Merhaba {0.user}".format(client)

def get_qoute():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)

def update_encourgements(encouraging_message):
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
  print("Discordumuza Hoşgeldiniz sayın {0.user}".format(client))

@client.event
async def on_hadibakalim():
  print("Discordumuz iyi bir yerdir. dsjakdjka")  


@client.event
async def on_message(message):
  if message.author == client.user:
    return


  msg = message.content

  if message.content.startswith("!inspire"):
    quote = get_qoute()
    await message.channel.send(quote)

  if message.content.startswith("!Merhaba"):
    hi = get_hi()
    await message.channel.send(hi)


  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(starter_encouragements))


  if msg.startswith("!new"):
    encouraging_message = msg.split("!new",1)[1]
    update_encourgements(encouraging_message)
    await message.channel.send("Mesajınız alındı.")
    
  if msg.startswith("!del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("!del",1)[1])
      delete_encouragment(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)
  
  if msg.startswith('!list'):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("!responding"):
    value = msg.split("!responding",1)[1]

    if value.lower() == " true":
      db["responding"] = True
      await message.channel.send("responding in on")

    else:
      db["responding"] = False
      await message.channel.send("responding in off")

client.run(os.getenv("TOKEN"))


# Kod replit arayüzüyle yazılmıştır
























