import quest
import random
import messages

genders = ["female", "male"]
femaleNames= [
    "Flora Schroeder", "Nancy Ayers", "Lauri Cameron", "Aimee Smith", "Addie Marsh", "Tammy Malone", "Nina David", "Kaitlin Gillespie", "Audra Nash", "Cathy Bass", "Abigail Curry", "Aurora Valencia", "Rhoda Greene", "Rosemarie Baxter", "Lela Mills", "Jenny Moody", "Liza Clark", "Leola Braun", "Erna Ortega", "Kendra Hale"
]
maleNames = [
    "Junior Shepard", "Barry Odonnell", "Wilfredo Sheppard", "Frances Pacheco", "Abdul Watkins", "Oren Shah", "Ernest Farley", "Sybil Huff", "Lenard Vaughan", "Hans Boyer", "Hilton Robles", "Anderson Klein", "Rickie Bray", "Clint Downs", "Graham Norris", "Alex Solis", "Florencio Rodgers", "Eddy Chavez", "Bernard Bass", "Santiago Esparza"
]

npcTypes = [
    "Merchant", "Warrior", "Villager", "Child", "Nobleman", "Criminal"
]

class NPC:
    def __init__(self, quest=None):
        self.gender = random.choice(genders)
        self.name = ""
        if self.gender == "female":
            self.name = random.choice(femaleNames)
        else:
            self.name = random.choice(maleNames)

        self.type = random.choice(npcTypes)

    def greeting(self):
        greeting = random.choice(messages.greetings)
        if greeting == "Huh? ":
            return greeting
        else:
            return greeting + "My name is " + self.name + "."
# TODO: make the npcs interactive

testNPC = NPC()

print(testNPC.greeting())
