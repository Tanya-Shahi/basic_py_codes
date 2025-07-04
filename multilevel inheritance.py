#hierachy of classes
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def show_details(self):
        print(f"name:{self.name}")  
        print(f"species:{self.species}") 
class Dog:
     def __init__(self,name,breed):
         Animal.__init__(self,name,species="dog")
         self.breed=breed
     def show_details(self):
         Animal.show_details(self)
         print(f"breed:{self.breed}")
class pug:
    def __init__(self,name,color):
       Dog.__init__(self,name,breed="pug")
       self.color=color
    def show_details(self):
       Dog.show_details(self) 
       print(f"color:{self.color}")  

o=pug("tom","black")
o.show_details()          
            
p=Dog("tom","goldie")
p.show_details() 

w=Animal("tom","cat")
w.show_details()