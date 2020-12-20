try:
    fob = open('./app.log', 'r')
    try:
        fob.write('testing line')
    finally:
        fob.close()
        print('finally block executed to close the file')
except IOError:
    print("Error: cant find the file or write data")
