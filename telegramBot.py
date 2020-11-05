import Angebote
import requests
import time
import datetime

#DurstExpressBot
#username telegram: DurstExpress_bot 

token = '1308432447:AAEIe1mrS-8kYO2dWizretTjkELjLBPT03w'
api = 'https://api.telegram.org/bot'+ token + '/getUpdates'
sendURL = 'https://api.telegram.org/bot'+ token + '/sendMessage'

update_raw = requests.get(api)
update = update_raw.json()

articles = {}

user_chat_id = []

user_input = {}

outgoing_messages = {}

#if you are not located in Germany change the daynames to your matching language
#they are needed for running the script on a schedule 
days = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']

index = 0

def send_message(chatID, message):
    requests.post(sendURL + '?chat_id=' + chatID + '&text=' + message)

def bot(chatID):
    try:    
        Angebote.searchCategory()
        articles = Angebote.getArticles()
        text = 'Aktuelle Angebote bei Durstexpress'
        send_message(chatID, text)
        for item, price in articles.items():
            text = str(item) + '\n' + str(price) + '\n'
            send_message(chatID, text)    
        text = 'Das wars für heute :=)'
        send_message(chatID, text)
    except requests.exceptions.ConnectionError:
        pass    

def getChatID():
    index_max = getJsonLength()
    for i in range(index, index_max):
        id = str(update['result'][i]['message']['chat']['id'])
        user_chat_id.append(id)

    ids = list(dict.fromkeys(user_chat_id))   
    return ids     
        
def getJsonLength():
    index_max = len(update['result'])
    return index_max

def getUserLength():
    userLength = len(getChatID()) - 1
    return userLength

def getUpdateIDs():
    currentUpdateID = update['result'][getJsonLength()-1]['update_id']
    return currentUpdateID

def getLastUserInput():
    for value in update['result']:
        currentInput = []
        currentInput.append(value)
        update_id = currentInput[0]['update_id']
        userInput = currentInput[0]['message']['text']        
        if update_id == getUpdateIDs():
            user = str(currentInput[0]['message']['chat']['id'])
            user_input[user] = userInput
        else:
            pass    
    return user_input

#while True:
#    today = datetime.date.today()
#    dayNumber = datetime.date.weekday(today)
#    now = datetime.datetime.now()
#    hour = now.strftime('%H')
#    if days[dayNumber] == 'Montag' and hour == '10':
#        print('starting')
#        for x in getChatID():
#            chatID = x
#            bot(chatID)        
#    else:
#        pass    
#    time.sleep(3600)

Angebote.searchCategory()
articles = Angebote.getArticles()
print(articles)