import os
import sys
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse, Message, Body

page = requests.get('https://google.org/crisisresponse/covid19-map')

soup = BeautifulSoup(page.content, 'html.parser')

table_body = soup.find('tbody')

rows = table_body.find_all('tr')

application = Flask(__name__)



@application.route("/")
def home():
    return "App is Running..."

@application.route("/sms", methods=['GET','POST'])
def sms_replay():
    msg = request.values.get('Body')
    n1="\n"

    def search(list, msg):
        for i in range(len(list)):
            if list[i] == msg:
                return True
        return False

        

    for row in rows:
        cols=row.find_all('td')
    
        cols=[x.text.strip() for x in cols]


        if search(cols, msg):
            txtToSend = (
                f"{cols[0].upper()}{n1}{n1}"
                f"Confirmed Cases: {cols[1]}{n1}"
                f"Cases per 1 Million People: {cols[2]}{n1}"
                f"Recoverd: {cols[3]}{n1}"
                f"Deaths {cols[4]}{n1}{n1}"
                f"About This Data: "
                f"{n1}{n1}"
                f"This data changes rapidly, so what’s shown may be out of date(1 Hour old).Information about reported cases is also available on the World Health Organization site.{n1}{n1}"
                f"{n1}{n1}"
                f"To get worlwide data about coronavirus replay with <worldwide>"
                f"{n1}{n1}"
                f"Sorce: https://google.org/crisisresponse/covid19-map"
                f"{n1}{n1}"
                f"Have Questions? Please Visit: https://www.who.int/news-room/q-a-detail/q-a-coronaviruses{n1}{n1}"
                f"Stay Home! Stay Safe!{n1}{n1}{n1}"
                f"DHAVAL VASVELIYA"
                )
            
    resp = MessagingResponse()
    resp.message(txtToSend)

    return str(resp)




if __name__  == "__main__":
    application.run()

    
  
    

    











