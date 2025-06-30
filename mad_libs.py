import random

print("Choose a template:")
print("1. Hospital Story")
print("2. Camping Story")
print("3. Magical Castle Letter")

choice = input("Enter the number of the template you want to use (1-3): ")

if choice == "1":
    number = input("Type a number: ")
    time_measure = input("Type a measure of time (e.g., days, weeks): ")
    transport = input("Type a mode of transportation: ")
    adjective = input("Type an adjective: ")
    adjective2 = input("Type another adjective: ")
    noun = input("Type a noun: ")
    color = input("Type a color: ")
    body_part = input("Type a part of the body: ")
    verb = input("Type a verb: ")
    number2 = input("Type another number: ")
    noun2 = input("Type another noun: ")
    noun3 = input("Type one more noun: ")
    body_part2 = input("Type another part of the body: ")
    verb2 = input("Type another verb: ")
    noun4 = input("Type one last noun: ")
    adjective3 = input("Type another adjective: ")
    silly_word = input("Type a silly word: ")

    story = f"\nIt was about {number} {time_measure} ago when I arrived at the hospital in a {transport}. "
    story += f"The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here. "
    story += f"There are nurses here who have {color} {body_part}. "
    story += f"If someone wants to come into my room I told them that they have to {verb} first. "
    story += f"I’ve decorated my room with {number2} {noun2}. Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}. "
    story += f"I heard that all doctors {verb2} {noun4} every day for breakfast. "
    story += f"The most {adjective3} thing about being in the hospital is the {silly_word} {noun}!"

elif choice == "2":
    person_name = input("Type a person's name: ")
    noun = input("Type a noun: ")
    feeling1 = input("Type a feeling (adjective): ")
    verb = input("Type a verb: ")
    feeling2 = input("Type another feeling (adjective): ")
    animal = input("Type an animal: ")
    verb2 = input("Type another verb: ")
    color = input("Type a color: ")
    verb_ing = input("Type a verb ending in -ing: ")
    adverb = input("Type an adverb ending in -ly: ")
    number = input("Type a number: ")
    time_measure = input("Type a measure of time: ")
    color2 = input("Type another color: ")
    animal2 = input("Type another animal: ")
    number2 = input("Type another number: ")
    silly_word = input("Type a silly word: ")
    noun2 = input("Type another noun: ")

    story = f"\nThis weekend I am going camping with {person_name}. "
    story += f"I packed my lantern, sleeping bag, and {noun}. "
    story += f"I am so {feeling1} to {verb} in a tent. "
    story += f"I am {feeling2} we might see a(n) {animal}, I hear they’re kind of dangerous. "
    story += f"While we’re camping, we are going to hike, fish, and {verb2}. "
    story += f"I have heard that the {color} lake is great for {verb_ing}. "
    story += f"Then we will {adverb} hike through the forest for {number} {time_measure}. "
    story += f"If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet! "
    story += f"At night we will tell {number2} {silly_word} stories and roast {noun2} around the campfire!!"

elif choice == "3":
    name = input("Type a person's name: ")
    adjective = input("Type an adjective: ")
    color = input("Type a color: ")
    animal = input("Type an animal: ")
    place = input("Type a place: ")
    adjective2 = input("Type another adjective: ")
    creature1 = input("Type a plural magical creature: ")
    adjective3 = input("Type one more adjective: ")
    creature2 = input("Type another plural magical creature: ")
    room = input("Type a room in a house: ")
    noun = input("Type a noun: ")
    noun2 = input("Type another noun: ")
    plural_noun = input("Type a plural noun: ")
    adjective4 = input("Type an adjective: ")
    plural_noun2 = input("Type another plural noun: ")
    number = input("Type a number: ")
    time_measure = input("Type a measure of time: ")
    verb_ing = input("Type a verb ending in -ing: ")
    adjective5 = input("Type another adjective: ")
    noun5 = input("Type one last noun: ")

    story = f"\nDear {name}, I am writing to you from a {adjective} castle in an enchanted forest. "
    story += f"I found myself here one day after going for a ride on a {color} {animal} in {place}. "
    story += f"There are {adjective2} {creature1} and {adjective3} {creature2} here! "
    story += f"In the {room} there is a pool full of {noun}. "
    story += f"I fall asleep each night on a {noun2} of {plural_noun} and dream of {adjective4} {plural_noun2}. "
    story += f"It feels as though I have lived here for {number} {time_measure}. "
    story += f"I hope one day you can visit, although the only way to get here now is {verb_ing} on a {adjective5} {noun5}!!"

else:
    story = "\nInvalid choice. Please restart the program and choose 1, 2, or 3."

print(story)
