import time
import random

class Cat:
  def __init__(self, name):
    self.name = name
    self.age = 0
    self.is_alive = True
    self.hunger = 50
    self.boredom = 50

def __str__(self):
    return f"Cat {self.name} is {self.age} years old."

def feed(self):
    if self.hunger < 30:
        print(f"{self.name} is not hungry.")
    else:
        self.hunger -= 20
        print(f"{self.name} is eating.")

def play(self):
    if self.boredom < 30:
        print(f"{self.name} is not bored.")
    else:
        self.boredom -= 20
        print(f"{self.name} is playing.")

def wait(self):
    self.hunger += 5
    self.boredom += 5
    self.age += 1
    if self.age >= random.randint(7, 18):
        self.is_alive = False
        print(f"{self.name} has died.")
    else:
        print(f"{self.name} is waiting.")

def show_options(self):
    print(f"What would you like to do with {self.name}?")
    print("1. Feed")
    print("2. Play")
    print("3. Wait")

def act(self, choice):
    if choice == "1":
        self.feed()
    elif choice == "2":
        self.play()
    elif choice == "3":
        self.wait()

def run(self):
    print(f"Welcome to the cat simulator with {self.name}!")
    while self.is_alive:
        self.show_options()
        choice = input("> ")
        while choice not in ["1", "2", "3"]:
            print("Invalid choice. Please enter 1, 2, or 3.")
            choice = input("> ")
        self.act(choice)
        time.sleep(2)
cat = Cat("Asya")
cat.run()
