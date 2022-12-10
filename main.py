import discord
import requests

api_url = "http://0.0.0.0:5005/webhooks/rest/webhook"
TOKEN = "MTA0NzU3MDMyOTg4MDUwNjQyMA.GtuIZW.DtxW-C4i5PBAJdf2gsBn1zFBuAtnPbZjuCM9sk"

client = discord.Client()

@client.event
async def on_ready():
    print('Ready to talk to bot')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('$bot'):

        question = {
            "sender": message.author.id,
            "message": message.content[5:]
        }

        response = requests.post(api_url, json=question)
        data = response.json()

        if len(data) == 0:
            bot_response = 'No response to that'
            await message.channel.send(bot_response)
        else:
            for i in data:
                bot_response = '<@'+i["recipient_id"]+'> '+i["text"]
                await message.channel.send(bot_response)



client.run(TOKEN)