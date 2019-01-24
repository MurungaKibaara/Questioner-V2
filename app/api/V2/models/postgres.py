'''Postgres Database connection model'''
import os
import psycopg2
from flask import jsonify

DB_URL = os.getenv('DATABASE')


def init_db():
    '''Connecting to the DB'''
    conn = psycopg2.connect(DB_URL)
    return conn


def create_tables():
    '''Function for creating tables in database'''
    conn = init_db()
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

    queries = [users_database, questions_database, meetups_database]

    conn = init_db()
    cur = conn.cursor()

    for query in queries:
        cur.execute(query)
        conn.commit()

    try:

        admin_query = """INSERT INTO users (firstname, lastname, email,
        password, confirm_password, imagefile, role, phonenumber) VALUES
        (Murunga, Kibaara, murungakibaara@protonmail.com, admin_secret_password, admin_secret_password
        ,Admin_dp.jpg ,Admin,0719562555;"""

        cur.execute(admin_query)
        cur.commit()
    except (psycopg2.Error) as error:
        return jsonify(error)


def tables():
    '''Function to define the tables'''
    users_db = """CREATE TABLE IF NOT EXISTS users(
            user_id serial PRIMARY KEY NOT NULL,
            firstname character varying(1000) NOT NULL,
            lastname character varying(1000) NOT NULL,
            email character varying(1000) NOT NULL,
            password character varying(1000) NOT NULL,
            confirm_password character varying(1000) NOT NULL,
            imagefile character varying(1000) NOT NULL,
            date_created TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT TIMESTAMP 'epoch');
            """

    meetups_db = """CREATE TABLE IF NOT EXISTS meetups (
            meetup_id serial PRIMARY KEY NOT NULL,
            Meeetup_title character varying(1000) NOT NULL,
            location character varying(1000) NOT NULL,
            meetup_date character varying(1000) NOT NULL,
            about character varying(1000) NOT NULL,
            date_created TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT TIMESTAMP 'epoch');"""   

    questions_db = """CREATE TABLE IF NOT EXISTS questions (
            question_id serial PRIMARY KEY NOT NULL,
            user_id integer NULL,
            votes integer NULL,
            question character varying(1000) NOT NULL,
            date_created TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT TIMESTAMP 'epoch');"""

    comments_db = """CREATE TABLE IF NOT EXISTS comments (
            comment_id serial PRIMARY KEY NOT NULL,
            user_id integer NOT NULL,
            comment character varying(1000) NOT NULL,
            date_created TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT TIMESTAMP 'epoch');"""

    queries = [users_db, meetups_db, comments_db, questions_db]

    return queries
