# mini-API-de-gestion-de-bibliotheque

## Motivations
Cette  API permettant de gérer les livres d’une bibliothèque.
## Getting Started

### Installing Dependencies

#### Python 3.9.7
#### pip 20.3.4 from /usr/lib/python3/dist-packages/pip (python 3.9)

Si vous n'avez pas python installé, merci de suivre cet URL pour l'installer [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

Vous devez installer le package dotenv en utilisant la commande pip install python-dotenv 

#### PIP Dependencies

Exécuter la commande ci dessous pour installer les dépendences
```bash
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

```

## Running the server

From within the `Projet_Python` directory first ensure you are working using your created virtual environment.

To run the server on Linux or Mac, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
To run the server on Windows, execute:

```bash
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## API REFERENCE

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

## Error Handling
Errors are retourned as JSON objects in the following format:
{
    "success":False
    "error": 404
    "message":"Not found"
}

The API will return four error types when requests fail:
. 404: Not found

## Endpoints
. ## GET/categories

    GENERAL: cet endpoint permet de récupérer la liste des categories 
    
        
    SAMPLE: curl -i http://localhost:5000/categories

    {
        "Total_categorie": 6,
        "categorie": [
            {
            "id": 1,
            "libelle": "conte"
            },
            {
            "id": 2,
            "libelle": "science"
            },
            {
            "id": 3,
            "libelle": "harlequin"
            },
            {
            "id": 4,
            "libelle": "fiction"
            },
            {
            "id": 5,
            "libelle": "policier"
            },
            {
            "id": 7,
            "libelle": "aventure"
            }
        ],
        "success": true
    
    }

```
. ## POST/categorie

    GENERAL: cet endpoint permet d'ajouter une categorie

    
        
    SAMPLE:  curl -i -H "Content-Type: application/json" -X POST -d '{"libelle":"poetique"}' http://127.0.0.1:5000/categorie
    {
  "Total_categorie": 7,
  "categorie": [
    {
      "id": 1,
      "libelle": "conte"
    },
    {
      "id": 2,
      "libelle": "science"
    },
    {
      "id": 3,
      "libelle": "harlequin"
    },
    {
      "id": 4,
      "libelle": "fiction"
    },
    {
      "id": 5,
      "libelle": "policier"
    },
    {
      "id": 7,
      "libelle": "aventure"
    },
    {
      "id": 8,
      "libelle": "poetique"
    }
  ],
  "success": true
}
'''

. ## DELETE/categorie/id

    GENERAL: Cet endpoint permet de supprimer une categorie

        SAMPLE: curl -X DELETE http://localhost:5000/categorie/2

        Les resulats de cette requete se présentent comme suit
```
    "categorie": {
    "id": 2,
    "libelle": "science"
    },
    "success": true,
    "total_categorie": 6
    }

```
. ##PATCH/categorie/id

  GENERAL: Cet endpoint permet de modifier une categorie
      
  SAMPLE.....For Patch
  ``` curl -i -H "Content-Type: application/json" -X PATCH -d '{"libelle":"aventure"}' http://127.0.0.1:5000/categorie/4
  ```
    {
    "categorie": {
        "id": 4,
        "libelle": "science_fiction"
    },
    "successs": true,
    "update_id": 4
    }

  ```
     

. ## /categorie/id

    GENERAL:   Cet endpoint permet d'affichier une categorie

    SAMPLE.....For Search:
    ```
    curl -i http://localhost:5000/categorie/3
    ```
        {
            "categorie": {
                "id": 3,
                "libelle": "harlequin"
            },
            "selected_id": 3,
            "success": true
        }

 
``` 
. ## GET/livres

    GENERAL: cet endpoint permet de récupérer la liste des livres 
    
        
    SAMPLE: curl -i http://localhost:5000/livres

    {
  "Livres": [
    {
      "auteur": "Alain Bombard",
      "categorie": "aventure",
      "date_publication": "Sat, 20 Feb 1999 00:00:00 GMT",
      "editeur": "L richard",
      "id": 1,
      "isbn": 53,
      "titre": "Naufrage volontaire"
    },
    {
      "auteur": "Isabella Brid",
      "categorie": "aventure",
      "date_publication": "Sun, 10 Aug 1879 00:00:00 GMT",
      "editeur": "T smith",
      "id": 2,
      "isbn": 25,
      "titre": "Une anglaise au far west"
    },
    {
      "auteur": "Jack London",
      "categorie": "aventure",
      "date_publication": "Thu, 29 Aug 1907 00:00:00 GMT",
      "editeur": "Alfred Freddy",
      "id": 3,
      "isbn": 2285,
      "titre": "La route ou les vagabonds du rail"
    }
  ],
  "success": true,
  "total_livres": 3
}


```
. ## POST/categorie

    GENERAL: cet endpoint permet d'ajouter un livre

    
        
    SAMPLE:   curl -i -H "Content-Type: application/json" -X POST -d '{"isbn":"85","titre":"Les contenplation","date":"1907-08-29","auteur":"Vitor Hugo","editeur":"","categorie":"8"}' http://127.0.0.1:5000/livre
   {
  "Livres": [
    {
      "auteur": "Alain Bombard",
      "categorie": "aventure",
      "date_publication": "Sat, 20 Feb 1999 00:00:00 GMT",
      "editeur": "L richard",
      "id": 1,
      "isbn": 53,
      "titre": "Naufrage volontaire"
    },
    {
      "auteur": "Isabella Brid",
      "categorie": "aventure",
      "date_publication": "Sun, 10 Aug 1879 00:00:00 GMT",
      "editeur": "T smith",
      "id": 2,
      "isbn": 25,
      "titre": "Une anglaise au far west"
    },
    {
      "auteur": "Jack London",
      "categorie": "aventure",
      "date_publication": "Thu, 29 Aug 1907 00:00:00 GMT",
      "editeur": "Alfred Freddy",
      "id": 3,
      "isbn": 2285,
      "titre": "La route ou les vagabonds du rail"
    },
    {
      "auteur": "Vitor Hugo",
      "categorie": "poetique",
      "date_publication": "Thu, 29 Aug 1907 00:00:00 GMT",
      "editeur": "",
      "id": 5,
      "isbn": 85,
      "titre": "Les contenplation"
    }
  ],
  "success": true,
  "total_livres": 4
}

'''

. ## DELETE/livre/id

    GENERAL: Cet endpoint permet de supprimer un livre

        SAMPLE: curl -X DELETE http://localhost:5000/livre/2

        Les resulats de cette requete se présentent comme suit
```
     "livre": {
        "auteur": "Isabella Brid",
        "categorie": "aventure",
        "date_publication": "Sun, 10 Aug 1879 00:00:00 GMT",
        "editeur": "T smith",
        "id": 2,
        "isbn": 25,
        "titre": "Une anglaise au far west"
    },
    "success": true,
    "total_livre": 3
    }


```
. ##PATCH/livre/id

  GENERAL: Cet endpoint permet de modifier un livre
      
  SAMPLE.....For Patch
  ```  curl -i -H "Content-Type: application/json" -X PATCH -d '{"isbn":"85","titre":"Les contenplation","date":"1907-08-29","auteur":"Vitor Hugo","editeur":"H Louis","categorie":"8"}' http://127.0.0.1:5000/livre/5
  ```
   {
    "livre": {
        "auteur": "Vitor Hugo",
        "categorie": "poetique",
        "date_publication": "Thu, 29 Aug 1907 00:00:00 GMT",
        "editeur": "H Louis",
        "id": 5,
        "isbn": 85,
        "titre": "Les contenplation"
    },
    "successs": true,
    "update_id": 5
    }

  ```
     

. ## /livre/id

    GENERAL:   Cet endpoint permet d'affichier un livre

    SAMPLE.....For Search:
    ```
    curl -i http://localhost:5000/livre/3
    ```
    {
    "livre": {
        "auteur": "Jack London",
        "categorie": "aventure",
        "date_publication": "Thu, 29 Aug 1907 00:00:00 GMT",
        "editeur": "Alfred Freddy",
        "id": 3,
        "isbn": 2285,
        "titre": "La route ou les vagabonds du rail"
    },
    "selected_id": 3,
    "success": true
    }

 '''   
. ## /categorie/id/livres

    GENERAL:   Cet endpoint permet d'affichier les livres d'une categorie

    SAMPLE.....For Search:
    ```
    curl -i http://localhost:5000/categorie/7/livres
    ```
    {
    "categorie": "aventure",
    "livres": [
        "Naufrage volontaire",
        "La route ou les vagabonds du rail"
    ],
    "success": true,
    "total_livre": 2
    }


 '''     
