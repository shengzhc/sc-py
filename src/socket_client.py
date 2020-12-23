import socket


def Main():
    s = socket.socket()
    print("Client connecting...")
    s.connect(("127.0.0.1", 5001))
    msg = input(" ? ")

    while msg != "q":
        s.send(msg.encode())
        data = s.recv(1024).decode()
        print("Received from server: ", str(data))
        msg = input(" ? ")
    s.close()


if __name__ == '__main__':
    Main()
