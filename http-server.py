import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('127.0.0.1', 8080)

server.bind(address)

server.listen()
print('Server is listening!')

def send_response(conn):
    with open('hello_world.html', 'r') as file:
       text = file.read()
    request = conn.recv(1024)
    print(request.decode('utf-8'))
    response = f'''\
HTTP/1.1 200 OK

{text}
'''
    conn.send(response.encode())

while True:
    conn, addr = server.accept()
    print(f'{addr} has connected')
    send_response(conn)
    