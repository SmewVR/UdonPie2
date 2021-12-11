




variables = []


def make_code_seg(self) -> str:
    ret_code: str = f'.code_start\n\n'

    for variable in variables:
        ret_code += '.export '+variable+'\n'
    ret_code += '\n'
    ret_code += f'.code_end\n'
    return ret_code
