import socket


def Main():
    host = "127.0.0.1"
    port = 5001
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    print("Connection from: ", str(addr))

    while True:
        data = conn.recv(1024).decode()
        # cases like client terminates unexpectly
        if not data:
            print("unexpected data")
            break
        print("from connected user: " + str(data))
        data = str(data).upper()
        msg = input(" ? ")
        conn.send(msg.encode())

    conn.close()


if __name__ == '__main__':
    Main()
