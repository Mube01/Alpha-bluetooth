import bluetooth
from alpha_1s import *
from alpha_1s import Command
import eel
eel.init('web')
def action_add(servo_id,angle,r_time,f_time):
    id = int_to_bytes(servo_id)
    ang = b'('
    r = int_to_bytes(r_time)
    f = int_to_bytes(f_time)
    command = b'\x22'
    param = [id,ang,r,f]
    msg = message(command,param)
    return msg 
@eel.expose
def main(servo_id,angle,r_time,f_time):
    msg = action_add(servo_id,angle,r_time,f_time)
    bd_addr = "88:1B:99:09:E8:96"
    if bd_addr:
        port = 6
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((bd_addr, port))
        print('Connected')
        print(Command.alpha_parser(msg))
        sock.settimeout(60.0)
        sock.send(msg)
        response = sock.recv(1024)
        print(Command().get(response))
        print('Sent data')
        return 0


def message(command, parameters):
    header = b'\xFB\xBF'
    end = b'\xED'
    parameter = b''.join(parameters)
    # len(header + length + command +parameters + check)
    length = bytes([len(parameters) + 5])
    data = [command, length]
    data.extend(parameters)
    check = bytes([sum(ord(x) for x in data)])
    return header+length+command+parameter+check+end
def discover():
    print("searching ...")
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("found %d devices" % len(nearby_devices))

    for addr, name in nearby_devices:
        if name == "ALPHA1_E896":
            return addr

eel.start('index.html')  