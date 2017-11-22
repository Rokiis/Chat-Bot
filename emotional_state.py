import re
import random

SAD_KEYWORDS = ('sad', 'upset', 'down', 'unhappy', 'sorrowful', 'dejected', 'regretful', 'depressed', 'downcast', 'miserable', 'downhearted', 'down', 'despondent', 'despairing', 'disconsolate', 'out of sorts', 'desolate', 'bowed down', 'wretched', 'glum', 'gloomy', 'doleful', 'dismal', 'blue', 'melancholy', 'melancholic', 'low-spirited', 'mournful', 'woeful', 'woebegone', 'forlorn', 'crestfallen', 'broken-hearted', 'heartbroken', 'inconsolable', 'grief-stricken', 'down in the mouth', 'down in the dumps')
SAD_RESPONSES = ['Whats wrong bud?', 'Dont be so down :frowning:', 'Wanna talk about it?', '*BEEP BOOP*... Cheer up pal...', 'Look at the bright side. Your talking to a :robot:']
HAPPY_KEYWORDS = ('happy', 'contented', 'content', 'cheerful', 'cheery', 'merry', 'joyful', 'jovial', 'jolly', 'jocular', 'gleeful', 'carefree', 'untroubled', 'delighted', 'smiling', 'beaming', 'grinning', 'glowing', 'satisfied,' 'gratified', 'buoyant', 'radiant', 'sunny', 'blithe', 'joyous', 'beatific', 'blessed', 'cock-a-hoop', 'in good spirits', 'in high spirits', 'in a good mood', 'light-hearted', 'good-humoured', 'thrilled', 'exuberant', 'elated', 'exhilarated', 'ecstatic', 'blissful', 'euphoric', 'overjoyed', 'exultant', 'rapturous', 'rapt', 'enraptured', 'in seventh heaven', 'on cloud nine', 'over the moon', 'walking on air', 'beside oneself with joy', 'jumping for joy', 'chirpy', 'on top of the world', 'as happy as a sandboy', 'tickled pink', 'tickled to death', 'like a dog with two tails', 'as pleased as punch', 'on a high', 'blissed out', 'as happy as larry', 'happy as a clam', 'datedgay', 'rareblithesome', 'jocose', 'jocund')
HAPPY_RESPONSES = ['Thats the spirit!', 'Youve got a good mindset', 'Emotions look like fun', '*BEEP BOOP*', 'I know im a robot and all, no need to get excited']
EXCITED_KEYWORDS = ('excited', 'thrilled', 'exhilarated', 'elevated', 'enlivened', 'electrified', 'stirred', 'moved', 'delighted', 'exuberant', 'enraptured', 'intoxicated', 'feverish', 'enthusiastic', 'eager', 'high as a kite', 'fired up', 'tickled', 'tickled pink', 'full of beans', 'bright-eyed and bushy-tailed', 'peppy', 'sparky')
ANGRY_KEYWORDS = ()
ANGRY_RESPONSES = ()
def check_for_sad(sentence):
    wordlist = re.sub("[^\w]", " ", sentence).split()
    for word in wordlist:
        if word in SAD_KEYWORDS:
            returnMess = random.choice(SAD_RESPONSES)
            return returnMess

def check_for_happy(sentence):
    wordlist = re.sub("[^\w]", " ", sentence).split()
    for word in wordlist:
        if word in HAPPY_KEYWORDS:
            returnMess = random.choice(HAPPY_RESPONSES)
            return returnMess
        
def check_for_excited(sentence):
    wordlist = re.sub("[^\w]", " ", sentence).split()
    for word in wordlist:
        if word in EXCITED_KEYWORDS:
            returnMess = random.choice(HAPPY_RESPONSES)
            return returnMess
        
        
        
        return None
