def search_movies():
    Movie_name = easygui.enterbox("insert movie name here: ")
    for item in movies:
        if movies[item]["title"] == Movie_name:
            for key, value in movies[item].items():
                easygui.msgbox(f'{key}: {value}\n')
    return item