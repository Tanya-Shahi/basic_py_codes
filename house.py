import random
class Hat:
    def __init__(self):
        self.houses=["Gryffindor","Hufflepuff","RavenClaw","Slytherin"]
    def sort(self,name):
        if name == "Draco Malfoy":
            print(name,"is in","Slytherin")
        else:
         print(name,"is in",random.choice(self.houses))
hat=Hat() 
name=input("enter name:")
hat.sort(name)

        