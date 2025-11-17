def personalised_recommendation():
    print("Welcome to The Media Hub!")
    
    name = input("What's your name? ")
    age = int(input("What's your age? "))
    favourite = input("What's your favourite media type? ")
    
    print(f"Hi {name}! We love {favourite} at The Media Hub!")
    print(f"As you are {age}, you could enjoy a {age}% birthday discount!")
