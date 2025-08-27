class Persion:
    number_of_people = 0 # class variable/ attribute
    
    def __init__(self, name):
        self.name = name
        Persion.number_of_people += 1

    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people

p1 = Persion("Arafat")
p2 = Persion("Saki")

print(Persion.number_of_people)
Persion.number_of_people = 4
print(p1.number_of_people)
print(p2.number_of_people)

print(Persion.get_number_of_people())