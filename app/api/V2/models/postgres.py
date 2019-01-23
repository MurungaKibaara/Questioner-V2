'''Postgres Database connection model'''
import os
import psycopg2
URL = os.getenv("DATABASE")

class Questioner:
    '''DB connection'''
    @classmethod
    def connect_db(cls, url):
        '''Connect to database'''
        cls.connection = psycopg2.connect(url)

    @classmethod
    def init_db(cls):
        '''Return the connection'''
        return cls.connection

def create_tables():
    '''Function for creating tables'''

    queries = tables()

    for query in queries:
        cur = Questioner.init_db().cursor()
        cur.execute(query)
        Questioner.init_db().commit()

#     def drop_tables(self):
#         '''Function for dropping tables in tests'''
#         users_db = """DROP TABLE IF EXISTS users CASCADE"""
#         questions_db = """DROP TABLE IF EXISTS questions CASCADE"""
#         meetups_db = """DROP TABLE IF EXISTS meetups CASCADE"""

def tables():

    '''Function to define the tables'''
    users_db = """CREATE TABLE IF NOT EXISTS users(
        user_id serial PRIMARY KEY NOT NULL,
        firstname character varying(1000) NOT NULL,
        lastname character varying(1000) NOT NULL,
        email character varying(1000) NOT NULL,
        password character varying(1000) NOT NULL,
        role character varying(1000) NOT NULL,
        phonenumber character varying(1000) NOT NULL,
        confirm_password character varying(1000) NOT NULL,
        imagefile character varying(1000) NOT NULL,
        date_created TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT TIMESTAMP 'epoch');
        """

    meetups_db = """CREATE TABLE IF NOT EXISTS meetups (
                meetup_id serial PRIMARY KEY NOT NULL,
                Meetup_title character varying(1000) NOT NULL,
                Meetup_image character varying(1000) NOT NULL,
                location character varying(1000) NOT NULL,
                meetup_date character varying(1000) NOT NULL,
                about character varying(1000) NOT NULL,
                date_created TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT TIMESTAMP 'epoch');"""

    questions_db = """CREATE TABLE IF NOT EXISTS questions (
                        question_id serial PRIMARY KEY NOT NULL,
                        question character varying(1000) NOT NULL,
                        date_created TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT TIMESTAMP 'epoch')"""

    comments_db = """CREATE TABLE IF NOT EXISTS comments (
                        comment_id serial PRIMARY KEY NOT NULL,
                        comment character varying(1000) NOT NULL,
                        date_created TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT TIMESTAMP 'epoch')"""

    queries = [users_db, meetups_db, comments_db, questions_db]

    return queries
