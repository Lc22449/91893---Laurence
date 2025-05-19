import easygui
movies = {
    "M001": {
        "title": "Inception",
        "genre": "Sci-Fi",
        "duration": 148,
        "seats": 85,
        "rating": 6,
        "reviews": {
            1: {"name": "Adam", "rating": 6, "comment": "Amazing plot!"},
        },
        "price": 12,
    },
    "M002": {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "duration": 169,
        "seats": 110,
        "rating": 4.6,
        "reviews": {
            1: {"name": "Jane", "rating": 4.6, "comment": "Mind-expanding!"},
        },
        "price": 13,
    },
    "M003": {
        "title": "Joker",
        "genre": "Drama",
        "duration": 122,
        "seats": 100,
        "rating": 8.0,
        "reviews": {
            1: {"name": "Jason", "rating": 8.0, "comment": "Dark and intense."},
        },
        "price": 12,
    },
}
 
users = {
    "admin": {"password": "admin"},
    "Billy": {"password": "billy", "balance": 1250.50},
    "Bobby": {"password": "bobby", "balance": 820.00},
    "Bo": {"password": "bo", "balance": 312.75},
}

def search_movies():
    Movie_name = input("insert movie name here: ")
    for item in movies:
        if movies[item]["title"] == Movie_name:
            for key, value in movies[item].items():
                print(f'{key}: {value}\n')
    return item

def edit_movies():
    print("Please input the movie you would like to edit")
    movie_id = search_movies()
    movie_key = input("Input chosen key: ")
    for key in movies[movie_id]:
        if movie_key == key:
            movies[movie_id][key] = input("Change your key: ")



def buy_tickets():
    pass

x = 1

while x == 1:
    username = easygui.msgbox("hello")
    if username in users:
        password = input("Input Password: ")
        if password == users[username]["password"]:
            print("You have access")
            if username == "admin":
                print("You are admin, and therefore have admin permissions")
                action = input("Input your chosen action, here are your options as an admin: Search Movies, Edit Movies, Buy Tickets  ")
                if action == "Search Movies":
                    search_movies()
                elif action == "Edit Movies":
                    edit_movies()
                    print(movies)
                elif action == "Buy Tickets":
                    buy_tickets()
                else:
                    print("Action not recognised")
            else:
                print("Default user permissions granted")
            x += 1
        else: 
            print("Validation Error")
    else: 
        print("Validation Error")

