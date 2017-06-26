<<<<<<< HEAD
x = 2
def palindrome(x):
    #x = str(input('Add a string'))
    x = x.replace(' ', '')
    x = x.lower()
    for i in range(len(x)):
        if x[i] == x[-(i+1)]:
            continue
        else:
            return False
    return True

def main():
    palindrome(x)
=======
def palindrome(str):
    return


def main():
>>>>>>> 09f839555b6954a7aba9b86aeecb792ec87088b3
    return


if __name__ == '__main__':
    main()
