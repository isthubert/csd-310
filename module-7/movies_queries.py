
import mysql.connector
from mysql.connector import errorcode

import dotenv
from dotenv import dotenv_values

secrets = dotenv_values(".env")


config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

try:

    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # Select all fields from studio table

    print("\n--- DISPLAYING Studio RECORDS ---")

    cursor.execute("SELECT studio_id, studio_name FROM studio")

    studios = cursor.fetchall()

    for studio_id, studio_name in studios:
        print(f"\nStudio ID: {studio_id} \nStudio Name: {studio_name}")

    # Select all fields from genre table

    print("\n--- DISPLAYING Genre RECORDS ---")

    cursor.execute("SELECT genre_id, genre_name FROM genre")

    genres = cursor.fetchall()

    for genre_id, genre_name in genres:
        print(f"\nGenre ID: {genre_id} \nGenre Name: {genre_name}")

    # Select movie names with runtime < 120 minutes

    print("\n--- DISPLAYING Short Film RECORDS ---")

    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")

    short_movies = cursor.fetchall()

    for film_name, film_runtime in short_movies:
        print(f"\nFilm Name: {film_name} \nFilm Runtime: {film_runtime} minutes")

    # List film names and directors in order

    print("\n--- DISPLAYING Director RECORDS in Order ---")

    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")

    films_and_director = cursor.fetchall()

    for film_name, film_director in films_and_director:
        print(f"\nFilm Name: {film_name} \nFilm Director: {film_director}")

    cursor.close()


except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)



finally:

    db.close()