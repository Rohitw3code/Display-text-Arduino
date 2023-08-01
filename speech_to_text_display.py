import speech_recognition as sr
from pyfirmata import Arduino, util, STRING_DATA
import serial

port = "COM8"

board = Arduino(port)
# ser = serial.Serial(port, 115200, timeout=0)
r = sr.Recognizer()

# board.send_sysex( STRING_DATA, util.str_to_two_byte_iter('Hello!') )

def msg( text ):
    if text:
        board.send_sysex( STRING_DATA, util.str_to_two_byte_iter( text ) )


while True:
    with sr.Microphone() as mic:
        try:
            print("Silence please, calibrating...")
            r.adjust_for_ambient_noise(mic, duration=2)
            print("calibrated, speak now...")
            audio = r.listen(mic)
            text = r.recognize_google(audio)
            text = text.lower()
            print("You said "+text+"\n")
            msg(text)
            
        
            
        except sr.UnknownValueError:
            print("Could not understand audio")
            
        except sr.RequestError as e:
            print("Request error; {0}".format(e))