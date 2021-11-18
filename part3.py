import sys as sy

def get_sys_argc():
    try:
        print("Success", file=stdout)
    except:
        print("You must import all the sys module")
    return len(sy.argv)

get_sys_argc()