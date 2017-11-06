import socket
import time
 
 
def Main():
    #Give ChatBot server an IP address and port
    host = "127.0.0.1"
    port = 5001
    #Create Socket and bind server to socket           
    thisSocket = socket.socket()
    thisSocket.bind((host,port))
    #Listen for clients     
    thisSocket.listen(1)
    #Connect to client
    conn, addr = thisSocket.accept()
    #print Connect ip address
    print ("The Connection ip is : " + str(addr))
    #Repear forever
    while True:
                #Receive info from client
                receiveMess = conn.recv(1024).decode()
                #if no info from client end loop
                if not receiveMess:
                                    break
                #Print info from client
                print ("Message from User to Chatbot : " + str(receiveMess))
                #set return message
                returnMess = "This is the return message"
                conn.send(returnMess.encode())                             
    conn.close()                
if __name__ == '__main__':
            Main()
