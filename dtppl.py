import random

def pack(appname, methname, message):

    probnumber = str(random.randrange(1000000))
    reqnumber = str(random.randrange(1000000000))
    strnumber = str(random.randrange(1000000))
    n = 0
    ipaddr = ''
    while n < 4:
        ipaddr += str(random.randrange(256)) + '.'
        n += 1
    ipaddr = ipaddr[:len(ipaddr) - 2]
    hour = str("%02d"%(random.randrange(24)))
    day = str("%02d"%(random.randrange(28) + 1))
    minute = str("%02d"%(random.randrange(60)))
    second = str("%02d"%(random.randrange(60)))
    msecond = str("%03d"%(random.randrange(1000)))
    rappname = appname[random.randrange(len(appname))]
    rmethname = methname[random.randrange(len(methname))]
    rmessage = message[random.randrange(len(message))]
    exectime = str(random.random())

    return {'Date/Time' : '2018 ' + '02 ' + day + ' ' + hour + ' ' + minute + ' ' + second + ' ' + msecond,'App name' : rappname,
            'Method name': rmethname, 'Ip-address' : ipaddr, 'Text message' : rmessage, 'Problem number' : probnumber,
            'Stream number' : strnumber, 'Request number' : reqnumber, 'Execution time' : exectime}

appname = ['Google Chrome', 'Mozilla Firefox', 'Opera', 'Internet Explorer', 'Safari']
methname = ['try hard', 'die hard', 'go ahead', 'born to cry', "let's go", "what doesn't kill you", 'blahblahblah', 'purple cucumber']
message = ['gimme money', 'go to outer space', 'slice you nice', 'rabbit hole', 'unicorns and magic', 'look at my horse',
           'cut my life into pieces', "i'm lovin' it", 'so good', 'collective unconsciousness', 'piglet', 'well done']
