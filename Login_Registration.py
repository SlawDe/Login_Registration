accounts = {}
while True:
    option= input("Choose 'Login' lub 'Register'\n")
    login = input("Login: ")
    password = input("Hasło: ")
 
    if option == "Register":
        accounts[login] = password                   
    elif option == "Login":
        accounts[login] == password
        print("Login success !")
        break
    else:
        print("Error. Try again !")
        continue
    
    
    