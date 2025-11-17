def count_up():
    print("Welcome to The Media Hub!")
    number = int(input("Enter a number: "))
    
    print(f"Counting up to {number}:")
    for i in range(1, number + 1):   # starts at 1, ends at 'number'
        print(i)
