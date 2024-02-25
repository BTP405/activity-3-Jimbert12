import socket
import threading
import pickle

class User:
    def __init__(self):
        self.host = 'localhost'
        self.port = 55556
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.client_socket.connect((self.host, self.port))
        print("You Are Connected to the Chat Room")

        # Start a thread to receive messages from the server
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

        # Sending messages
        self.send_messages()

    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(4096)
                if not data:
                    break

                # Unpickle received data
                message = pickle.loads(data)
                print(message)
            except Exception as error:
                print("Error:", error)
                break

    def send_messages(self):
        while True:
            try:
                message = input("Enter your message: ")
                if message.lower() == 'exit':
                    break

                # Pickle the message before sending
                data = pickle.dumps(message)
                self.client_socket.sendall(data)

            except Exception as error:
                print("Error sending message:", error)
                break

        self.client_socket.close()

if __name__ == "__main__":
    chat_client = User()
    chat_client.start()
