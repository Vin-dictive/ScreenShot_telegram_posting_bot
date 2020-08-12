import pymongo
import schedule
import time
import os
import requests
import json

myclient = pymongo.MongoClient(<MONGO ID>)
mydb = myclient[<Database>]
mycol = mydb[<COLLECTION>]
x = mycol.find_one()

def update_db(title):
    
    if mycol.find({"title":title}).count() == 0 :
        print("Picture Does'nt Exist")
        data = title
        send_photo(data)
    mycol.update({"title":title},{"$set":{"title":title}},upsert=True)     
    
def send_screen_shot():
    for root, dirs, files in os.walk("."):
        for filename in files:
#             print(filename)
            update_db(filename)


def send_photo(f):
    bot_token = '<bot_token>'
    chat_id = "<chat id to post on>"
    file = f

    files = {
        'photo': open(file, 'rb')
    }

    message = ('https://api.telegram.org/bot'+ bot_token + '/sendPhoto?chat_id=' 
               + chat_id)
    send = requests.post(message, files = files)


schedule.every(1).second.do(send_screen_shot)

while True:
    schedule.run_pending()
    time.sleep(1)
