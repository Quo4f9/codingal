print("HELLO I am AI bot")

name=input("what is your name?:")
print("nice to meet you",name)

mood=input("how are you feeling today?(good/bad):").lower().strip()

if mood=="good":
    print("I am glad to hear that!")
elif mood=="bad":
    print("sorry to hear that. Hope things get better soon")
else:
    print(f"it was nice chatting with you{name}.Goodday!")

    