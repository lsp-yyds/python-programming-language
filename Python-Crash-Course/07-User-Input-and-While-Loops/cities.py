prompt = "Please enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        # using break to exit a loop
        break
    else:
        print("I'd love to go to " + city.title() + "!")