'''Postgres Database connection model'''
import psycopg2
from psycopg2.extras import DictCursor

class Questioner:
    '''DB connection'''
    @classmethod
    def connect_db(cls, url):
        '''Connect to the database'''
        cls.conn = psycopg2.connect(url)
    @classmethod
    def init_db(cls):
        '''Return connection'''
        return cls.conn

def destroy_tables():
    '''Function for dropping tables in tests'''
    users_db = """DROP TABLE IF EXISTS users CASCADE"""
    questions_db = """DROP TABLE IF EXISTS questions CASCADE"""
    meetups_db = """DROP TABLE IF EXISTS meetups CASCADE"""

    queries = [users_db, questions_db, meetups_db]

    conn = Questioner.init_db()
    cur = conn.cursor(cursor_factory=DictCursor)

    for query in queries:
        cur.execute(query)
        conn.commit()


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
            date_created TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT TIMESTAMP 'epoch');"""

    comments_db = """CREATE TABLE IF NOT EXISTS comments (
            comment_id serial PRIMARY KEY NOT NULL,
            comment character varying(1000) NOT NULL,
            date_created TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT TIMESTAMP 'epoch');"""

    queries = [users_db, meetups_db, comments_db, questions_db]

    return queries
