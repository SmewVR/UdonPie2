import udon_types
import udon_functions

# .export
mat1 = udon_types.udon_types["Material"]
# .export
mat2 = udon_types.udon_types["Material"]
# .export
isGlobal = True # PUSH, __0_intnl_SystemBoolean
# isMaster: %SystemBoolean, null
isMaster = False # PUSH __0_intnl_SystemBoolean

'''
isGlobal: %SystemBoolean, null
targetObject: %UnityEngineGameObjectArray, null
mat2: %UnityEngineMaterial, null
mat1: %UnityEngineMaterial, null
'''

# x: %SystemBoolean, null

x = True
targetObject = []

print(mat1)

# .code_start ------------------------------------------------------------

# EXPORT _interact
def interact():
    if not isGlobal:
        toggle_skybox()
    elif (isGlobal):
        # EXTERN
        return udon_types.udon_types["NetworkEventTarget"]

# EXPORT day_sky
def day_sky():
    # PUSH mat1
    # PUSH targetObject
    #print(dict.keys(udon_functions.udon_functions))
    print(udon_functions.udon_functions['InstanceFunc', 'AimConstraint', 'get_gameObject', ()])
    # PUSH, __0_intnl_UnityEngineGameObject
    #print('PUSH, __0_intnl_' + udon_functions.udon_functions['InstanceFunc', 'AimConstraint', 'get_gameObject', ()])
    # EXTERN
    print(udon_functions.udon_functions['StaticFunc', 'RenderSettings', 'set_skybox', ('Material',)])

day_sky()
# EXPORT night_sky
def night_sky():
    # EXTERN
    print(udon_functions.udon_functions["set_skybox"])

# EXPORT toggle_skybox
def toggle_skybox(x):
    if (x == True):
        day_sky()
    else:
        night_sky()
    x = not x

toggle_skybox(x)
