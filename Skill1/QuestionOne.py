class Passenger:
    def __init__(self, name, age,source,destination):
        self.name = name
        self.age = age
        self.source = source
        self.destination = destination

    def view(self):
        print(self.name, self.age)


class Train(Passenger):
    def __init__(self, name, age, persons, source, destination):
        Passenger.__init__(self, name, age,  source, destination)
        self.cost = int(200) * persons

    def view(self):
        print("*-*-* Details are save Successfully *-*-*")
        print("Passenger Name : ", self.name)
        print("Passenger Age : ", self.age)
        print("Source : ", self.source)
        print("Destination : ", self.destination)
        print("Number of Persons : ",int(self.cost/int(200)))
        print("Total Cost of the Tickets : ₹", self.cost, '/-')


print('Enter Customer Name')
name = input()
print('Enter age of the customer')
age = int(input())
print('Enter number of persons')
persons = int(input())
print('Enter your source of Travel')
source=input()
print('Enter your destination of the Travel')
destination=input()
ob = Train(name, age, persons, source, destination)
ob.view()
