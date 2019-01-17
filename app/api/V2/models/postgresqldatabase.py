'''Postgres Database connection model'''
import os
import psycopg2

URL = "dbname='Questioner', host='localhost', port='5432', user='ephy', password='root'"
DB_URL = os.getenv('DATABASE_URL')

def connection(url):
    '''Connectiong to db via psycopg2'''
    conn = psycopg2.connect(url)
    return conn

def init_db():
    '''Connecting to the DB'''
    conn = connection(URL)
    return conn

def create_tables():
    '''Function for creating tables in database'''
    conn = connection(URL)
    cur = conn.cursor()
    queries = tables()

    for query in queries:
        cur.execute(query)
        conn.commit()

def destroy_tables():
    '''Function for dropping tables in tests'''
    users_database = """DROP TABLE IF EXISTS users CASCADE"""
    questions_database = """DROP TABLE IF EXISTS questions CASCADE"""
    meetups_database = """DROP TABLE IF EXISTS meetups CASCADE"""

def tables():
    '''Function to define the tables'''
    users_database = """CREATE TABLE IF NOT EXISTS users (
            user_id serial PRIMARY KEY NOT NULL,
            firstname character varying(50) NOT NULL,
            lastname character varying(50) NOT NULL,
            email character varying(50) NOT NULL,
            password character varying(50) NOT NULL,
            confirm_password character varying(50) NOT NULL,
            role character varying(10) NOT NULL,
            phone_number numeric NOT NULL,
            date_created timestamp with time zone DEFAULT ('now'::date NOT NULL)
            );
        """

    meetups_database = """CREATE TABLE IF NOT EXISTS meetups (
            meetup_id serial PRIMARY KEY NOT NULL,
            Meeetup_title character varying(1000) NOT NULL,
            location character varying(1000) NOT NULL,
            meetup_date character varying(1000) NOT NULL,
            about character varying(1000) NOT NULL,
            date_created timestamp with time zone DEFAULT ('now'::date NOT NULL)
            )"""

    questions_database = """CREATE TABLE IF NOT EXISTS questions (
            question_id serial PRIMARY KEY NOT NULL,
            question character varying(1000) NOT NULL,
            date_created timestamp with time zone DEFAULT ('now'::date NOT NULL)
            )
        """
    comments_database = """CREATE TABLE IF NOT EXISTS comments (
            comment_id serial PRIMARY KEY NOT NULL,
            comment character varying(1000) NOT NULL,
            date_created timestamp with time zone DEFAULT ('now'::date NOT NULL)
            )
        """

    queries = [users_database, meetups_database, comments_database, questions_database]

    return queries
    