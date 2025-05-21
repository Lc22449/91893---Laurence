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

def print_dictionary(movie_id):
    msg = ''
    for key, value in movies[movie_id].items():
        msg += f'{key} : {value}\n'
    easygui.msgbox((f"The Movie {movie_id} has this information:\n" +msg))

def search_movies():
    Movie_name = easygui.enterbox("insert movie name here: ")
    for movie_id in movies:
        if movies[movie_id]["title"] == Movie_name:
            print_dictionary(movie_id)
            return movie_id

def edit_movies():
    movie_id = search_movies()
    movie_key = easygui.enterbox("Input chosen key: ")
    for key in movies[movie_id]:
        if movie_key == key:
            movies[movie_id][key] = easygui.enterbox("Change your key: ")
    print_dictionary(movie_id)

def buy_tickets(movie_id):
    msg = ''
    
    easygui.msgbox(f"What movie would you like to buy tickets to?\nYour balance is {balance}")
    search_movies()


x = 1

while x == 1:
    username = easygui.enterbox("Input Your Username")
    if username in users:
        password = easygui.enterbox("Input Password: ")
        if password == users[username]["password"]:
            easygui.msgbox("You have access")
            if username == "admin":
                easygui.msgbox("You are admin, and therefore have admin permissions")
                action = easygui.choicebox("Pick an action:", choices=["Search Movies", "Edit Movies", "Buy Tickets"])
                if action == "Search Movies":
                    item = search_movies()
                elif action == "Edit Movies":
                    edit_movies()
                elif action == "Buy Tickets":
                    buy_tickets()
                else:
                    easygui.msgbox("Action not recognised")
            else:
                easygui.msgbox("Default user permissions granted")
            x += 1
        else: 
            easygui.msgbox("Validation Error")
    else: 
        easygui.msgbox("Validation Error")

