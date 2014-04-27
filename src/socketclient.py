import socket
import sys
import time
import Image
import io
import random

# Generate a random array of bytes (random image)
def generate_random_genes():

    result = []
    for i in range(1536):
        result.append(random.randint(0,255))

    return bytearray(result)


HOST, PORT = "localhost", 8888
#data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    
except:
    sock.close()
    print("Could not set up socket connection")
    sys.exit(0)

print('Welcome to Client Application\nType a message to the server')
user_in = raw_input('> ')
while (user_in  != 'q'):
    try:

        if user_in.find('<random>'):
            #print(generate_random_genes())
            user_in = user_in.replace('<random>', generate_random_genes())


        sock.sendall(user_in)
        
        # Receive data from the server and shut down
        received = bytearray(sock.recv(7168).split(':')[1])


#        int_list = []

#       for b in received:
#           int_list.append(int(b))
#       print int_list

#        tuple_list = zip(int_list[0::3],int_list[1::3],int_list[2::3])

#        img = Image.new('RGB', (32,16))
#        img.putdata(tuple_list)
#        img.show()

#        print(len(received))
        
        # display received data
        print "Sent:     {}".format(user_in)
        print "Received: {}".format(str(received))

        #img = Image.
    
        
        user_in = raw_input('> ')
    
    except:
        sock.close()
        raise
        break

sock.close()
