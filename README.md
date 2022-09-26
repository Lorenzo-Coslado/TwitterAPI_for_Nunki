# TwitterAPI_for_Nunki

# Lorenzo Coslado

# Langage de Programmation

- Python

# Sommaire

1. Téléchargement du dossier Git
2. Lancement du fichier API
3. Test de L'API
4. Cas pratique numéro 1 (getTweet / keyword & boolean)
5. Cas pratique numéro 2 (getUser / userId)
6. Cas pratique BONUS avec postgreSQL

# Pip install

- pip install Flask
- pip install tweepy
- pip install requests
- pip install bs4
- pip install lxml

# 1. Téléchargement du dossier Git

![Download ZIP](https://user-images.githubusercontent.com/93212434/192364689-7d70a301-b4cc-4d2b-ad23-bbfbdbd18cbc.png)

![Extraire le Dossier](https://user-images.githubusercontent.com/93212434/192365262-188d0514-5896-400a-88bf-778c43c8400b.png)



# 2. Lancement du fichier API

![Ouvrir avec son IDE](https://user-images.githubusercontent.com/93212434/192365899-d0d2241c-dc54-4b83-9f8a-f3f794bb7e8e.png)

![censuré](https://user-images.githubusercontent.com/93212434/192367814-947030ac-bdcf-4825-91db-7a02aca6aef3.png)

# 3. Test de L'API

- Ouvrez deux nouveaux onglets dans votre navigateur

- http://127.0.0.1:5000/user=*****
- http://127.0.0.1:5000/search=*****/media=*****

- Remplacez les ***** par votre user_id, keyword, boolean
- WARNING : boolean ne peut être que "True" ou "False"

![Modifier 103770784 change le user_id](https://user-images.githubusercontent.com/93212434/192371616-f0c4c7b0-28b7-42a5-959c-e2d9584f44b3.png)

![Modifier speed change le keyword](https://user-images.githubusercontent.com/93212434/192371682-1742e689-058e-4503-adf4-328e7a88f304.png)

- La première page vous renvoit les user_info de votre user-id (http://127.0.0.1:5000/user=*****)
- La deuxième page vous renvoit le texte du tweet le plus récent comprenant votre keyword (http://127.0.0.1:5000/search=*****/media=*****)

# 4. Cas pratique numéro 1 (getTweet / keyword & boolean)

- WARNING !!!!  Le premier fichier doit toujours Run pendant la durée des Cas pratique

- Lancez dans votre IDE le fichier Cas_Pratique_1.py
- Changez votre keyword et votre boolean

![Vous devez changer salut les gens et False (1)](https://user-images.githubusercontent.com/93212434/192380782-ff27d1c6-5c64-49bc-ae11-d5e504e71a3c.png)

- Lancez dans votre terminal python Cas_Pratique_1.py
- On peut voir que tout fonctionne correctement, on nous a bien print notre text_of_tweet

<img width="1280" alt="10" src="https://user-images.githubusercontent.com/93212434/192380976-dd812c03-fa01-4609-872d-77cf60763135.png">


# 5. Cas pratique numéro 2 (getUser / userId)

- Lancez dans votre IDE le fichier Cas_Pratique_2.py
- Changez votre userID

![Vous devez changer 103770784](https://user-images.githubusercontent.com/93212434/192375834-41dba2b6-2072-4c79-a104-4f3990cabff2.png)

- Lancez dans votre terminal python Cas_Pratique_2.py
- On peut voir que tout fonctionne correctement, on nous a bien print notre user_info

<img width="1280" alt="8" src="https://user-images.githubusercontent.com/93212434/192375866-e184a484-c896-4da1-8e9a-f3147631a094.png">

# 6. Cas pratique BONUS avec postgreSQL

- Lancez dans votre IDE le fichier Cas_Pratique_BONUS_postgreSQL.py
- 
