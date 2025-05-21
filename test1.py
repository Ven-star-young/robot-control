import serial
import time

#单个舵机角度及速度控制函数
def setAngleSpeed(ser, channel, angle, speed):
    scaleValue=int((angle/180.0)*2000+500)
    channelByte=str(channel)
    angleByte=str(angle)
    speedByte=str(speed)
    command="#"+channelByte+"P"+angleByte+"T"+speedByte+"\r\n"
    print (command)
    ser.write(command)
    ser.flush()

#两个舵机角度及速度控制函数
def setAngleSpeed2(ser,channel1, angle1, channel2, angle2, speed):
    scaleValue1=int((angle1/180.0)*2000+500)
    scaleValue2=int((angle2/180.0)*2000+500)
    angleByte1=str(angle1)
    angleByte2=str(angle2)
    speedByte=str(speed)
    command="#"+str(channel1)+"P"+angleByte1+"#"+str(channel2)+"P"+angleByte2+"T"+speedByte
    print(command)
    ser.write(command)
    ser.flush()