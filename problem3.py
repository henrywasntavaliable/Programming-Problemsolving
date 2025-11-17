def calculate_birth_year():
    print("Welcome to The Media Hub!")
    
    age = int(input("Please enter your age: "))
    current_year = int(input("Please enter the current year: "))
    
    birth_year = current_year - age
    opening_year = 1995
    
    difference = birth_year - opening_year
    
    print(f"You were born in {birth_year}, {difference} years after our opening!")
