import socket
import time
import re
import random
import random_questions
from IMDb import imdb
from discordx import discord
import asyncio
import aiohttp
import websockets#Do not edit anything above this unless it is necessary for your code to work.
mv = imdb.IMDb() #imdb connection linking.
client = discord.Client() #discord api connection linking
memory = []
stuff = ["", ""]
choices = [""]
AGGREE_KEYOWORDS = ('yes','y','yeah')
DISAGGGREE_KEYWORDS = ('no', 'n', 'nope')
FILTERING_KEYWORDS = ('title', 'genres', 'director', 'writer', 'cast', 'language', 'country', 'rating', 'plot')
SWEAR_KEYWORDS = ('fuck', 'stfu', 'idiot', 'noob', 'faggot','bullshit','bs','fck','fcker','fucker','bastard', 'cunt')
SWEARING_RESPONSES = ["That was not cool...", "Wow, ur such a badass....", "Well, im not used to this kind of language", "Please, dont swear while im on this channel", "Yo, there might be some kids running around", "WOW. Ur such a man. That was a cool word... *sarcasm*"]
GREETING_KEYWORDS = ("hello",  "hi", "greetings", "sup", "hey", "sup dog", "yo", "hey bro", "hey robot", "good morning", "good afternoon", "good evening", "morning", "hey ya", "hey there", "hello chatbot", "hey man", "wazzup?", "sup?", "yo!", "howdy-doody!", "hey there", "hey mister robot", "hey mr robot", "hello mate", "hey boo", "aloha", "bonjour", "sup robot" )
GREETING_RESPONSES = ["'sup bro :smile:", "hey :smile:", "*nods*", "hello", "hi", "nice to hear from you", "hello human", "hey human", "Greetings from the smartest chatbot",  ]#this one had to be put into db too.
def check_for_greeting(sentence): 
	wordList = re.sub("[^\w]", " ",  sentence).split()
	for word in wordList:
		if word in GREETING_KEYWORDS:
			returnMess = random.choice(GREETING_RESPONSES)
			return returnMess
			
QUESTION_KEYWORDS = ('how','are','you','good','alright','hows','it','going','ok')
QUESTION_RESPONSES = ["I'm good, thanks for asking", "Not so bad", "Pretty good", "So far so good", "Honestly, life is going better that ever", "I've been struggling for a while, but now im good"]
IDK_RESPONSES = ["I did'nt understood your question, can you please give me a more simple one? Im a workpiece of a first year students. Dont exepect too much from me.","What is that?", "Ok, next question...","IM A ROBOT *beep* *bop* *boop* CANT UNDERSTAND HOOMANS","What language is this? Definately not ROBOTish"]
def check_for_questions(sentence): #also, this function has to be called from different file(database of all Q/A)
	wordList = re.sub("[^\w]", " ",  sentence).split()
	returnMess = random.choice(IDK_RESPONSES)
	y=0
	while y < len(wordList)-1:
		if wordList[y] in QUESTION_KEYWORDS and wordList[y+1] in QUESTION_KEYWORDS and wordList[y+1] in QUESTION_KEYWORDS:
			returnMess = random.choice(QUESTION_RESPONSES)
		y=y+1
	return returnMess

def check_for_swears(sentence): 
	wordList = re.sub("[^\w]", " ",  sentence).split()
	for word in wordList:
		if word in SWEAR_KEYWORDS:
			return True


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
def keywording(summarisation, keyword):
	keywordx = keyword.capitalize()
	text = summarisation.split('\n')
	for i in text:
		if keywordx in i:
			return i


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
			if lists == []:
				return False
			else:
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
		randomly = None
		msg = message.content
		memory.append(message.content)
		message.content = lowercasing(msg)
		randomly = random_questions.random_question_filter(message.content)
		if randomly != None:
			response = randomly
		elif message.content == "clear":
			del memory[:]
			response = ("Okay, lets start again... Im IMDb ChatBot")
		elif check_for_swears(message.content) == True:
			response = random.choice(SWEARING_RESPONSES)
		elif message.content in GREETING_KEYWORDS:
			print("GREETING")
			response=(check_for_greeting(message.content))
			print(response)
		elif msg.endswith('?'):
			print("QUESTION")
			message.content.replace("?","")
			response = (check_for_questions(message.content))
		elif message.content in AGGREE_KEYOWORDS:
			print("AGGREED")
			print(str(memory[-2] + "MEMORY LAST"))
			movie = mv.search_movie(memory[-2])[0] # a Movie instance.
			m = mv.get_movie(movie.movieID)
			print(str(m))
			response = ("What would you want to know about this movie? -" + str(m) + ". Write the thing you want to know only please."+ '\n' + "Type -choices- to see all available options...")
		elif message.content in DISAGGGREE_KEYWORDS:
			print("DISAGGREED")
			stuff[1] = "What movie?"
			response = "What movie then? Please, try to type the full title this time. If you want me to forget this movie, type -clear-"	
		elif choices[0] == "a":
			choices[0] == ""
			print("FILTERING")
			keyword = filter_on_message(message.content)
			movie = mv.search_movie(memory[-4])[0] # a Movie instance.
			m = mv.get_movie(movie.movieID)
			del memory[:]
			if keyword == "summary":
				print("SUMMARISING... ... ...")
				response = (m.summary())
			else:
				print(keywording(m.summary(),keyword))
				response = keywording(m.summary(),keyword)
		elif message.content == "choices":
			choices[0] = "a"
			response = ("Title, Genres, Director, Writer, Cast, Language, Country, Rating, Plot.")
		elif "movie" in message.content:
			print("MOVIE")
			moviefound = filter_on_movie(message.content)
			if moviefound == False:
				stuff[0]= "What movie?"
				response =  "What movie?"
			else:
				memory.append(moviefound)
				movie = mv.search_movie(moviefound)[0] # a Movie instance.
				m = mv.get_movie(movie.movieID)
				response =  ("Is this the movie you have asked about?" + str(m))
		elif stuff[0] == "What movie?":
			stuff[0] = ""
			print(message.content)
			msg = message.content
			movie = mv.search_movie(message.content)[0]
			m = mv.get_movie(movie.movieID)
			response =  ("Is this the movie you have asked about?" + str(m))
		elif stuff[1] == "What movie?":
			print("REMOVIE")
			stuff[1] = ""
			print(message.content)
			moviex = mv.search_movie(message.content)[0]
			mx = mv.get_movie(moviex.movieID)
			response =  ("Sorry,Is this the movie you have asked about?" + str(mx))
		elif message.content in FILTERING_KEYWORDS:
			print("FILTERING")
			keyword = filter_on_message(memory[-1])
			print("MOVIE MEMORY" + str(memory[-3]))
			movie = mv.search_movie(memory[-3])[0] # a Movie instance.
			m = mv.get_movie(movie.movieID)
			del memory[:]
			response = ("I cant give the " + str(keyword) + " of movie - " + str(m) + " yet. I'm sorry... :weary: ")
			if keyword == "summary":
				print("SUMMARISING... ... ...")
				response = (m.summary())
			else:
				print(keywording(m.summary(),keyword))
				response = keywording(m.summary(),keyword)
		else:
			response = check_for_questions(message.content)
		await client.send_message(message.channel, response)


#Do not edit anything under this one. 
client.run('Mzc5NjM5MzY0OTkwMjcxNDg4.DOtMdg.SwT7lTbgyDsmpSYOxvMzELHvonM')
