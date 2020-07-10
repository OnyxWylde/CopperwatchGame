#Character Creation
welcome = input('Welcome, are you new around here adventurer? (y/n)')

#New user algorithm
if welcome == "y":
    while True:
        username  = input("Enter a username:")
        username1 = input("Is "  + username + " your name(y/n)")
        if username1 == "y":
          password  = input("Enter a password:")
          password1 = input("Confirm password:")
          if password == password1:
              file = open(username+".txt", "w")
              file.write(username+":"+password)
              file.close()
              welcome = "n"
              break
          else:
            print("Passwords do NOT match! Please try again")
        else:
          print('Goodbye then, stranger')
          quit

#Existing user login algorithm
if welcome == "n":
    while True:
        login1 = input("Login:")
        login2 = input("Password:")
        file = open(login1+".txt", "r")
        data   = file.readline()
        file.close()
        if data == login1+":"+login2:
            print("Welcome Back")
            break
        print("Incorrect username or password. Please try again")
else:
   print ("Access Denied")
   quit