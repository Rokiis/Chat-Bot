import socket
import time
import re
import random
from IMDb import imdb
from discordx import discord
import asyncio
import aiohttp
import websockets#Do not edit anything above this unless it is necessary for your code to work.
mv = imdb.IMDb() #imdb connection linking.
client = discord.Client() #discord api connection linking


#KEYWORD FILTERING
GREETING_KEYWORDS = ("hello",  "hi", "greetings", "sup","hey")
GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hello", "hi","nice to hear from you"]#this one had to be put into db too.
def check_for_greeting(sentence): 
	"""If any of the words in the user's input was a greeting, return a greeting response"""
	wordList = re.sub("[^\w]", " ",  sentence).split()
	for word in wordList:
		if word.lower() in GREETING_KEYWORDS:
			returnMess = random.choice(GREETING_RESPONSES)
			return returnMess
			
PRIMARY_QUESTION_KEYWORDS = ("how", "are","is")
SECONDARY_QUESTION_KEYWORDS = ("you","everything","are")
FINAL_QUESTION_KEYWORDS = ("good", "alright"," fine", "you")
QUESTION_RESPONSES = ["I'm good, thanks for asking", "Not so bad", "Pretty good", "So far so good", "Honestly, life is going better that ever", "I've been struggling for a while, but now im good"]
def check_for_questions(sentencex): #also, this function has to be called from different file(database of all Q/A)
	"""If any of the words in the user's input was a greeting, return a greeting response"""
	wordList = re.sub("[^\w]", " ",  sentencex).split()
	returnMess = ("I did'nt understood you question, can you please give me a more simple one? Im a workpiece of a first year students. Dont exepect too much from me.")
	for word1 in wordList:
		if word1 in PRIMARY_QUESTION_KEYWORDS:
			for word2 in wordList:
				if word2 in SECONDARY_QUESTION_KEYWORDS:
					for word3 in wordList:
						if word3 in FINAL_QUESTION_KEYWORDS:
							returnMess = random.choice(QUESTION_RESPONSES)
	return returnMess


def lowercasing(sentence):
	print("LOWERCASING")
	words = sentence.split()
	words = [element.lower() for element in words]
	return words


@client.event #Discord API connection.
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')


@client.event #Test stuff. This will stay here as an example and debugging.
async def on_message(message):	
	if not message.author.bot:
		print(message.content)
		if message.content in GREETING_KEYWORDS:
			response=(check_for_greeting(message.content))
		elif message.content.endswith('?'):
			print("QUESTION")
			message.content.replace("?","")
			response = (check_for_questions(message.content))
		else:
			print("MOVIE")		
			await client.send_message(message.channel, "I'll take a look")
			movie = mv.search_movie(message.content)[0] # a Movie instance.
			m = mv.get_movie(movie.movieID)
			response =("Is that the movie we are talking about? - " + str(movie) + "?")
		await client.send_message(message.channel, response)


#Do not edit anything under this one. 
client.run('Mzc5NjM5MzY0OTkwMjcxNDg4.DOtMdg.SwT7lTbgyDsmpSYOxvMzELHvonM')
