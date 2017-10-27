import socket
 
def Main():
    #connection to ChatBot 
    host = '127.0.0.1'
    port = 5001	
    thisSocket = socket.socket()
    thisSocket.connect((host,port))
    #Reading first message to ChatBot
    message = input(" Message to ChatBot: ")
    #Continue conversation with ChatBot until end is types
    while message != "end":
    #send message to Chatbot
                        thisSocket.send(message.encode())
                        #Receive Message from ChatBot
                        RMess = thisSocket.recv(1024).decode()
                        #Print message from ChatBot
                        print('Message Received from ChatBot: '+RMess)
                        #Get user message to ChatBot
                        message = input(" Message to  ChatBot: ")
    #Close Socket
    thisSocket.close()
    #Display conversation is over
    print("Conversation between user and ChatBot Ended")
#Check if running directly from this file
if __name__ == '__main__':
    Main()
