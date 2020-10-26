import offers
import requests
import time
import datetime

#DurstExpressBot
#username telegram: DurstExpress_bot 

token = #enter your token from telegram bot father here
api = 'https://api.telegram.org/bot'+ token + '/getUpdates'
sendURL = 'https://api.telegram.org/bot'+ token + '/sendMessage'

update_raw = requests.get(api)
update = update_raw.json()

articles = {}

#if you are not located in Germany change the daynames to your matching language
#they are needed for running the script on a schedule 
days = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']

def extract_result(dict):
    result_array = dict['result']
    if result_array == []:
        return False
    else:
        result_dict = result_array[0]
        return result_dict   

def send_message(chatID, message):
    requests.post(sendURL + '?chat_id=' + chatID + '&text=' + message)

def bot(chatID):
    try:    
        Angebote.searchCategory()
        articles = Angebote.getArticles()
        text = 'Aktuelle Angebote bei Durstexpress'
        send_message(chatID, text)
        for marke, price in articles.items():
            text = str(marke) + '\n' + str(price) + '\n'
            send_message(chatID, text)    
        text = 'Das wars für heute :=)'
        send_message(chatID, text)
    except requests.exceptions.ConnectionError:
        pass    
   
#get chat_id
final_result = extract_result(update)
chatID = str(final_result['message']['chat']['id'])

while True:
    today = datetime.date.today()
    dayNumber = datetime.date.weekday(today)
    now = datetime.datetime.now()
    hour = now.strftime('%H')
    if days[dayNumber] == 'Montag' and hour == '10':
        print('starting')
        bot(chatID)        
    else:
        pass    
    time.sleep(3600)
