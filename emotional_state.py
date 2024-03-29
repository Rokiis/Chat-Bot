import re
import random


def check_for_sad(sentence):
    SAD_KEYWORDS = ('sad', 'upset', 'down', 'unhappy', 'sorrowful', 'dejected', 'regretful', 'depressed', 'downcast', 'miserable', 'downhearted', 'down', 'despondent', 'despairing', 'disconsolate', 'out of sorts', 'desolate', 'bowed down', 'wretched', 'glum', 'gloomy', 'doleful', 'dismal', 'blue', 'melancholy', 'melancholic', 'low-spirited', 'mournful', 'woeful', 'woebegone', 'forlorn', 'crestfallen', 'broken-hearted', 'heartbroken', 'inconsolable', 'grief-stricken', 'down in the mouth', 'down in the dumps')
    SAD_RESPONSES = ['Whats wrong bud?', 'Dont be so down :frowning:', 'Wanna talk about it?', '*BEEP BOOP*... Cheer up pal...', 'Look at the bright side. Your talking to a :robot:']
    wordlist = re.sub("[^\w]", " ", sentence).split()
    for word in wordlist:
        if word in SAD_KEYWORDS:
            returnMess = random.choice(SAD_RESPONSES)
            return returnMess
    return None


def check_for_happy(sentence):
    HAPPY_RESPONSES = ['Thats the spirit!', 'Youve got a good mindset', 'Emotions look like fun', '*BEEP BOOP*', 'I know im a robot and all, no need to get excited']
    HAPPY_KEYWORDS = ('happy', 'contented', 'content', 'cheerful', 'cheery', 'merry', 'joyful', 'jovial', 'jolly', 'jocular', 'gleeful', 'carefree', 'untroubled', 'delighted', 'smiling', 'beaming', 'grinning', 'glowing', 'satisfied,' 'gratified', 'buoyant', 'radiant', 'sunny', 'blithe', 'joyous', 'beatific', 'blessed', 'cock-a-hoop', 'in good spirits', 'in high spirits', 'in a good mood', 'light-hearted', 'good-humoured', 'thrilled', 'exuberant', 'elated', 'exhilarated', 'ecstatic', 'blissful', 'euphoric', 'overjoyed', 'exultant', 'rapturous', 'rapt', 'enraptured', 'in seventh heaven', 'on cloud nine', 'over the moon', 'walking on air', 'beside oneself with joy', 'jumping for joy', 'chirpy', 'on top of the world', 'as happy as a sandboy', 'tickled pink', 'tickled to death', 'like a dog with two tails', 'as pleased as punch', 'on a high', 'blissed out', 'as happy as larry', 'happy as a clam', 'datedgay', 'rareblithesome', 'jocose', 'jocund')
    wordlist = re.sub("[^\w]", " ", sentence).split()
    for word in wordlist:
        if word in HAPPY_KEYWORDS:
            returnMess = random.choice(HAPPY_RESPONSES)
            return returnMess
    return None

        
def check_for_excited(sentence):
    EXCITED_KEYWORDS = ('excited', 'thrilled', 'exhilarated', 'elevated', 'enlivened', 'electrified', 'stirred', 'moved', 'delighted', 'exuberant', 'enraptured', 'intoxicated', 'feverish', 'enthusiastic', 'eager', 'high as a kite', 'fired up', 'tickled', 'tickled pink', 'full of beans', 'bright-eyed and bushy-tailed', 'peppy', 'sparky')
    HAPPY_RESPONSES = ['Thats the spirit!', 'Youve got a good mindset', 'Emotions look like fun', '*BEEP BOOP*', 'I know im a robot and all, no need to get excited']
    wordlist = re.sub("[^\w]", " ", sentence).split()
    for word in wordlist:
        if word in EXCITED_KEYWORDS:
            returnMess = random.choice(HAPPY_RESPONSES)
            return returnMess
    return None

def check_for_angry(sentence):
    ANGRY_KEYWORDS = ('irate', 'annoyed', 'cross', 'vexed', 'irritated', 'exasperated', 'indignant', 'aggrieved', 'irked', 'piqued', 'displeased', 'provoked', 'galled', 'resentful', 'furious', 'enraged', 'infuriated', 'in a temper', 'incensed', 'raging', 'incandescent', 'wrathful', 'fuming', 'ranting', 'raving', 'seething', 'frenzied', 'in a frenzy', 'beside oneself', 'outraged', 'in high dudgeon', 'irascible', 'bad-tempered', 'hot-tempered', 'choleric', 'splenetic', 'dyspeptic', 'tetchy', 'testy', 'crabby', 'waspish', 'hostile', 'antagonistic', 'mad', 'hopping mad', 'livid', 'as cross as two sticks', 'boiling', 'apoplectic', 'aerated', 'hot under the collar', 'riled', 'on the warpath', 'up in arms', 'with all guns blazing', 'foaming at the mouth', 'steamed up', 'in a lather', 'in a paddy', 'fit to be tied', 'aggravated', 'snappy', 'snappish', 'shirty', 'stroppy', 'narky', 'ratty', 'eggy', 'teed off', 'ticked off', 'ropeable', 'snaky', 'crook', 'vex', 'pissed off', 'pissed', 'pisses')
    ANGRY_RESPONSES = ['No need to get so heated', 'Alright, calm down pal', 'No need to be so hostile, im only a :robot:', 'Im sorry you feel that way']
    wordlist = re.sub("[^\w]", " ", sentence).split()
    for word in wordlist:
        if word in ANGRY_KEYWORDS:
            returnMess = random.choice(ANGRY_RESPONSES)
            return returnMess  
    return None   
        
