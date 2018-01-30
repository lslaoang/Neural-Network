import socket
import sys
import struct
import re


def receiveData(s):
    data = ''
    try:
        data = s.recvfrom(65565)
    except timeout:
        data = ''
    except:
        print ("An error occured.")
        sys.exc_info()
    return data[0]

#get TOS
def getTOS(data):
    precedence = {0: "Routine", 1: "Priority", 2: "Immediate", 3: "Flash", 4: "Flash Override", 5: "CRITIC/ECF",
                  6: "Internetwork control", 7: "Network control"}
    delay = {0: "Normal delay", 1: "Low delay"}
    throughput = {0: "Normal throughput", 1: "High throughput"}
    reliability = {0: "Normal reliability", 1: "High reliability"}
    cost = {0: "Normal monetary cost", 1: "Minimize monetary cost"}

    D = data & 0x10
    D >>= 4
    T = data & 0x8
    T >>= 3
    R = data & 0x4
    R >>= 2
    M = data & 0x2
    M >>= 1

    tabs = '\n\t\t\t'
    TOS = precedence[data >> 5] + tabs + delay[D] + tabs + throughput[T] + tabs + reliability[R] + tabs + cost[M]
    return TOS

def getFlags(data):
    flagR = {0: "0-Reserved bit"}
    flagDF = {0: "0-Fragment if necessary", 1: "Do not fragment"}
    flagMF = {0: "Lost fragment", 1: "More fragments"}

    R = data & 0x8000
    R >>= 15
    DF = data & 0x4000
    DF >>= 14
    MF = data & 0x2000
    DF >>= 13

    tabs = '\n\t\t\t'
    flags = flagR[R] + tabs + flagDF[DF] + tabs + flagMF[MF]
    return flags

def getProtocol(protocolNr):
    protocolFile = open('Protocol.txt', 'r')
    protocolData = protocolFile.read()
    protocol = re.findall(r'\n' + str(protocolNr) + ' (?:.)+\n', protocolData)
    if protocol:
        protocol = protocol[0]
        protocol = protocol.replace('\n', '')
        protocol = protocol.replace(str(protocolNr), '')
        protocol = protocol.lstrip()
        return protocol

# the public network interface
HOST = socket.gethostbyname(socket.gethostname())

# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((HOST, 0))

# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

data = receiveData(s)
unpackedData = struct.unpack('!BBHHHBBH4s4s', data[:20])
#print (unpackedData)

version_IHL = unpackedData[0]
version = version_IHL >> 4

IHL = version_IHL & 0xF
TOS = unpackedData[1]
totalLength = unpackedData[2]
ID = unpackedData[3]
flags = unpackedData[4]
fragmentOffset = unpackedData[4] & 0x1FFF
TTL = unpackedData[5]
protocolNr = unpackedData[6]
checksum = unpackedData[7]
sourceAddress = socket.inet_ntoa(unpackedData[8])
destinationAddress = socket.inet_ntoa(unpackedData[9])

print ("An IP packet with the size %i was captured."%totalLength)
#print ("Raw data:" + str(data))
print ("\nParsed data")
print ("Version:\t\t" + "IPV" + str(version))
print ("Header length:\t\t" + str(IHL*4) + " bytes")
print ("Type of service:\t" + getTOS(TOS))
print ("Length:\t\t\t" + str(totalLength))
print ("ID:\t\t\t" + str(hex(ID)) + '('+str(ID) + ')')
print ("Flags:\t\t\t" + getFlags(flags))
print ("Fragment offset:\t" + str(fragmentOffset))
print ("TTL:\t\t\t" + str(TTL))
print ("Protocol:\t\t" + getProtocol(protocolNr))
print ("Checksum:\t\t" + str(checksum))
print ("Source:\t\t\t" + sourceAddress)
print ("Destination:\t\t" + destinationAddress)
#print ("Payload:\n" + str(data[20:]))


# disabled promiscuous mode
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)