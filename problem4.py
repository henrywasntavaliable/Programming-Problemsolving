def birthday_discount():
    print("Welcome to The Media Hub!")
    
    age = int(input("Please enter your age: "))
    price = float(input("Enter the price of your favourite item: "))
    
    discount_rate = age / 100   # Convert age into a percentage (e.g. 30 → 0.30)
    discount_amount = price * discount_rate
    final_price = price - discount_amount
    
    print(f"For your {age}th birthday, we'll give you a {age}% discount!")
    print(f"Your item would cost: {final_price}")

