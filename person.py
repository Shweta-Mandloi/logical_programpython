class Person:
    def start(self, first, last): #self ka use hame object ka data accse krne ke liye use krte he 
        self.first = first
        self.last = last

    def first_name(self):
        print("First Name:", self.first)

    def last_name(self):
        print("Last Name:", self.last)

    def full_name(self):
        print("Full Name:", self.first, self.last)


# Object banate hain
p1 = Person("Shweta", "Mandloi")

# Methods call karte hain
p1.first_name()   # First Name: Shweta
p1.last_name()    # Last Name: Mandloi
p1.full_name()    # Full Name: Shweta Mandloi
