weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

if weather == 'sunny':
    print("Wear a t-shirt and sunglasses.")

elif weather == 'rainy':  # Ensure the condition checks against 'rainy'
    print("Don't forget your umbrella and a raincoat.")

elif weather == 'cold':  # Ensure the condition checks against 'cold'
    print("Make sure to wear a warm coat and a scarf.")

else:  # Handle unexpected input
    print("Sorry, I don't have recommendations for this weather.")

