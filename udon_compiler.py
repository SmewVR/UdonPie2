import sys
import ast
import re
import udon_functions
import udon_types


class UdonCompiler:
    def __init__( ):
        print('hi')
    def udon_behaviors( ):
        return f'instance_0: %UnityEngineTransform, this'

    def data_start( ):
        return '.data_start'
    def data_end( ):
        return '.data_end'
    def export_target( ):
        return '.export Target'
    '''    # define variables with this syntax: name: $typestring, defaultvalue
        __refl_const_intnl_udonTypeID: %SystemInt64, null
        __refl_const_intnl_udonTypeName: %SystemString, null
        __0_const_intnl_SystemUInt32: %SystemUInt32, null
        __0_intnl_returnTarget_UInt32: %SystemUInt32, null
    '''
    def int( ):
        return '__refl_const_intnl_udonTypeID: %SystemInt64, null'

    def default_angle( ):
        return f'angle_0: %SystemSingle, null'
    def axis( ):
        return f'axis_0: %UnityEngineVector3, null'
    def instance( ):
        return f'instance_0: %UnityEngineTransform, this'
    def push():
        return 'PUSH'
    def pop( ):
        return 'POP'
    def push( ):
        return 'PUSH'
    def jump( ):
        return 'JUMP'
    def jump_label( ):
        return f'JUMP, 0x{addr:08x}'
    def jump_if_false( ):
        return f'JUMP_IF_FALSE, 0x{addr:08x}'
    def jump_indirect(var_name):
        return f'JUMP_INDIRECT, {var_name}'
    def extern(extern_str):
        return f'EXTERN, "{extern_str}"'
    def jump_ret_addr(ret_addr):
        return f'JUMP_INDIRECT, {ret_addr}'
    def end( ):
        return f'JUMP, 0xFFFFFFFC'
    def set_bool():
        return


    s = f'{push()}\n{push()}, axisName_0'
    print(s)



'''
.data_start
    __refl_const_intnl_udonTypeID: %SystemInt64, null
    __refl_const_intnl_udonTypeName: %SystemString, null
    __0_const_intnl_SystemUInt32: %SystemUInt32, null
    __0_intnl_returnTarget_UInt32: %SystemUInt32, null
.data_end
.code_start
    .export _start
    _start:
        PUSH, __0_const_intnl_SystemUInt32
        PUSH, __0_intnl_returnTarget_UInt32 # Function epilogue
        COPY
        JUMP_INDIRECT, __0_intnl_returnTarget_UInt32
.code_end
'''

