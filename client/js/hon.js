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
  this.buffs = [];
  this.debuffs = [];
  this.currentHP = 0;
  this.currentMP = 0;
}

hon.Init = function () {
  
}
