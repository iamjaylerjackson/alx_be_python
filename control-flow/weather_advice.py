user_input = input("What's the weather like today? (sunny/rainy/cold): ")

if user_input == "sunny":  # If the weather is “sunny”
    print("Wear a t-shirt and sunglasses.")

elif user_input == "rainy":  # If the weather is “rainy”
    print("Don't forget your umbrella and a raincoat.")

elif user_input == "cold":  # If the weather is “cold”
    print("Make sure to wear a warm coat and a scarf.")

else:
    print("Sorry, I don't have recommendations for this weather.")
