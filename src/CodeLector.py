#Dependencies import
import cv2
from pyzbar import pyzbar

class Reader:
    def __init__(self) -> None:
        self.boxes = []
    def barcode(self, frame):
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            x, y , w, h = barcode.rect
            barcode_info = barcode.data.decode('utf-8')
            cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
            print(barcode_info)
            boxData = {

            }
            self.boxes.append(boxData)
            
        return frame
    def realTime(self):
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        while ret:
            ret, frame = camera.read()
            frame = self.barcode(frame)
            cv2.imshow('Barcode reader', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        camera.release()
        cv2.destroyAllWindows()
    def getBoxes(self):
        return self.boxes()

