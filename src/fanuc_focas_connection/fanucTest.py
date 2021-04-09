from ctypes import *

mylib = windll.LoadLibrary("./Fwlib32.dll")

class ODBSYS(Structure):
    pass
    _fields_ =[
    ("dummy", c_ushort),
    ("max_axis", c_char*2),
    ("cnc_type", c_char*2),
    ("mt_type",c_char*2),
    ("series",c_char*4),
    ("version",c_char*4),
    ("axes",c_char*2),]

h=c_ushort()
pt=pointer(h)
ret=c_short()
buf=ODBSYS()

#cnc_allclibhndl3 prototype
mylib.cnc_allclibhndl3.argtypes = c_char_p,c_ushort,c_long,POINTER(c_ushort)
mylib.cnc_allclibhndl3.restype = c_short

#cnc_allclibhndl3 prototype


ret=mylib.cnc_allclibhndl3(b'192.168.0.100',8193,1,byref(h))
print(ret)

