

# Flash-Cards

#### 14/07/2020
#### By **Jorim Midumbi Okong'o Opondo, Rose Kairu, Nyota Mwangi, Wanjiku Karanja**

## Description
An application to help people learn via flashcards, that has these goals:

- Registered users can create multiple decks of flashcards, each with a prompt or question and an answer.
- Registered users can quiz themselves on a deck.
- Success and failure for each card is recorded.

You can view the site at:[Heroku]()


## User Stories
As a user, I would like to:

* A user must be authenticated to see his flashcards.
* A user's flash card can contain a title with some notes.
* Flashcards should be organized according to subjects/courses.
* A user can delete or update a flash card he has created.
* A user should see when the flash card was created and when it was last updated.
  

  
## Setup and Installation  
To get the project ....... 
  
##### Cloning the repository:  
 ```bash 
 https://github.com/JORIM1981/Flash-Cards.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Flash-Cards pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv venv - source venv/bin/activate 
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations pictures 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`. 


## Technology used

* [Python3.8](https://www.python.org/)
* [Django3.0.7](https://docs.djangoproject.com/en/2.2/)
* [Heroku](https://heroku.com)


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email us at [okongo.midumbi.opondo@gmail.com, rosekairu@gmail.com, ciiku92@gmail.com, nyota.benjamin@gmail.com]

## License:

- _MIT License:_[LICENSE MIT](./LICENSE)

- Copyright (c) 2020 **Jorim Midumbi Okongo Opondo**


