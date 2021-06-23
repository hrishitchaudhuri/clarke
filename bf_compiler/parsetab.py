
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftEUAUAXEXleftANDORleftNOTAND AU AX EU EX LPAREN NOT OR PROPOSITION RPARENbool_form : NOT bool_formbool_form : bool_form AND bool_formbool_form : bool_form OR bool_formbool_form : AX bool_formbool_form : EX bool_formbool_form : bool_form AU bool_formbool_form : bool_form EU bool_formbool_form : LPAREN bool_form RPARENbool_form : PROPOSITION'
    
_lr_action_items = {'NOT':([0,2,3,4,5,7,8,9,10,],[2,2,2,2,2,2,2,2,2,]),'AX':([0,2,3,4,5,7,8,9,10,],[3,3,3,3,3,3,3,3,3,]),'EX':([0,2,3,4,5,7,8,9,10,],[4,4,4,4,4,4,4,4,4,]),'LPAREN':([0,2,3,4,5,7,8,9,10,],[5,5,5,5,5,5,5,5,5,]),'PROPOSITION':([0,2,3,4,5,7,8,9,10,],[6,6,6,6,6,6,6,6,6,]),'$end':([1,6,11,12,13,15,16,17,18,19,],[0,-9,-1,-4,-5,-2,-3,-6,-7,-8,]),'AND':([1,6,11,12,13,14,15,16,17,18,19,],[7,-9,-1,7,7,7,-2,-3,7,7,-8,]),'OR':([1,6,11,12,13,14,15,16,17,18,19,],[8,-9,-1,8,8,8,-2,-3,8,8,-8,]),'AU':([1,6,11,12,13,14,15,16,17,18,19,],[9,-9,-1,-4,-5,9,-2,-3,-6,-7,-8,]),'EU':([1,6,11,12,13,14,15,16,17,18,19,],[10,-9,-1,-4,-5,10,-2,-3,-6,-7,-8,]),'RPAREN':([6,11,12,13,14,15,16,17,18,19,],[-9,-1,-4,-5,19,-2,-3,-6,-7,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'bool_form':([0,2,3,4,5,7,8,9,10,],[1,11,12,13,14,15,16,17,18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> bool_form","S'",1,None,None,None),
  ('bool_form -> NOT bool_form','bool_form',2,'p_bf_not','parser.py',21),
  ('bool_form -> bool_form AND bool_form','bool_form',3,'p_bf_and','parser.py',26),
  ('bool_form -> bool_form OR bool_form','bool_form',3,'p_bf_or','parser.py',31),
  ('bool_form -> AX bool_form','bool_form',2,'p_bf_alsucc','parser.py',36),
  ('bool_form -> EX bool_form','bool_form',2,'p_bf_exsucc','parser.py',41),
  ('bool_form -> bool_form AU bool_form','bool_form',3,'p_bf_aluntil','parser.py',46),
  ('bool_form -> bool_form EU bool_form','bool_form',3,'p_bf_exuntil','parser.py',51),
  ('bool_form -> LPAREN bool_form RPAREN','bool_form',3,'p_bf_paren','parser.py',56),
  ('bool_form -> PROPOSITION','bool_form',1,'p_bf_prop','parser.py',60),
]