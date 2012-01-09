var _state = namespace('HoN.State');

_state.WORLD = [];
_state.EVENTS = new Queue();
_state.PLAYER = [];
_state.PLAYERS = [];
_state.OBJECTS = [];

function HoN.State.WorldObject(name, x, y) {
  this.Name = name;
  this.X = x;
  this.Y = y;
  this.onCollision = function () {};//do nothing unless overridden
  this.onInspect = function () {};
}

function HoN.State.Player(uid, playerName) {
  this.Character = [];
  this.UID = uid;
  this.Name = playerName;
}
HoN.State.Player.prototype = new HoN.State.WorldObject('player', 0, 0);


function HoN.State.Wall() {};
HoN.State.Wall.prototype = new HoN.State.WorldObject('wall', 0, 0);

function HoN.State.NPC() {};
HoN.State.NPC.prototype = new HoN.State.WorldObject('npc', 0, 0,);

_state.Sync = function (data) {
  //init world array
  _state.WORLD = = new Array(data.x);
  for(var i = 0; i < data.x; i = i + 1)
  {
    _state.WORLD[i] = new Array(data.y);
  }
  
  //place objects into world
  var objects = data.objects;
  for (obj in objects)
  {
    switch(obj.type)
    {
      case 'player':
        var player = new HoN.State.Player(obj.uid, obj.name);
        player.X = _state._getInt(obj.x);
        player.Y = _state._getInt(obj.y);
        player.Character = state._parseCharacter(obj.character);
        _state.Place(player);
        break;
      case 'wall':
        var wall = new HoN.State.Wall();
        wall.X = _state._getInt(obj.x);
        wall.Y = _state._getInt(obj.y);
        _state.Place(wall);
        break;
      case
  }
}

_state._getInt = function (number){
  if (typeof number == "string")
  {
    return parseInt(number);
  }
  
  return number;
}

_state._parseCharacter = function (character) {
  //TODO expand this with parse/validation code
  return character;
}