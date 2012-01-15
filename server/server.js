/*****************INLINE LIBRARIES**************/
/*

Queue.js

A function to represent a queue

Created by Stephen Morley - http://code.stephenmorley.org/ - and released under
the terms of the CC0 1.0 Universal legal code:

http://creativecommons.org/publicdomain/zero/1.0/legalcode

*/

function Queue(){
var _1=[];
var _2=0;
this.getLength=function(){
return (_1.length-_2);
};
this.isEmpty=function(){
return (_1.length==0);
};
this.enqueue=function(_3){
_1.push(_3);
};
this.dequeue=function(){
if(_1.length==0){
return undefined;
}
var _4=_1[_2];
if(++_2*2>=_1.length){
_1=_1.slice(_2);
_2=0;
}
return _4;
};
this.peek=function(){
return (_1.length>0?_1[_2]:undefined);
};
};
/*******************END INLINE ***************/


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

function Session(id){
  this.SID = id;
  this.Users = [];
  this.Events = new Queue();

  this.AddPlayer = function (uid, socket) {
    Users[uid] = socket;
    Users[uid].on('event', QueueEvent);
    Users[uid].on('chat', PushMessage);
    Users[uid].on('disc', DisconnectPlayer);

    PushMessage({msg : uid + ' has joined the game.'});
  }

  this.QueueEvent = function(event) {
    Events.enqueue(event.action);
  }

  this.PushMessage = function(data){
    console.log(data.uid + ': ' + data.msg);
    for(var user in Users)
    {
      user.emit('chat', data);
    }
  }

  this.DisconnectPlayer = function(data) {
    console.log(data.uid + ' disconnecting from ' + SID);
    Users = Users.splice(Users.indexOf(data.uid), 1);
    PushMessage({msg : data.uid + ' disconnected from the game'});
  }

  this.SessionState = [];

  this.Update = function() {
    //TODO
  }

  this.PushState = function() {
    for(var user in Users)
    {
      user.emit('sync', SessionState);
    }
  }
}

var uidtemp = 0, sidtemp = 0;
function GenerateUserID() {
  uidtemp = uidtemp + 1;
  return uidtemp;
}
function GenerateSessionID() {
  sidtemp = sidtemp + 1;
  return sidtemp;
}

io.sockets.on('connection', function (socket) {
  socket.emit('ack', { uid: GenerateUserID() });
  socket.on('join', function (data) {
    console.log('User ' + data.uid + ' joining ' + data.name);

    if (sessions[data.name] == undefined)
    {
        console.log('Game ' + data.name + ' does not exist! Creating now.');
        sessions[data.name] = new Session(GenerateSessionID());
    }

    sessions[data.name].AddPlayer(data.uid, socket);
  });
});