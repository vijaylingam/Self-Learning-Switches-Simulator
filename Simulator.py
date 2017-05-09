__author__ = 'vijaychandra'

import random

def randomMAC():
    x = random.randint(1,15)
    mac = [ 0x18%x, 0x16%x, 0x3e,
		random.randint(0x00, 0x7f),
		random.randint(0x00, 0xff),
		random.randint(0x00, 0xff) ]
    return ':'.join(map(lambda x: "%02x" % x, mac))

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

def S1(port, message, source_address, destination):
    table = []
    with open('table1.txt') as f:
        for line in f:
            table.append(line)
    if(len(table) == 0):
        with open('table1.txt', 'a') as f:
            x = str(source_address) + " " + str(port)+"\n"
            f.write(x)
        table.append([source_address, port])
    counter = 0
    for address in (table):
        if str(destination) == str(address[0]):
            counter += 1
            if(int(address[2]) == UP):
                H1(source_address, message, int(destination), 'yes')
            if(int(address[2]) == LEFT):
                H2(source_address, message, int(destination), 'yes')
            if(int(address[2]) == RIGHT):
                S4(RIGHT, message, source_address, int(destination))
            if(int(address[2]) == DOWN):
                S2(DOWN, message, source_address, int(destination))
        if str(source_address) != str(address[0]):
            with open('table1.txt', 'a') as z:
                temp = []
                with open('table1.txt') as f:
                    for line in f:
                        temp.append([line[0], line[2]])
                x = str(source_address) + " " + str(port)+"\n"
                if not([str(source_address), str(port)] in temp):
                    z.write(x)
                    break
    if counter == 0 and port == 0:
        print("Switch1 Broadcasting.")
        S2(UP, message, source_address, destination)
        S4(LEFT, message, source_address, destination)
        H1(source_address, message, destination, 'yes')
    if counter == 0 and port == 2:
        print("Switch1 Broadcasting.")
        S2(UP, message, source_address, destination)
        S4(LEFT, message, source_address, destination)
        H2(source_address, message, destination, 'yes')
    if counter == 0 and port == 1:
        print("Switch1 Broadcasting.")
        S2(UP, message, source_address, destination)
        H1(source_address, message, destination, 'yes')
        H2(source_address, message, destination, 'yes')
    if counter == 0 and port == 3:
        print("Switch1 Broadcasting.")
        S4(LEFT, message, source_address, destination)
        H1(source_address, message, destination, 'yes')
        H2(source_address, message, destination, 'yes')

def S2(port, message, source_address, destination):
    table2 = []
    with open('table2.txt') as f:
        for line in f:
            table2.append(line)
    if(len(table2) == 0):
        with open('table2.txt', 'a') as f:
            x = str(source_address) + " " + str(port) + "\n"
            f.write(x)
        table2.append([source_address, port])
    counter = 0
    for address in table2:
        if str(destination) == str(address[0]):
            counter += 1
            if(int(address[2]) == UP):
                S1(UP, message, source_address, int(destination))
            if(int(address[2]) == LEFT):
                S3(LEFT, message, source_address, int(destination))
            if(int(address[2]) == DOWN):
                H7(int(address[0]), message, int(destination))
        if str(source_address) != str(address[0]):
            with open('table2.txt', 'a') as z:
                temp = []
                with open('table2.txt') as f:
                    for line in f:
                        temp.append([line[0], line[2]])
                x = str(source_address) + " " + str(port)+"\n"
                if not([str(source_address), str(port)] in temp):
                    z.write(x)
                    break
    #BROADCASTING
    if counter == 0 and port == 3:
        print("Switch2 Broadcasting.")
        S3(RIGHT, message, source_address, destination)
        S1(DOWN, message, source_address, destination)
    if counter == 0 and port == 0:
        print("Switch2 Broadcasting.")
        S1(DOWN, message, source_address, destination)
        H7(source_address, message, destination, 'yes')
    if counter == 0 and port == 2:
        print("Switch2 Broadcasting.")
        S3(RIGHT, message, source_address, destination)
        H7(source_address, message, destination, 'yes')

def S3(port, message, source_address, destination):
    table = []
    with open('table3.txt') as f:
        for line in f:
            table.append(line)
    if(len(table) == 0):
        with open('table3.txt', 'a') as f:
            x = str(source_address) + " " + str(port)+"\n"
            f.write(x)
        table.append([source_address, port])

    counter = 0
    for address in (table):
        if str(destination) == str(address[0]):
            counter += 1
            if(int(address[2]) == RIGHT):
                S2(RIGHT, message, source_address, int(destination))
            if(int(address[2]) == DOWN):
                H6(source_address, message, destination, 'yes')
            if(int(address[2]) == LEFT):
                H5(source_address, message, destination, 'yes')

        if str(source_address) != str(address[0]):
            with open('table3.txt', 'a') as z:
                temp = []
                with open('table3.txt') as f:
                    for line in f:
                        temp.append([line[0], line[2]])
                x = str(source_address) + " " + str(port)+"\n"
                if not([str(source_address), str(port)] in temp):
                    z.write(x)
                    break
    if counter == 0 and port == 0:
        print("Switch3 Broadcasting.")
        S2(LEFT, message, source_address, destination)
        H6(source_address, message, destination, 'yes')
    if counter == 0 and port == 1:
        print("Switch3 Broadcasting.")
        H5(source_address, message, destination, 'yes')
        H6(source_address, message, destination, 'yes')
    if counter == 0 and port == 4:
        print("Switch3 Broadcasting.")
        H5(source_address, message, destination, 'yes')
        S2(LEFT, message, source_address, destination)

def S4(port, message, source_address, destination):
    table = []
    with open('table4.txt') as f:
        for line in f:
            table.append(line)
    if(len(table) == 0):
        with open('table4.txt', 'a') as f:
            x = str(source_address) + " " + str(port)+"\n"
            f.write(x)
        table.append([source_address, port])

    counter = 0
    for address in (table):
        if str(destination) == str(address[0]):
            counter += 1
            if(int(address[2]) == UP):
                H3(source_address, message, int(destination), 'yes')
            if(int(address[2]) == LEFT):
                S1(LEFT, source_address, message, int(destination))
            if(int(address[2]) == RIGHT):
                H4(RIGHT, message, source_address, int(destination), 'yes')
            if(int(address[2]) == DOWN):
                S5(DOWN, message, source_address, int(destination))
        if str(source_address) != str(address[0]):
            with open('table4.txt', 'a') as z:
                temp = []
                with open('table4.txt') as f:
                    for line in f:
                        temp.append([line[0], line[2]])
                x = str(source_address) + " " + str(port)+"\n"
                if not([str(source_address), str(port)] in temp):
                    z.write(x)
                    break
    if counter == 0 and port == 0:
        print("Switch4 Broadcasting.")
        H4(source_address, message, destination, 'yes')
        S5(UP, message, source_address, destination)
        H3(source_address, message, destination, 'yes')
    if counter == 0 and port == 1:
        print("Switch4 Broadcasting.")
        S1(RIGHT, message, source_address, destination)
        S5(UP, message, source_address, destination)
        H3(source_address, message, destination, 'yes')
    if counter == 0 and port == 2:
        print("Switch4 Broadcasting.")
        S1(RIGHT, message, source_address, destination)
        S5(UP, message, source_address, destination)
        H4(source_address, message, destination, 'yes')
    if counter == 0 and port == 3:
        print("Switch4 Broadcasting.")
        S1(RIGHT, message, source_address, destination)
        H3(source_address, message, destination, 'yes')
        H4(source_address, message, destination, 'yes')

def S5(port, message, source_address, destination):
    table = []
    with open('table5.txt') as f:
        for line in f:
            table.append(line)
    if(len(table) == 0):
        with open('table5.txt', 'a') as f:
            x = str(source_address) + " " + str(port)+"\n"
            f.write(x)
        table.append([source_address, port])

    counter = 0
    for address in (table):
        if str(destination) == str(address[0]):
            counter += 1
            if(int(address[2]) == UP):
                S4(UP, message, source_address, int(destination))
            if(int(address[2]) == RIGHT):
                H8(source_address, message, destination, 'yes')
            if(int(address[2]) == DOWN):
                H9(source_address, message, destination, 'yes')
        if str(source_address) != str(address[0]):
            with open('table5.txt', 'a') as z:
                temp = []
                with open('table5.txt') as f:
                    for line in f:
                        temp.append([line[0], line[2]])
                x = str(source_address) + " " + str(port)+"\n"
                if not([str(source_address), str(port)] in temp):
                    z.write(x)
                    break
    if counter == 0 and port == 1:
        print("Switch5 Broadcasting.")
        S4(DOWN, message, source_address, destination)
        H9(source_address, message, destination, 'yes')
    if counter == 0 and port == 3:
        print("Switch5 Broadcasting.")
        S4(DOWN, message, source_address, destination)
        H8(source_address, message, destination, 'yes')
    if counter == 0 and port == 2:
        print("Switch5 Broadcasting.")
        H8(source_address, message, destination, 'yes')
        H9(source_address, message, destination, 'yes')

def H1(source, message, destination, switchcall):
    source_address = 1
    if source_address == destination:
        print('H1: Message Received:', message)
    else:
        if switchcall == 'no':
            S1(UP, message, source_address, destination)
        else:
            print('H1 received Message: ', message)

def H2(source, message, destination, switchcall):
    source_address = 2
    #print(destination)
    if source_address == destination:
        print('H2: Message Received:', message)
    else:
        if switchcall == 'no':
            S1(LEFT, message, source_address, destination)
        else:
            print('H2 received Message: ', message)

def H3(source, message, destination, switchcall):
    source_address = 3
    if source_address == destination:
        print('H3: Message Received:', message)
    else:
        if switchcall == 'no':
            S4(UP, message, source_address, destination)
        else:
            print('H3 received Message: ', message)

def H4(source, message, destination, switchcall):
    source_address = 4
    if source_address == destination:
        print('H4: Message Received:', message)
    else:
        if switchcall == 'no':
            S4(RIGHT, message, source_address, destination)
        else:
            print('H4 received Message: ', message)

def H5(source, message, destination, switchcall):
    source_address = 5
    if source_address == destination:
        print('H5: Message Received:', message)
    else:
        if switchcall == 'no':
            S3(LEFT, message, source_address, destination)
        else:
            print('H5 received Message: ', message)

def H6(source, message, destination, switchcall):
    source_address = 6
    if source_address == destination:
        print('H6: Message Received:', message)
    else:
        if switchcall == 'no':
            S3(DOWN, message, source_address, destination)
        else:
            print('H6 received Message: ', message)

def H7(source, message, destination, switchcall):
    source_address = 7
    if source_address == destination:
        print('H7: Message Received: ', message)
    else:
        if switchcall == 'no':
            S2(DOWN, message, source_address, destination)
        else:
            print('H7 received Message: ', message)

def H8(source, message, destination, switchcall):
    source_address = 8
    if source_address == destination:
        print('H8: Message Received:', message)
    else:
        if switchcall == 'no':
            S5(RIGHT, message, source_address, destination)
        else:
            print('H8 received Message: ', message)

def H9(source, message, destination, switchcall):
    source_address = 9
    if source_address == destination:
        print('H9: Message Received:', message)
    else:
        if switchcall == 'no':
            S5(DOWN,message, source_address, destination)
        else:
            print('H9 received Message: ', message)

# TEST CASES
#H1(1, 'po', 2, 'no')
#H2(2, 'yo', 1, 'no')
#H1(1, 'hi', 3, 'no')
#H1(1, 'hey 7', 7, 'no')
#H1(7, '7 says hello', 1, 'no')
#H3(3, 'hey 6y', 6, 'no')
#H8(8, 'hey 5y', 5, 'no')
#H5(5, 'yo 8', 8, 'no')
#H1(1, 'hello', 4, 'no')
#H2(1, 'hello', 4, 'no')
#H2(1, 'hello', 3, 'no')
#H8(8, 'yooo', 5, 'no')
#H1(1,'hello 8', 8, 'no')
#H8(8,'hello 1', 1, 'no')

while(1):
    source = int(input('Enter Source Address: '))
    message = input('Enter the message: ')
    destination = int(input('Destination Address: '))
    eval('H'+str(source)+'('+str(source)+','+ '"'+message+'"'+','+str(destination)+','+"'no')")
    print('**************************************')