import math
class person:
    def __init__(self, name, birthday, location, address):
        self.name = name
        self.birthday = birthday
        self.location = location
        self.address = address

def closestPerson(person, personArray):
    if(person.name != personArray[0].name):
        closestDistance = math.sqrt(pow(personArray[0].location[0] - person.location[0], 2) + pow(personArray[0].location[1] - person.location[1], 2))
        closestPerson = personArray[0].name
    else:
        closestDistance = math.sqrt(pow(personArray[1].location[0] - person.location[0], 2) + pow(personArray[1].location[1] - person.location[1], 2))
        closestPerson = personArray[1].name

    for i in range(1, len(personArray)):
        person2 = personArray[i]
        if(person.name != person2.name):
            distance = math.sqrt(pow(person2.location[0] - person.location[0], 2) + pow(person2.location[1] - person.location[1], 2))
            if (closestDistance > distance):
                    closestDistance = distance
                    closestPerson = person2.name
                    
    return closestPerson
                
Alex = person("Alex", "02-21-2000", [-10.0, 20.0], "125 Kings Point Road")
Chase = person("Chase", "05-16-2003", [10, 22.1], "123 Lake Road")
Michael = person("Michael", "07-09-1997", [16.3, 1.5], "15 Dennis Street")
Dave = person("Dave", "10-01-1995", [-13.5, 3.6], "1 Hyper Loop Way")
Olivia = person("Olivia", "12-11-2001", [-10.0, 21.0], "128 Kings Point Road")
Mark = person("Mark", "02-20-1999", [-75.2, 95.3], "256 Angel Street")

personArray = [Alex, Chase, Michael, Dave, Olivia, Mark]
print(closestPerson(Olivia, personArray))
    