import requests
from bs4 import BeautifulSoup

### Exemple de user_id à vous de le changer ###

userId = "103770784"

### Correspond à ma route pour getUser ###

api = "http://127.0.0.1:5000/user=" + userId

response = requests.get(api)

### Si ma réponse me renvoit 200 elle est donc ok ###

if response.ok :

    ### Permet de parser mon response.text ###
    soup = BeautifulSoup(response.text, "lxml")
    ### Permet de trouver et extraire mon texte à l'aide des balises ###
    user_info = soup.find("p").getText()

    print (user_info)

else :
  
    print ("Tu as oublié de de Run ton fichier API") 
