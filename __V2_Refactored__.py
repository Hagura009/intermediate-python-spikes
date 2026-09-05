import math
import requests as rq 

# Importación de APIs y transformación a JSON
posts = rq.get("https://jsonplaceholder.typicode.com/posts").json()
users = rq.get("https://jsonplaceholder.typicode.com/users").json()
photos = rq.get("https://jsonplaceholder.typicode.com/photos").json()
albums = rq.get("https://jsonplaceholder.typicode.com/albums").json()
comments = rq.get("https://jsonplaceholder.typicode.com/comments").json()

admins_ids = ('A9X2K', '7Z1V0', 'K3R8Q', '2M9Y4')

# Función universal auxiliar para paginación
def paginar_universal(lista_datos, campos_mostrar):
    while True:
        page = input("Enter page number (1-10) or 'exit' to go back: ")
        if page.lower() == 'exit':
            break
        try:
            page_num = int(page)
            if 1 <= page_num <= 10:
                start_index = (page_num - 1) * 10
                end_index = start_index + 10
                for item in lista_datos[start_index:end_index]:
                    linea = ", ".join([f"{label}: {item[key]}" for key, label in campos_mostrar])
                    print(linea)
            else:
                print("Invalid page number. Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid page number or 'exit'.")

def user_is_true():
    while True:
        print("Welcome, user! You have limited access to the system.\n Funciones de usuario activadas \n Puedes acceder a informacion basica (solo posts y comentarios) y puedes acceder a datos mas recientes de la API de jsonplaceholder, los mas antiguos estan restringidos para usuarios normales.")
        print('''Funciones de usuario disponibles:
         00. Exit
         01. View posts
         02. View comments
         03. View public photos
         04. View recent photos
         05. View recent albums
         06. View public albums''')
        user_choice = input("Enter your choice (00-06): ")
        if user_choice == '00':
            print("Exiting user mode.")
            break
        elif user_choice == '01':
            print("Viewing posts:")
            for post in posts[:10]:
                print(f"ID: {post['id']}, Title: {post['title']}")
        elif user_choice == '02':
            print("Viewing comments:")
            for comment in comments[:10]:
                print(f"ID: {comment['id']}, Name: {comment['name']}")
        elif user_choice == '03':
            print("Viewing public photos:")
            for photo in photos[:30]:
                print(f"ID: {photo['id']}, Title: {photo['title']}")
        elif user_choice == '04':
            print("Viewing recent photos:")
            for photo in photos[:10]:
                print(f"ID: {photo['id']}, Title: {photo['title']}")
        elif user_choice == '05':
            print("Viewing recent albums:")
            for album in albums[:10]:
                print(f"ID: {album['id']}, Title: {album['title']}")
        elif user_choice == '06':
            print("Viewing public albums:")
            for album in albums[:30]:
                print(f"ID: {album['id']}, Title: {album['title']}")

def admin_is_true():
    while True:
        print("Welcome, admin! You have full access to the system.\n Funciones de administrador activadas \n Puedes acceder a informacion sensible (como nombres de usuarios) y puedes acceder a datos mas antiguos de la API de jsonplaceholder, restringidos para usuarios normales.")
        print('''Funciones de administrador disponibles:

     00. Exit

     01. View all users

     02. View all posts

     03. View all comments

     04. View all albums

     05. View all photos

     010. View paginated posts

     020. View paginated comments

     030. View paginated albums

     040. View paginated photos
     Para acceder a estas funciones, ingresa el número correspondiente a la opción deseada

     Example: 01 para ver todos los usuarios, 02 para ver todos los posts, etc.''')
        admin_choice = input("Enter your choice (00-05): ")
        if admin_choice == '00':
            print("Exiting admin mode.")
            break
        elif admin_choice == '01':
            print("Viewing all users:")
            for user in users:
                print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
        elif admin_choice == '02':
            print("Viewing all posts:")
            for post in posts:
                print(f"ID: {post['id']}, Title: {post['title']}")
        elif admin_choice == '03':
            print("Viewing all comments:")
            for comment in comments:
                print(f"ID: {comment['id']}, Name: {comment['name']}, Email: {comment['email']}")
        elif admin_choice == '04':
            print("Viewing all albums:")
            for album in albums:
                print(f"ID: {album['id']}, Title: {album['title']}")
        elif admin_choice == '05':
            print("Viewing all photos:")
            for photo in photos:
                print(f"ID: {photo['id']}, Title: {photo['title']}")
        elif admin_choice == '010':
            print("Viewing paginated posts:")
            paginar_universal(posts, [('id', 'ID'), ('title', 'Title')])
        elif admin_choice == '020':
            print("Viewing paginated comments:")
            paginar_universal(comments, [('id', 'ID'), ('name', 'Name'), ('email', 'Email')])
        elif admin_choice == '030':
            print("Viewing paginated albums:")
            paginar_universal(albums, [('id', 'ID'), ('title', 'Title')])
        elif admin_choice == '040':
            print("Viewing paginated photos:")
            paginar_universal(photos, [('id', 'ID'), ('title', 'Title')])

def verification_admin():
    try:
        ver = input("Enter admin identification code: ").upper()
        if ver in admins_ids:
            print("Access granted.")
            admin_is_true()
        else:
            print("Access denied. Invalid code.")
    except Exception as e:
        print(f"An error occurred: {e}")

def UserOrAdmin():
    user_type = input("Are you a user or an admin? (Enter 'user' or 'admin'): ").lower()
    if user_type == 'admin':
        verification_admin()
    elif user_type == 'user':
        print("Welcome, user! You have limited access to the system.")
        user_is_true()
    else:
        print("Invalid input. Please enter 'user' or 'admin'.")

UserOrAdmin()