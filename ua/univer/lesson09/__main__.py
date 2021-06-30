import sqlite3
import mysql.connector


class Artist:
    def __init__(self, artist_title, artist_name):
        self.artist_id = artist_title
        self.artist_name = artist_name

    def __str__(self)->str:
        return f"{self.artist_id}, {self.artist_name}"

    def __repr__(self)->str:
        return f"Artist({self.__str__()})"


def get_album_by_author(author_name):
    with sqlite3.connect("Chinook_Sqlite.sqlite") as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
        select Album.Title, Artist.Name 
        from Album join Artist 
        on Album.ArtistId = Artist.ArtistId
        where Artist.Name="{author_name}"
        """)
        result_list = cursor.fetchall()
        artists_list=[]
        for result in result_list:
            artists_list.append(Artist(result[0], result[1]))
    return artists_list


#def get_album_by_author1(author_name):
#    with mysql.connector.connect(
#        host="127.0.0.1",
#        database='chinook',
#        user='root',
#        password='root',
#   ) as conn

def insert_author(author_id, author_name):
    with sqlite3.connect("Chinook_Sqlite.sqlite") as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
        insert into Artist values({author_id}, '{author_name}')
        """)
        conn.commit()
        cursor.execute(f"""
                select count(*) from Artist 
                """)
        return cursor.fetchall()


def update_author(author_id, author_name):
    with sqlite3.connect("Chinook_Sqlite.sqlite") as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
        update Artist set Name = '{author_name}' where ArtistId={author_id}
        """)
        conn.commit()
        cursor.execute(f"""
                select count(*) from Artist 
                """)
        return cursor.fetchall()


def delete_author(author_id):
    with sqlite3.connect("Chinook_Sqlite.sqlite") as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
        delete from Artist where ArtistId={author_id}
        """)
        conn.commit()
        cursor.execute(f"""
                select count(*) from Artist 
                """)
        return cursor.fetchall()


if __name__ == '__main__':
    result_list = get_album_by_author("Accept")
    print(result_list)
    for row in result_list:
        print(row)
