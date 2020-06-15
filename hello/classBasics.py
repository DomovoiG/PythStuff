#class basics
import datetime

class User:
    """
    |   A Class that stores full name and birthday for users
    |   methods decribed here:
    |   __init__(self, fullName, birthday)
    """
    def __init__(self, fullName, birthday): #this is how you initialize a class. (create a constructor)
        self.name = fullName
        self.birthday = str(birthday) #yyyymmdd

        #extract first and last names
        namePieces = fullName.split(" ")
        self.firstName = namePieces[0]
        self.lastName = namePieces[1]

    def age(self, today=datetime.date(2001, 5, 12)):#created default value for "today", as keyword argument(kwarg)
        """Returns the age of the user in years."""
        #today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd) #date of birth
        ageInDays = (today - dob).days
        ageInYears = ageInDays/365
        return int(ageInYears)

user1 = User("David Bowman", 19940912)

#these variables are attached to the user1 instance of User. they must be accessed using the "." operator.
print(user1.firstName)
print(user1.lastName)
print(user1.age())
print(user1.age(today=datetime.date(2020, 6, 12)))

#we can see that these variables, even thought they are named the same as the user1 members are not attached.
#they print out a differnt value
firstName = "Arthur"
lastName = "Clark"

print(firstName,lastName)
print(user1.firstName,user1.lastName)

#List comprehensions

doubles = [x*2 for x in range(5)]

print(doubles)
