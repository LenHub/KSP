from irc import IRC
import time

irc = IRC('#EpiKnet')
irc.connect('irc.epiknet.org','Philippe')  #irc.epiknet.org

time.sleep(5)
irc.send('Salut MEC')
time.sleep(2)
while True:
    time.sleep(1)
    m = irc.recv()
    id = m.split('!')[0]
    id = id.lstrip(':')

    messages = m.split(' :')
    message = messages[-1]
    message = message.strip('\r\n')
    if m.find('PING') != -1:
        irc.ping()
        message = ''

    if len(message) != 0:

        if message.find('JOIN') != -1:
            print(id, 'a rejoint le channel')

        elif message == ' Je suis pas ton pote MEC' and id == 'Terrance':
            irc.send('Je suis pas ton mec MON GARS')
            time.sleep(1)
            #print(id, '>', message)

        elif message == ' Je suis pas ton mec MON GARS' and id == 'Terrance':
            irc.send('Je suis pas ton gars MON POTE')
            time.sleep(1)
            #print(id, '>', message)

        elif message == ' Je suis pas ton gars MON POTE' and id == 'Terrance':
            irc.send('Je suis pas ton pote MEC')
            time.sleep(1)
            #print(id, '>', message)

        else:
            # print(rawmess)
            print(id, '>', message)


