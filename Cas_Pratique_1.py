import requests
from bs4 import BeautifulSoup

keyword = "salut"
boolean = "true"


api = "http://127.0.0.1:5000/search=" + keyword + "/media=" + boolean

response = requests.get(api)

if response.ok :

    soup = BeautifulSoup(response.text, "lxml")
    text_of_tweet = soup.find("p").getText()

    print (text_of_tweet)

else :
    print ("Tu as oublié de de Run ton fichier API")

