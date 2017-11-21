def random_question_filter(message):
    if message == "how old are you":
        return "I dont have age"
    elif message == "who made you" or message =="who is your creator" or message == "who invented you?" or message =="who is your ceo":
        return "Students From Coventry Univeristy created me"
    elif message == "what are you" or message =="who are you":
        return "Come on man im just a Movie Chatbot "
    elif message == "when did you born":
        return "I dont get it with these type of questions but just to let you know 2 days ago"
    elif message == "what is your nationality":
        return "im from Coding country"
    elif message == "tell me a joke":
        return "No jokes allowed here pal just movie questions "
    elif message == "where do you live":
        return "i live in python world :smile:"
    elif message == "are you smart":
        return "I only know about movies so if you wanna try me go for it!! :sunglasses: "
    elif message == "where is your server located":
        return "Actually one of the students runs me on his device "
    elif message == "are you a robot":
        return "To be honest I am a :robot:"
    elif message == "are you real":
        return "No man im just a :robot: "
    elif message == "how does it work":
        return "Go on bro ask me something you want from a movie(summary,actors,genre)"
    elif message == "do you like donald trump" "do you like trump":
        return "I dont talk about politics ONLY MOVIES SIR!"
    elif message == "what's the weather":
        return "How do you expect me to know im not a weather forecast"
    return None