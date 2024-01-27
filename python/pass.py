def main():
    password = "4honor"
    tries = 3
    while tries > 0:
     attempt = input("Enter your password: ")
     if attempt != password:
        tries -= 1
        print("Incorrect password.", tries, "Attempt left")
        

     elif tries == 0:
        print("Too many incorrect attempts. Account Locked.")
     else:
        print("Correct password. Login Succesfull!.")

main()