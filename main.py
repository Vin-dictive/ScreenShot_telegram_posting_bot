import pymongo
import schedule
import time
import os
import requests
import json

myclient = pymongo.MongoClient("mongodb+srv://vinay_1998:sepI6llmqwFPJWUe@bookmarker-cofya.gcp.mongodb.net/AIT_placements_bot?retryWrites=true&w=majority")
mydb = myclient["Screenshots_bot"]
mycol = mydb["pictures_name"]
x = mycol.find_one()

def update_db(title):
    
    mycol = mydb["pictures_name"]
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
    bot_token = '1370880217:AAHC6s3sKvWp9V9Utnwl-ouccz1tNKzGhNQ'
    chat_id = "-499571829"
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