class Point():
    def __init__(self , x , y):
        self.x = x
        self.y = y


class Flight():

    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passanger(self,name):
        if not self.open_seats():
            return False;
        self.passengers.append(name)
        return True;

    def open_seats(self):
        return self.capacity - len(self.passengers);
    

fligth = Flight(3)

people = ['john','harry','ginny','melissa'];

for person in people:
    if fligth.add_passanger(person):
        print(f'added {person} to flight succesfully');
    else:
        print(f'Not avaitable seats for {person}')

