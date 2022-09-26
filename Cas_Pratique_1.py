import requests
from bs4 import BeautifulSoup

### Exemple de keyword et boolean à vous de le changer. WARNING boolean ne peut etre que True ou False ###

keyword = "salut"
boolean = "true"

### Correspond à ma route pour getTweet ###

api = "http://127.0.0.1:5000/search=" + keyword + "/media=" + boolean

response = requests.get(api)

### Si ma réponse me renvoit 200 elle est donc ok ###

if response.ok :
    
    ### Permet de parser mon response.text ###
    soup = BeautifulSoup(response.text, "lxml")
    ### Permet de trouver et extraire mon texte à l'aide des balises ###
    text_of_tweet = soup.find("p").getText()

    print (text_of_tweet)

else :
    print ("Tu as oublié de de Run ton fichier API")

