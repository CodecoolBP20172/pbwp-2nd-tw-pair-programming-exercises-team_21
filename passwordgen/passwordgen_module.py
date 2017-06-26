<<<<<<< HEAD
import random
import string
def passwordgen():
    e = []
    for i in range(2):
        e.append(random.choice(list(string.ascii_lowercase)))
        e.append(random.choice(list(string.ascii_uppercase)))
        e.append(str(random.randrange(0, 9)))
        e.append(random.choice(list('!@#$%^&*()?')))
    e = ("").join(e)
    return e

def main():
    passwordgen()
=======
def passwordgen():
    return


def main():
    return
>>>>>>> 09f839555b6954a7aba9b86aeecb792ec87088b3


if __name__ == '__main__':
    main()
