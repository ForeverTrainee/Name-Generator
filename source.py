import linecache
import random


def sourced_data():
    with open("NamesSource/uk.txt", "r") as file:
        for name in enumerate(file):
            pass
        print(name)
        randomName = random.randint(0, name[0])
        print(randomName)
        firstName = linecache.getline("NamesSource/uk.txt", randomName)
        print(firstName)

    with open("NamesSource/us.txt", "r") as file:
        for name in enumerate(file):
            pass
        print(name)
        randomName = random.randint(0, name[0])
        print(randomName)
        lastName = linecache.getline("NamesSource/us.txt", randomName)
        print(lastName)

    fullName = firstName.strip() + " " + lastName.strip()
    print(fullName)
    return fullName

sourced_data()
