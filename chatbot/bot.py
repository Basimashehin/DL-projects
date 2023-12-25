from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pyttsx3
import webbrowser
txt_sp=pyttsx3.init()
# for error collection not hashable
# import collections.abc
# collections.Hashable=collections.abc.Hashable
chatbot=ChatBot('mybot')
trainer=ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english','chatterbot.corpus.english.conversations')
while(True):
   qns=input("Me: ")
   if qns=='bye':
      print("Bot: bye")
      break
   elif 'search' in qns:
      print("searching..............",qns.split('search')[1])
      url='https://google.com/search?q='+qns.split('search')[1]
      print(url)
      try:
        webbrowser.get().open(url)
      except:
         print("check your internet connection")
   else:
      response=chatbot.get_response(qns)
      print("Bot: ",response)
      txt_sp.say(response)
      txt_sp.runAndWait()


