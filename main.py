
from nltk.chat.util import Chat, reflections

import datetime

currentDT = datetime.datetime.now()

hr = '0'
cas = "AM"

if currentDT.hour > 12:
    
    hr = str(currentDT.hour - 12)
    cas = "PM"
else:
    
    hr = str(currentDT.hour)
    cas = "AM"



pairs = [
    [r"hi", ["hello , what is your name ?"]],
    [r"hello", ["hi , what is your name ?", ]],
    [r"what is your name ? ", [" my name is baymax , and im chatbot created by eng.adly nady , so how can I help you?", ]],
    [r"what is your name? ", [" my name is baymax , and im chatbot created by eng.adly nady , so how can I help you?", ]],
    [r"what is your name", [" my name is baymax , and im chatbot created by eng.adly nady , so how can I help you?", ]],
    [r"what is your job? ", ["My job is help you, so how can I help you?", ]],
    [r"what is your job ? ", ["My job is help you, so how can I help you?", ]],
    [r"what is your job", ["My job is to help you, so how can I help you?", ]],
    [r"what is something you can't do ? ",
     [" I do not know, but you will find out for yourself when you talk to me ", ]],
    [r"what is something you can't do", ["I do not know, but you will find out for yourself when you talk to me", ]],
    [r"what is something you can't do (.*)",
     ["I do not know, but you will find out for yourself when you talk to me", ]],
    [r"what time is now ?", [" the time now is {0}:{1}:{2} {3}".format(hr, currentDT.minute, currentDT.second, cas), ]],
    [r"what time is now", [" the time now is {0}:{1}:{2} {3}".format(hr, currentDT.minute, currentDT.second, cas), ]],
    [r"what time ?", [" the time now is {0}:{1}:{2} {3}".format(hr, currentDT.minute, currentDT.second, cas), ]],
    [r"what time", [" the time now is {0}:{1}:{2} {3}".format(hr, currentDT.minute, currentDT.second, cas), ]],
    [r"tell me the time", [" the time now is {0}:{1}:{2} {3}".format(hr, currentDT.minute, currentDT.second, cas), ]],
    [r"what date is now ?", [" the time now is {0}-{1}-{2}".format(currentDT.day, currentDT.month, currentDT.year), ]],
    [r"what date is now", [" the time now is {0}-{1}-{2}".format(currentDT.day, currentDT.month, currentDT.year), ]],
    [r"what date ?", [" the time now is {0}-{1}-{2}".format(currentDT.day, currentDT.month, currentDT.year), ]],
    [r"what date", [" the time now is {0}-{1}-{2}".format(currentDT.day, currentDT.month, currentDT.year), ]],
    [r"tell me the date", [" the time now is {0}-{1}-{2}".format(currentDT.day, currentDT.month, currentDT.year), ]],
    [r"my name is (.*)", ["hello %1, how can i help you ?", ]],
    [r"tell me something funny",
     ["I'm so glad we have brown cows, otherwise, there wouldn't be any chocolate milk.🤣", ]],
    [r"can you tell me something funny",
     ["I'm so glad we have brown cows, otherwise, there wouldn't be any chocolate milk.😂", ]],
    [r"(.*)", ["what is the %1 📝", ]],
]


def chatAdly():
    print("ih im adly , im created this chatbot! ")  # defult message


chat = Chat(pairs, reflections)
chat.converse()

if __name__ == "__main__":
    chatAdly()
