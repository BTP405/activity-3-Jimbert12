import socket
import pickle
import os

def receive_file(client_socket, directory):
    try:
       
        F_info = client_socket.recv(4096)
        F_info = pickle.loads(F_info)
        file_name = F_info['file_name']
        file_content = F_info['file_content']

        # Ensure the directory exists
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Save the received file to the specified directory
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'wb') as file:
            file.write(file_content)

        return f"File was saved succesfully"
    except Exception as e:
        return f"Error receiving/saving file: {str(e)}"

def run_server(save_directory):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print("Server is listening for incoming connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print("Connected to:", client_address)
        try:
            message = receive_file(client_socket, save_directory)
            print(message)

            ack_message = "File received by the server!"
            client_socket.sendall(ack_message.encode())
        finally:
            client_socket.close()

if __name__ == "__main__":
    directory = 'Q1'  
    run_server(directory)
