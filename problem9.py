def rating_scale():
    print("Welcome to The Media Hub!")
    max_rating = int(input("Enter the maximum rating: "))
    
    print(f"Rating scale up to {max_rating}:")
    for i in range(1, max_rating + 1):
        print(i)
