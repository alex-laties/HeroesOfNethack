import sys
import getopt
import socket

class WebSocket:
  
  preHandshake = '\
  HTTP/1.1 101 Web Socket Protocol Handshake \r\n\
  Upgrade: WebSocket\r\n\
  Connection: Upgrade\r\n\
  '
  
  def __init__(self, Port=8080, HostName="localhost"):
    self.Port = Port
    self.HostName = HostName
    self.Origin='WebSocket-Origin: '+'http://'+HostName+'\r\n'
    self.Socket='WebSocket-Location: '+'ws://'+HostName+':'+str(Port)+'\r\n'
    self.Handshake = self.preHandshake + self.Origin + self.Socket
    
  def start(self):
    self.stopped = False
    #initialize the socket
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.bind(("", self.Port))
    self.sock.listen(5)
    self.shaken = False
    
    data = ''
    header = ''
    
    client, address = self.sock.accept()
    while not self.stopped:
      if not self.shaken:
        header += client.recv(16)
        
        if header.find('\r\n\r\n') != -1:
          data = header.split('\r\n\r\n', 1)[1]
          self.shaken = True
          client.send(self.Handshake)
      else:
        tmp = client.recv(128)
        data += tmp;
        
        validated = []
        
        msgs = data.split('\xff')
        data = msgs.pop()
        
        for msg in msgs:
          if msg[0] == '\x00':
            validated.append(msg[1:])
        
        for v in validated:
          print v
          if v == "exit":
            self.stopped = True
            print "exiting"
          client.send('\x00' + v + '\xff')


def main():
  opts = 0
  args = 0
  try:
    opts, args = getopt.getopt(sys.argv[1:], "hp:n:", ["help", "port=", "hostname="])
  except getopt.error, msg:
    print msg
    print "for help use --help"
    sys.exit(2)
  
  port = 0;
  host = 0;
  print opts  
  for o, a in opts:
    if o in ("-h", "--help"):
      print __doc__
      sys.exit(0)
    elif o in ("--port", "-p"):
      try:
        port = int(a)
      except ValueError:
        print "port value not an int: " + a
        sys.exit(2);
    elif o in ("--hostname", "-n"):
      host = a
  
  if port != 0 and host != 0:
    print "starting server"
    srv = WebSocket(port, host)
    srv.start()
  else:
    print "port was set to: " + port
    print "host was set to: " + host
    print "breaking down and exiting"
  
if __name__ == "__main__":
  main()
