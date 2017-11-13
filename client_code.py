import socket
import time
import re
import random
from IMDb import imdb
from discordx import discord
import asyncio
import aiohttp
import websockets#Do not edit anything above this unless it is necessary for your code to work.
imv = imdb.IMDb() #imdb connection linking.
client = discord.Client() #discord api connection linking


 # Sentences we'll respond with if the user greeted us
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",) #this has to be put into database.
GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]#this one had to be put into db too.

def check_for_greeting(sentence): #also, this function has to be called from different file(database of all Q/A)
	"""If any of the words in the user's input was a greeting, return a greeting response"""
	wordList = re.sub("[^\w]", " ",  sentence).split()
	for word in wordList:
		if word.lower() in GREETING_KEYWORDS:
			returnMess = random.choice(GREETING_RESPONSES)
			return returnMess



@client.event #Discord API connection.
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')


@client.event #Test stuff. This will stay here as an example and debugging.
async def on_message(message):	
	print(message.content)
	if message.content.startswith('!test'):
		counter = 0
		tmp = await client.send_message(message.channel, 'Calculating messages...')
		async for log in client.logs_from(message.channel, limit=100):
			if log.author == message.author:
				counter += 1

		await client.edit_message(tmp, 'You have {} messages.'.format(counter))
	elif message.content.startswith('!sleep'):
		await asyncio.sleep(5)
		await client.send_message(message.channel, 'Done sleeping')
	if message.content in GREETING_KEYWORDS:
		response=(check_for_greeting(message.content))
	await client.send_message(message.channel, response)


#Do not edit anything under this one. 
client.run('Mzc5NjM5MzY0OTkwMjcxNDg4.DOtMdg.SwT7lTbgyDsmpSYOxvMzELHvonM')
