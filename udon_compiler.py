import sys
import ast
import re
from libs.my_type import *
from libs.tables import *
from libs.udon_assembly import *
from libs.udon_types import *
from libs.event_data import *

class UdonCompiler:
  var_table: VarTable
  uasm: UdonAssembly
  def_func_table: DefFuncTable
  udon_method_table: UdonMethodTable
  node: ast.AST
  current_func_ret_type: Optional[UdonTypeName]
  current_break_label: Optional[LabelName]
  current_continue_label: Optional[LabelName]

  def __init__(self, code: str) -> None:
    self.var_table = VarTable()
    self.def_func_table = DefFuncTable()
    self.uasm = UdonAssembly(self.var_table, self.def_func_table)
    self.udon_method_table = UdonMethodTable()
    self.current_func_ret_type = None
    self.current_break_label = None
    self.current_continue_label = None
    
