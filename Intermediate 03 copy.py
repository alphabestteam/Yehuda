# exceptions help us to not drop all the program with try and except


def Exceptions(num=2):
    for i in range(num):
        number = -999

        try:
            number = int(input("enter number:"))
        except:
            print("enter a valid number")
        if number != -999:
            print(number)

    print("running Finished.")


# 1. Comprehension List is way to make a new list with list how already exist with one line

# 2. is option you can do it for example with two for


def list_comp_squer(n=2):
    list_square = [x * x for x in range(n)]
    print(list_square)


from Person import Person


def list_comp_Person(n=2):
    people = [Person() for _ in range(n)]
    people_up_18 = [p for p in people if p.get_age() >= 18]
    for person in people_up_18:
        print(person)  # is can to not print nothing because every one is under 18


if __name__ == "__main__":
    # Exceptions()
    # list_comp_squer()
    list_comp_Person()
