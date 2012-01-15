_chat = namespace('HoN.Chat');

_chat.DEBUG = true;
_chat.DEFAULTLVL = 0;
_chat.VERBOSELVL = 1;
_chat.DEBUGLVL = 2;

_chat.Update = function(data) {
  if(data.uid == undefined)
  {
    _chat.Log(_chat.DEFAULTLVL, data.msg);
  }
}

_chat.Log = function(level, msg) {
  switch (level)
  {
    case _chat.DEFAULTLVL:

  }
}