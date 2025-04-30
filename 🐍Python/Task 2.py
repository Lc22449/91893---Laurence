passwordcorrect = 0 

y = input("select password: ")


while passwordcorrect == 0:
    x = input("Password: ")
    if x == y:
        print("You are correct! ")
        passwordcorrect += 1

    else:
        print("You got it wrong Haha!")


    

