
def login(noOfDigitsForThePalindrome:int, userId:str, password:str):
    if type(noOfDigitsForThePalindrome) != int or  noOfDigitsForThePalindrome <= 0 or not userId.isalnum() or not password.isalnum():
        print("Invalid Input")
        return

    user_number = userId[4:]
    password_number = password[4:]
    if user_number != password_number:
        print("UserId or password is not valid, pls try again.")
        return

    result = ["0" for _ in range(noOfDigitsForThePalindrome)]
    result[0] = '1'
    result[-1] = '1'
    print(f"Welcome {userId} and the generated token is: token-{''.join(result)}.")


    
    
