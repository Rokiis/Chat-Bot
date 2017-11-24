import socket
import time
import re
import random
import random_questions
import emotional_state
import greeting
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
		greeting = None #reseting keyword filters before every input not to mess up filtering sequence.
		randomly = None
		happy = None
		sad = None
		excited = None
		angry = None
		memory.append(message.content) #writing input into short term memory
		msg = message.content
		message.content = lowercasing(msg) #lowercasing all the letters in order to get the right input despite uppercased letters.
		mesg = message.content #getting a message content into other variable in order to keep original safe until the end of function
		randomly = random_questions.random_question_filter(mesg) #check for random questions
		sad = emotional_state.check_for_sad(mesg) #check for sad emotions
		happy = emotional_state.check_for_happy(mesg) #check for happy emotions
		excited = emotional_state.check_for_excited(mesg) # check for excitment
		angry = emotional_state.check_for_angry(mesg) #check for angry emotions
		if check_for_swears(message.content) == True: #swear filter
			response = random.choice(SWEARING_RESPONSES)
		elif happy != None: #filtering whitch emotions were triggered
			print("Happy")
			response = happy
		elif greeting != None:
			print("GREETING#1")
			response = greeting
		elif sad != None:
			print("SAD")
			response = sad
		elif excited != None:
			print("Excited")
			response = excited
		elif angry != None:
			print("Angry")
			response = angry
		elif randomly != None:
			print("RANDOM")
			response = randomly
		elif message.content == "clear": #if the input is -clear- wiping out the memory of chatbot
			del memory[:]
			choices[0] = ""
			stuff[0] = ""
			response  = ("Okay, lets start again... Im IMDb ChatBot")
		elif message.content in AGGREE_KEYOWORDS:
			print("AGGREED") # If input is YES or Y, robot takes the last movie as requested.
			movie = mv.search_movie(memory[-2])[0] # a Movie instance.
			m = mv.get_movie(movie.movieID)
			response = ("What would you want to know about this movie? -" + str(m) + ". Write the thing you want to know only please."+ '\n' + "Type -choices- to see all available options...")
		elif message.content in DISAGGGREE_KEYWORDS: # If the input is no or n, chatbot double checks for the movie requested.
			print("DISAGGREED")
			stuff[1] = "What movie?"
			response = "What movie then? Please, try to type the full title this time. If you want me to forget this movie, type -clear-"	
		elif choices[0] == "a": #Movie and summary filtering if -choices- was typed in
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
				response = keywording(m.summary(),keyword)
		elif message.content == "choices": #if an input is -choices-, chatbot gives choices of summary parts to be given.
			choices[0] = "a"
			response = ("Title, Genres, Director, Writer, Cast, Language, Country, Rating, Plot.")
		elif "movie" in message.content: # if sentence has word movie in it, it filters out to get the exact movie request.
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
		elif stuff[0] == "What movie?": #if he cant fint the movie, he asks what movie should he find.
			stuff[0] = ""
			msg = message.content
			movie = mv.search_movie(message.content)[0]
			m = mv.get_movie(movie.movieID)
			response =  ("Is this the movie you have asked about?" + str(m))
		elif stuff[1] == "What movie?":#if he cant fint the movie, he asks what movie should he find.
			print("REMOVIE")
			stuff[1] = ""
			moviex = mv.search_movie(message.content)[0]
			mx = mv.get_movie(moviex.movieID)
			response =  ("Sorry,Is this the movie you have asked about?" + str(mx))
		elif message.content in FILTERING_KEYWORDS: # filtering for summary if -choices- wasnt typed in
			print("FILTERING")
			keyword = filter_on_message(message.content)
			print("MOVIE MEMORY - " + str(memory[-3]))
			movie = mv.search_movie(memory[-3])[0] # a Movie instance.
			m = mv.get_movie(movie.movieID)
			del memory[:]
			if keyword == "summary":
				print("SUMMARISING... ... ...")
				response = (m.summary())

			else:

				response = keywording(m.summary(),keyword)
		elif msg.endswith('?'): #check for questions
			print("QUESTION")
			message.content.replace("?","")
			response = (check_for_questions(message.content))		
		else: # if there was no triggers in this function, chatbot gives an output of message unknown.
			response = check_for_questions(message.content)
		await client.send_message(message.channel, response) #Message Send line.


#Do not edit anything under this one. 
client.run('Mzc5NjM5MzY0OTkwMjcxNDg4.DOtMdg.SwT7lTbgyDsmpSYOxvMzELHvonM') #ChatBot token in order for it to login to Discord app.
