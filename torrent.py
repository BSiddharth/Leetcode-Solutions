import socket

host ='tracker.opentrackr.org' 
port = 1337
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((host, port))

data_to_send = "udp://tracker.opentrackr.org:1337/announce?info_hash=D3C1165FCCDBC8D50A2A8EC738FD45341803B75B&peer_id=JuVEwt4k2M0W0OFz1w7s&port=6888&uploaded=0&downloaded=0&left=2121770439&compact=1&event=started"
s.sendall(b'Hello, world')
data = s.recv(1024)
s.close()
print('Received', repr(data))
