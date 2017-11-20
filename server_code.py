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
memory = []

AGGREE_KEYOWORDS = ('yes','y','yeah')
FILTERING_KEYWORDS = ('summary','release','date','director')
#KEYWORD FILTERING
GREETING_KEYWORDS = ('hello',  'hi', 'greetings', 'sup','hey')
GREETING_RESPONSES = ["'sup bro",":kappa:" "hey", "*nods*", "hello", "hi","nice to hear from you"]
def check_for_greeting(sentence): 
	wordList = re.sub("[^\w]", " ",  sentence).split()
	for word in wordList:
		if word in GREETING_KEYWORDS:
			returnMess = random.choice(GREETING_RESPONSES)
			return returnMess
			
QUESTION_KEYWORDS = ('how','are','you','good','alright','hows','it','going','ok')
QUESTION_RESPONSES = ["I'm good, thanks for asking", "Not so bad", "Pretty good", "So far so good", "Honestly, life is going better that ever", "I've been struggling for a while, but now im good"]
def check_for_questions(sentence): #also, this function has to be called from different file(database of all Q/A)
	wordList = re.sub("[^\w]", " ",  sentence).split()
	returnMess = ("I did'nt understood your question, can you please give me a more simple one? Im a workpiece of a first year students. Dont exepect too much from me.")
	y=0
	while y < len(wordList)-1:
		if wordList[y] in QUESTION_KEYWORDS and wordList[y+1] in QUESTION_KEYWORDS and wordList[y+1] in QUESTION_KEYWORDS:
			returnMess = random.choice(QUESTION_RESPONSES)
		y=y+1
	return returnMess


def lowercasing(sentence):
	words = re.sub("[^\w]", " ",  sentence).split()
	words = [element.lower() for element in words]
	return " ".join(words)

def filter_on_message(message):
	wordList = re.sub("[^\w]", " ",  message).split()
	for word in wordList:
		if word in FILTERING_KEYWORDS:
			returnMess = word 
			return returnMess

def filter_on_movie(message):
	lists = re.sub("[^\w]", " ",  message).split()
	i = 0
	while i < len(lists):
		if lists[i] != "movie":
			lists.remove(lists[i])
			i=0
		elif lists[i] == "movie":
			lists.remove("movie")
			if "of" in lists:
				lists.remove("of")
			return " ".join(lists)
@client.event #Discord API connection.
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')


@client.event #Test stuff. This will stay here as an example and debugging.
async def on_message(message):
	if not message.author.bot:
		msg = message.content
		memory.append(message.content)
		message.content = lowercasing(msg)
		print(message.content)
		if message.content.startswith('test'):
			response = (":scream:")
		elif "movie" in message.content:
			moviefound = filter_on_movie(message.content)
			memory.append(moviefound)
			movie = mv.search_movie(moviefound)[0] # a Movie instance.
			m = mv.get_movie(movie.movieID)
			if message.content in FILTERING_KEYWORDS:
				filteredkeyword = (filter_on_message)
				response = ("I wish i could give you the " + str(filteredkeyword) + " of the movie " + str(m))
			else:
				response = ("Is this the movie you have asked about?" + str(m))

		elif message.content in AGGREE_KEYOWORDS:
			print("AGGREED")
			print(str(memory[-2] + "MEMORY LAST"))
			movie = mv.search_movie(memory[-2])[0] # a Movie instance.
			m = mv.get_movie(movie.movieID)
			response = ("What would you want to know about this movie? -" + str(m) + ". Write the thing you want to know only please.")
		elif message.content in FILTERING_KEYWORDS:
			print("FILTERING")
			keyword = filter_on_message(memory[-1])
			print("MOVIE MEMORY" + str(memory[-3]))
			movie = mv.search_movie(memory[-3])[0] # a Movie instance.
			m = mv.get_movie(movie.movieID)
			response = ("I cant give the " + str(keyword) + " of movie - " + str(m) + " yet. I'm sorry... :weary: ")
		elif message.content in GREETING_KEYWORDS:
			print("GREETING")
			response=(check_for_greeting(message.content))
			print(response)
		elif msg.endswith('?'):
			print("QUESTION")
			message.content.replace("?","")
			response = (check_for_questions(message.content))
			print(response)
		await client.send_message(message.channel, response)


#Do not edit anything under this one. 
client.run('Mzc5NjM5MzY0OTkwMjcxNDg4.DOtMdg.SwT7lTbgyDsmpSYOxvMzELHvonM')
