#varible to collect different swear words and reponses to them stored in a list
SWEAR_KEYWORDS = ('fuck', 'stfu', 'idiot', 'noob', 'faggot','bullshit','bs','fck','fcker','fucker','bastard', 'cunt')
SWEARING_RESPONSES = ["That was not cool...", "Wow, ur such a badass....", "Well, im not used to this kind of language", "Please, dont swear while im on this channel", "Yo, there might be some kids running around", "WOW. Ur such a man. That was a cool word... *sarcasm*"]


def check_for_swears(sentence): #function checks if any of user input includes words that are in SWEAR_KEYWORDS list
	wordList = re.sub("[^\w]", " ",  sentence).split() #breaks the sentence into single words
	for word in wordList: 
		if word in SWEAR_KEYWORDS:
			return True #if the sentence contains a swearword stored in the list SWEAR_KEYWORDs, function becomes true
        
if check_for_swears(message.content) == True: #if the user's input returns true for check_for_swears function (contains a swearword )
			response = random.choice(SWEARING_RESPONSES) #the chatbot gives a repsonse that tells user not to swear 
