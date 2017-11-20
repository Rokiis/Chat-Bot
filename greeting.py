def check_for_greeting(sentence): 
GREETING_KEYWORDS = ("hello",  "hi", "greetings", "sup", "hey", "sup dog", "yo", "hey bro", "hey robot", "good morning", "good afternoon", "good evening", "morning", "hey ya", "hey there", "hello chatbot", "hey man", "wazzup?", "sup?", "yo!", "howdy-doody!", "hey there", "hey mister robot", "hey mr robot", "hello mate", "hey boo", "aloha", "bonjour", "sup robot" )
GREETING_RESPONSES = ["'sup bro :smile:", "hey :smile:", "*nods*", "hello", "hi", "nice to hear from you", "hello human", "hey human", "Greetings from the smartest chatbot",  ]#this one had to be put into db too.
	"""If any of the words in the user's input was a greeting, return a greeting response"""
	wordList = re.sub("[^\w]", " ",  sentence).split()
	for word in wordList:
		if word.lower() in GREETING_KEYWORDS:
			returnMess = random.choice(GREETING_RESPONSES)
			return returnMess