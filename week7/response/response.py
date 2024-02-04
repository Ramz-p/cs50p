from validators import email

def main():
    user_input = input("Enter an email address: ")
    if email(user_input):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
