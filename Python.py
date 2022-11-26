import snap7 #import library snap7
from snap7.util import*
from snap7.types import*
import time #import library time
def ReadMemory(plc,byte,bit,datatype): #define read memory function
    result = plc.read_area(areas['MK'],0,byte,datatype)
    if datatype==S7WLBit:
        return get_bool(result,0,1)
    elif datatype==S7WLByte or datatype==S7WLWord:
        return get_int(result,0)
    elif datatype==S7WLReal:
        return get_real(result,0)
    elif datatype==S7WLDWord:
        return get_dword(result,0)
    else:
        return None

def WriteMemory(plc, byte, bit, datatype, value): #define write memory function
    result = plc.read_area(areas['MK'],0,byte,datatype)
    if datatype==S7WLBit:
        set_bool(result,0,bit,value)
    elif datatype==S7WLByte or datatype==S7WLWord:
        set_int(result,0,value)
    elif datatype==S7WLReal:
        set_real(result,0,value)
    elif datatype==S7WLDWord:
        set_dword(result,0,value)
    plc.write_area(areas['MK'],0,byte,result)


IP = '192.168.0.1' #IP plc
RACK = 0 #RACK PLC
SLOT = 1 #SLOT PLC

plc = snap7.client.Client() #call snap7 client function
plc.connect(IP,RACK,SLOT) #connect to plc

state = plc.get_cpu_state() #read plc state run/stop/error
print(f'State:{state}') #print state plc
a = 0
b = 0
c = 0
while True:
#read memory
    readbit = ReadMemory(plc,0,0,S7WLBit) #read m0.0
    print('readbit:',readbit)
    readword = ReadMemory(plc,10,0,S7WLWord) #read mw10
    print('readbyte:',readword)
    readreal = ReadMemory(plc,15,0,S7WLReal) #read md15
    print('readreal:',readreal)
    readDword = ReadMemory(plc,20,0,S7WLDWord) #read md20
    print('readDword:',readDword)

    a = a+1
    b = b+2.4
    c = c+10
    #write memory
    WriteMemory(plc,0,3,S7WLBit,True) #write m0.3 True
    time.sleep(1) #delay 1 sec
    WriteMemory(plc,0,3,S7WLBit,False) #wite m0.3 False
    time.sleep(1) #delay 1 sec
    WriteMemory(plc,30,0,S7WLWord,a) #write mw30 value from a variable
    WriteMemory(plc,40,0,S7WLReal,b) #write md40 value from b variable
    WriteMemory(plc,50,0,S7WLDWord,c) #wite md50 value from c variable
