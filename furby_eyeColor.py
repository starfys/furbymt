import serial

def EyeWrite(command, serialPort = "/dev/tty/USB0"):
    # Try to open serial port
    ser = serial.Serial(serialPort)

    # Write command to serial port
    ser.write(command)

