import socket
from common.util import *
from des import DesKey


def connect_to_server(host, port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (host, port)
    print('connecting to {} port {}'.format(host,port)) #Move to logging
    sock.connect(server_address)
    return sock


def send_message(sock, message):
    if type(message) == bytes:
        sock.sendall(message)
    else:
        sock.sendall(str.encode(message))


def close_connection(sock):
    sock.close()
    

def main():
    sock = connect_to_server('localhost', port=10000)
    try:
        # Define Diffie-Hellman parameters
        print('Defining Diffie-Hellman parameters with server')
        prime_module_number = generate_random_prime() #Prime Module number
        print('sending {}'.format(str(prime_module_number))) # Move to logging
        send_message(sock, str(prime_module_number))
        server_prime_generated = sock.recv(128).decode(encoding='latin-1')
        server_prime_generated_number = int(server_prime_generated)

        client_private_key = generate_random_prime() #Client private key
        print('Client Private Key {}'.format(str(client_private_key))) # Move to logging

        client_result = power(server_prime_generated_number, client_private_key, prime_module_number)
        print('Client Result {}'.format(str(client_result))) # Move to logging
        send_message(sock, str(client_result))
        
        server_result = sock.recv(128).decode(encoding='latin-1')
        print('Server received result {}'.format(server_result)) # Move to logging
        server_result_number = int(server_result)

        shared_private_key = power(server_result_number, client_private_key, prime_module_number)
        print('Shared Private Key {}'.format(str(shared_private_key))) # Move to logging

        key_object = DesKey(shared_private_key.to_bytes(8, byteorder='big'))
        message = 'lorem ipsum blablabla'

        encrypted_message = key_object.encrypt(str.encode(message), padding=True)
        print('Encrypted message : {}'.format(encrypted_message)) # Move to logging
        send_message(sock, encrypted_message)

        while True:
            data = sock.recv(128)
            if len(data) == 0:
                break
            print('received {}'.format(key_object.decrypt(data, padding=True))) #Move to logging     
            
    finally:
        print('closing socket') # Move to logging
        close_connection(sock)

if __name__ == '__main__':
    main()