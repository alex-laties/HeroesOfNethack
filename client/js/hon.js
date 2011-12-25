var hon = namespace('HoN');

hon.Character = new function (_name, _hp, _mp, _agi, _agiG, _int, _intG, _str, _strG, _ab1, _ab2, _ab3, _ab4) {
  this.name = _name;
  this.hp = _hp;
  this.mp = _mp;
  this.agility = _agi;
  this.agiG = _agiG;
  this.intel = _int;
  this.intG = _intG;
  this.strength = _str;
  this.strG = _strG;
  this.a1 = _ab1;
  this.a2 = _ab2;
  this.a3 = _ab3;
  this.a4 = _ab4;
  this.items = [];
  this.buffs = [];
  this.debuffs = [];
  this.currentHP = 0;
  this.currentMP = 0;
}

hon.Init = function () {
  
}

hon.PrintState = function () {
  $("name")[0].textContent("Name: " + HoN.State.player.name);
  $("hp")[0].textContent("HP: " + HoN.State.player.currentHP + "/" + HoN.State.player.hp);
  $("mp")[0].textContent("MP: " + HoN.State.player.currentMP + "/" + HoN.State.player.mp);
  $("agi")[0].textContent("Agility: " + HoN.State.player.agility);
  $("int")[0].textContent("Intelligence: " + HoN.State.player.intel);
  $("str")[0].textContent("Strength: " + HoN.State.player.strength);
  
  //TODO print items and abilities
}