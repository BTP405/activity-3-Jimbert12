import socket
import pickle

def send_file(file_content, client_socket):
    try:
        # Prepare file info to be sent
        file_info = {'file_name': 'Results.txt', 'file_content': file_content}

        # Serialize file info and send it to the server
        message = pickle.dumps(file_info)
        client_socket.sendall(message)

        return "File sent successfully"
    except Exception as e:
        return f"Error sending file: {str(e)}"

def run_client():
    file_path = "/Users/jimbert/Desktop/SEMESTER4/BTP 405 .NBB/Activities/Act-3/Q1/Message.txt"
    with open(file_path, 'rb') as file:
        file_content = file.read()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    try:
        # Send file content to the server
        message = send_file(file_content, client_socket)
        print(message)
    finally:
        client_socket.close()

if __name__ == "__main__":
    run_client()
