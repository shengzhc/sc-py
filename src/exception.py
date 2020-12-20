try:
    fob = open('./app.log', 'r')
    try:
        fob.write('testing line')
    finally:
        fob.close()
        print('finally block executed to close the file')
except IOError:
    print("Error: cant find the file or write data")


class Error(Exception):
    """Base class for other exceptions"""
    pass


class InputTooSmallException(Error):
    """Raised when input is smaller than actual one"""
    pass


class InputTooLargeException(Error):
    """Raised when input is larger than actual one"""
    pass


actual = "m"

while True:
    try:
        alp = input("Enter an alphabet:")
        if (alp < actual):
            raise InputTooSmallException
        elif (alp > actual):
            raise InputTooLargeException
        else:
            break
    except InputTooSmallException:
        print("The input is too small, please try again")
    except InputTooLargeException:
        print("The input is too large, please try again")

print("Congrats")
