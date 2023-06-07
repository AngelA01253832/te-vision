#Dependencies import
import cv2
import json
from pyzbar import pyzbar
from time import sleep

class Reader:
    def __init__(self, callback= None) -> None:
        self.contentList = []
        self.readCodes = set()
        self.isCodeReaded = False
        self.callback = callback
        self.isRunning = True
        
    def scanner(self, frame):
        codes = pyzbar.decode(frame)
        for code in codes:
            x, y , w, h = code.rect
            code_info = code.data.decode('utf-8')
            
            if code_info not in self.readCodes:
                self.readCodes.add(code_info)
                cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, code_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)                
                content = json.loads(code_info)
                #print(content)
                self.contentList.append(content)
                self.isCodeReaded = True

                if self.callback is not None:
                    self.callback(content)
        if len(codes) == 0:
            self.isCodeReaded = False
            
        return frame
    def realTime(self):
        camera = cv2.VideoCapture(0)
        while self.isRunning:
            ret, frame = camera.read()
            frame = self.scanner(frame)
            cv2.imshow('Barcode reader', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                self.stop()

            if not self.isRunning:
                break
 
        camera.release()
        cv2.destroyAllWindows()
    def getContentList(self):
        return self.contentList
    def stop(self):
        self.isRunning = False

state = False 

def visionCallback(content):
    global state 
    print(f"State:1 {state}")    
    print(f"QR detected, Content:{content}")
    state = True
    print(f"State:2 {state}")    
    sleep(1)  
    state = False
    print(f"State:3 {state}")

# qrcode = Reader(visionCallback)
# qrcode.realTime()

# content_list = qrcode.getContentList()
# print(content_list)