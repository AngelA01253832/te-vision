#Dependencies import
import cv2
import json
from pyzbar import pyzbar

class Reader:
    def __init__(self) -> None:
        self.contentList = []
        self.readCodes = set()
        
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
            
        return frame
    def realTime(self):
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        while ret:
            ret, frame = camera.read()
            frame = self.scanner(frame)
            cv2.imshow('Barcode reader', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        camera.release()
        cv2.destroyAllWindows()
    def getContentList(self):
        return self.contentList

qrcode = Reader()
qrcode.realTime()

content_list = qrcode.getContentList()
print(content_list)