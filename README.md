# Questioner-V2

## Badges
[![Build Status](https://travis-ci.com/MurungaKibaara/Questioner-V2.svg?branch=develop)](https://travis-ci.com/MurungaKibaara/Questioner-V2)
[![Coverage Status](https://coveralls.io/repos/github/MurungaKibaara/Questioner-V2/badge.svg?branch=develop)](https://coveralls.io/github/MurungaKibaara/Questioner-V2?branch=develop)


## Questioner
    Questioner is an application that crowd-sources questions for a meetup. Questioner helps the meetup organizer prioritize questions to be answered. Other users can vote on asked questions and they bubble to the top or bottom of the log

## Basic Features
    An API with endpoints where
    Admins can create a meetup.
    Users can create a question in a meetup.
    Users can get a specific meetup record.
    Users can get all meetup records.
    Users can upvote or downvote a question.
    Users can RSVP for a meetup.


## QUESTIONER API Version 2

---

## What is required

    - Python3
    - Flask
    - Postman
    - Pytest
    - Git
    - Python3 pip
    - PostgreSQL database 

## How to get started

1. Clone the repo

    > `https://github.com/MurungaKibaara/Questioner/`

2) Checkout delelop branch

    > `git checkout develop`

## First install

1. python3

    > `sudo apt-get install python3`

2. install python3 pip

    > `sudo apt-get install python3-pip`

3. install vitual environment

    > `pip3 install virtualenv`

4. checkout develop branch

    > `git checkout develop`

5. create the virtual environment

    > `virtualenv env`

6. Activate the vitualenv in the parent directory of your **"env"**

    > `source env/bin/activate`

7. Install requirement

    > `pip install -r requirements.txt`

8. Run the app

    > `python3 run.py`
    
9. Testing 

    > `python3 -m pytest`


## Endpoints to use on postman

    | Endpoints                                        |               Functions                |
    | -------------------------------------------------| :------------------------------------: |
    | POST/api/v1auth/registration                     |            create new user             |
    | POST/api/v1auth/login                            |              login user                |
    | POST/api/v1/meetups                              |             create meetups             |
    | GET/api/v1/meetups/all                           |            get all meetups             |
    | GET/api/v1/meetups/all&lt;meetup_id&gt;/         |         get a specific meetups         |
    | POST/api/v1/questions                            |       post question on meetups         |
    | GET/api/v1/questions/all                         | view all questions for given meetups   |
    | POST/api/v1/meetups/all/&lt;id&gt;/rsvp          |     respond to meetups invitation      |
    | PATCH/api/v1/questions/&lt;question_id&gt;       |           upvote a question            |
    | POST/api/v1/questions/all/&lt;question_id&gt;/   |        view a specific question        |


## Authors

    Murunga Kibaara

## Acknowledgements

    1. Andela
    
    2. #Teamroot teammates
