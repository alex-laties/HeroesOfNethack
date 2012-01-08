var _con = namespace('HoN.Connection');

var _msg = namespace('HoN.MSG');
_msg.CHAT = 'chat';
_msg.EVENT = 'event';
_msg.STAT = 'stat';
_msg.DISC = 'disc';

_con.HOST = 'http://aperaturetesting.com';
_con.PORT = '80';
_con.SOCK = '';
_con.LIVE = false;
_con.SEND_QUEUE = new Queue();


_con.Connect = function () {
  console.log('attempting to connect to ' + _con.HOST +':'+ _con.PORT);
  _con.SOCK = io.connect(_con.HOST +':'+ con.PORT);
  _con.SOCK.on('ack', _con.Connected);
 }
 
 _con.Connected = function(data) {
  if(!data.success)
  {
    console.log('connection unsuccessful');
    console.log(data.msg);
  }
  
  console.log('connection successful!');
  _con.LIVE = true;
  _con.SOCK.on('state', HoN.State.Sync);
  _con.SOCK.on('events', HoN.State.Update);
  _con.SOCK.on('alert', HoN.Alert);
  _con.SOCK.on('chat', HoN.Chat.Update);
  _con.SOCK.emit('sync', { uID : HoN.USERID });
  
 }
 
 _con.Send = function(type, data) {
  if (! _con.LIVE)
  {
    _con.SEND_QUEUE.enqueue( { t : type, d : data } );
  }
  
  //clear queue
  var temp = '';
  while(! _con.SEND_QUEUE.isEmpty())
  {
    temp = _con.SEND_QUEUE.dequeue();
    _con.SOCK.emit(temp.t, temp.d);
  }
  
  //send current message
  _con.SOCK.emit(type, data);
}