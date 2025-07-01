# Mad Libs Game - First Python Project
# This is a simple Mad Libs game that asks for user input and creates a funny sentence.

print(" Welcome to the Mad Libs Game! \n")

place = input("Enter a place: ")
person_name = input("Enter a person's name: ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
color = input("Enter a color: ")
clothing = input("Enter a piece of clothing: ")
verb1 = input("Enter a verb (past tense): ")
verb2 = input("Enter another verb (past tense): ")
noun = input("Enter a noun: ")

madlib = (
    f"\nToday I went to the {place} with my best friend {person_name}. "
    f"We saw a {adjective} {animal} wearing a {color} {clothing}. "
    f"It {verb1} right in front of us and then {verb2} into a {noun}!"
)

print("\nHere's your Mad Libs story:")
print(madlib)
