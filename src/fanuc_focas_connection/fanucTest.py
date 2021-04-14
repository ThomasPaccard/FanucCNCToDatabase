from ctypes import *
import time

Fwlib32DLL = windll.LoadLibrary("./Fwlib32.dll")

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

class SPEEDELM(Structure):
    pass
    _fields_ =[
        ("data", c_long),
        ("dec", c_short),
        ("unit", c_short),
        ("reserve", c_short),
        ("name", c_char),
        ("suff", c_char),]

class ODBSPEED(Structure):
    pass
    _fields_=[
        ("actf", SPEEDELM),
        ("acts", SPEEDELM),]


h=c_ushort()
ret=c_short()
buf=ODBSYS()

#cnc_allclibhndl3 prototype
Fwlib32DLL.cnc_allclibhndl3.argtypes = c_char_p,c_ushort,c_long,POINTER(c_ushort)
Fwlib32DLL.cnc_allclibhndl3.restype = c_short

#cnc_rdspeed
Fwlib32DLL.cnc_rdspeed.argtypes = c_ushort, c_short, POINTER(ODBSPEED)
Fwlib32DLL.cnc_rdspeed.restype = c_short


class PyFwlib():

    def __init__(self):

        self.__fwlibHndl = c_ushort()
        self.__connected = False

    def connect(self, ip, port, timeout=1):
        """
        A simple connection to the CNC, do this before using PyFwlib instance.
        """

        ret = Fwlib32DLL.cnc_allclibhndl3(ip.encode('ascii'), port , timeout, byref(self.__fwlibHndl))

        if ret == 0:
            print("Connection successful")
            print("Socket handle: " + str(self.__fwlibHndl))
            self.__connected = True
        
        else:
            print("Connection failed")
            print("Error code :" + str(ret))

    def rdSpeed(self):
        if self.__connected == True:
            speed = ODBSPEED()
            ret = Fwlib32DLL.cnc_rdspeed(self.__fwlibHndl, -1, byref(speed))
            print("spindle speed : " + str(speed.acts.data))
            print("spindle unit : " + str(speed.acts.unit))
            return(speed.acts.data)
        else:
            print("not connected")



PyFwlib_instance = PyFwlib()
PyFwlib_instance.connect('132.207.165.127', 8193)

a = list()
"""
for k in range(10):
    vitesse = PyFwlib_instance.rdSpeed()
    a.append(vitesse)
    time.sleep(0.2)

"""
while(1):
    vitesse = PyFwlib_instance.rdSpeed()
    a.append(vitesse)
    #time.sleep(0.2)
print(a)