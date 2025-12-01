# Isaac St Hubert Module 8.2 11/30/2025
# This program inserts, updates, and deletes data from the movies database
# Sources: https://www.w3schools.com/python/python_mysql_insert.asp

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

def show_films(cursor, title):
	cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

	films = cursor.fetchall ()

	print("\n -- {} --".format(title))

	for film in films:
		print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

try:

    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    show_films(cursor, "DISPLAYING FILMS")

    # This process inserts a new film into the film table

    insert = "INSERT INTO film (film_name, film_director, genre_id, studio_id, film_releaseDate, film_runtime) VALUES (%s, %s, %s, %s, %s, %s)"
    new_film = ("Planet of the Apes", "Franklin J. Schaffner", 2, 1, 1968, 112)
    cursor.execute(insert, new_film)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # This process updates and changes the film genre for Alien

    update = "UPDATE film SET genre_id = %s WHERE film_name = %s"
    updated_film = (1, "Alien")
    cursor.execute(update, updated_film)
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    # This process deletes the Gladiator film from the database

    delete = "DELETE FROM film WHERE film_name = %s"
    cursor.execute(delete, ("Gladiator",))
    db.commit()
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")



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