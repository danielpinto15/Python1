class NoMorePudins(Exception):
    pass

age = 3

try:
    if age < 5:
        raise NoMorePudins("Acabaram os pudins")
except NoMorePudins as error:
    print(error)

    print ("ola")