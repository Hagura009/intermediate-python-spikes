import requests as rq 
posts_dir= rq.get("https://jsonplaceholder.typicode.com/posts")
user_dir= rq.get("https://jsonplaceholder.typicode.com/users")
photos_dir= rq.get("https://jsonplaceholder.typicode.com/photos")
albums_dir= rq.get("https://jsonplaceholder.typicode.com/albums")
comments_dir= rq.get("https://jsonplaceholder.typicode.com/comments")
#pick up the APIs
posts = posts_dir.json()
users = user_dir.json()
photos = photos_dir.json()
albums = albums_dir.json()
comments = comments_dir.json()
#transform the APIs into json format
admins_ids = ('A9X2K','7Z1V0','K3R8Q','2M9Y4')
count=1
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
                count = 0
                for post in posts:
                    count += 1
                    print(f"ID: {post['id']}, Title: {post['title']}")
                    if count >= 10:
                        break
         elif user_choice == '02':
                print("Viewing comments:")
                count = 0
                for comment in comments:
                    count += 1
                    print(f"ID: {comment['id']}, Name: {comment['name']}")
                    if count >= 10:
                        break
         elif user_choice == '03':
                print("Viewing public photos:")
                count = 0
                for photo in photos:
                    count += 1
                    print(f"ID: {photo['id']}, Title: {photo['title']}")
                    if count >= 30:
                        break
         elif user_choice == '04':
                print("Viewing recent photos:")
                count = 0
                for photo in photos:
                    count += 1
                    print(f"ID: {photo['id']}, Title: {photo['title']}")
                    if count >= 10:
                        break
         elif user_choice == '05':
                print("Viewing recent albums:")
                count = 0
                for album in albums:
                    count += 1
                    print(f"ID: {album['id']}, Title: {album['title']}")
                    if count >= 10:
                        break
         elif user_choice == '06':
                print("Viewing public albums:")
                count = 0
                for album in albums:
                    count += 1
                    print(f"ID: {album['id']}, Title: {album['title']}")
                    if count >= 30:
                        break
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
                while True:
                    page = input("Enter page number (1-10) or 'exit' to go back: ")
                    if page.lower() == 'exit':
                        break
                    try:
                        page_num = int(page)
                        if 1 <= page_num <= 10:
                            start_index = (page_num - 1) * 10
                            end_index = start_index + 10
                            for post in posts[start_index:end_index]:
                                print(f"ID: {post['id']}, Title: {post['title']}")
                    except ValueError:
                        print("Invalid input. Please enter a valid page number or 'exit'.")
         elif admin_choice == '020':
                print("Viewing paginated comments:")
                while True:
                    page = input("Enter page number (1-10) or 'exit' to go back: ")
                    if page.lower() == 'exit':
                        break
                    try:
                        page_num = int(page)
                        if 1 <= page_num <= 10:
                            start_index = (page_num - 1) * 10
                            end_index = start_index + 10
                            for comment in comments[start_index:end_index]:
                                print(f"ID: {comment['id']}, Name: {comment['name']}, Email: {comment['email']}")
                    except ValueError:
                        print("Invalid input. Please enter a valid page number or 'exit'.")
         elif admin_choice == '030':
                print("Viewing paginated albums:")
                while True:
                    page = input("Enter page number (1-10) or 'exit' to go back: ")
                    if page.lower() == 'exit':
                        break
                    try:
                        page_num = int(page)
                        if 1 <= page_num <= 10:
                            start_index = (page_num - 1) * 10
                            end_index = start_index + 10
                            for album in albums[start_index:end_index]:
                                print(f"ID: {album['id']}, Title: {album['title']}")
                    except ValueError:
                        print("Invalid input. Please enter a valid page number or 'exit'.")
         elif admin_choice == '040':
                print("Viewing paginated photos:")
                while True:
                    page = input("Enter page number (1-10) or 'exit' to go back: ")
                    if page.lower() == 'exit':
                        break
                    try:
                        page_num = int(page)
                        if 1 <= page_num <= 10:
                            start_index = (page_num - 1) * 10
                            end_index = start_index + 10
                            for photo in photos[start_index:end_index]:
                                print(f"ID: {photo['id']}, Title: {photo['title']}")
                        else:
                            print("Invalid page number. Please enter a number between 1 and 10.")
                    except ValueError:
                        print("Invalid input. Please enter a valid page number or 'exit'.")
         
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
