#Prompt the user: Ask the user for different 
# words following specific prompts, such as a noun, verb, adjective, etc.
adjective1 = input("Enter an adjective (e.g., sunny, boring): ")
adjective2 = input("Enter an adjective2: ")
adjective3 = input("Enter an adjective3: ")
adjective4 = input("Enter an adjective4: ")

if adjective1.lower() == "rainy":
    weather_comment = "I should’ve brought an umbrella!"
else:
    weather_comment = "Perfect weather for an adventure!"

story = f"""
On a beautiful {adjective1} day, I went to the zoo. {weather_comment}
I saw a funny {adjective2} monkey swinging from the trees.
Then, I spotted a majestic {adjective3} lion lounging in the sun.
What a wild and {adjective4} experience!
"""
print(story)

