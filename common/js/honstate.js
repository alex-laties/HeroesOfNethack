var _state = namespace('HoN.State');

_state.WORLD = [];
_state.EVENTS = new Queue();
_state.PLAYERS = [];
_state.OBJECTS = [];

_state.Sync = function (data) {
  //init world array
  _state.WORLD = = new Array(data.x);
  for(var i = 0; i < data.x; i = i + 1)
  {
    _state.WORLD[i] = new Array(data.y);
  }
  
  //place objects into world
  var i;
}
