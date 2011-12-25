state = namespace('HoN.State');

state.player = [];
state.world = [];
state.worldID = -1;

state.Init = function ()
{
  state.getWorld();
}

state.getWorld = function() {
  var worker = new Worker("world_worker.js");
  worker.onmessage = function (event) {
    HoN.State.world = event.data.world;
    HoN.State.worldID = event.data.id;
  }
}