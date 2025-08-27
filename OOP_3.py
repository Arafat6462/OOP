class Persion:
    number_of_people = 0
    
    def __init__(self, name):
        self.name = name
        Persion.number_of_people += 1

p1 = Persion("Arafat")
p2 = Persion("Saki")

print(Persion.number_of_people)
Persion.number_of_people = 4
print(p1.number_of_people)
print(p2.number_of_people)