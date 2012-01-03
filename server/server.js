var app = require('http').createServer(handler),
  io = require('socket.io').listen(app),
  fs = require('fs');

var index = process.argv[2] || '/var/www/index.html';

app.listen(80);

function handler (req, res) {
  fs.readFile(index, 
  function (err, data) {
    if(err){
      res.writeHead(500);
      return res.end('Error loading index.html');
    }

    res.writeHead(500);
    res.end(data);
  });
}

io.sockets.on('connection', function (socket) {
  socket.emit('news', { hello: 'world' });
  socket.on('my other event', function (data) {
    console.log(data);
  });
});
