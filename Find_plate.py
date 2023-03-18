import torch
import cv2
import easyocr
class predict():
    def __init__(self):
        #Defining yolo models
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path='Models/LP_detector.pt')  # local model
        self.model.conf=0.6

    def extract_numbers(self, ocr_results):
        car_number = ''
        # Get the numbers out of OCR results
        for str in ocr_results:
            for char in str:
                if char.isdigit():
                    car_number += char
        return car_number

    def read_license_plate(self, img):
        # Use EasyOCR to read the license plate numbers
        reader = easyocr.Reader(['en'])
        ocr_results = reader.readtext(img, detail=0)
        if len(ocr_results) != 0:
            return self.extract_numbers(ocr_results)

    def detect_license_plate(self, img):
        # Changing the image colors
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Use YOLOv5 model for license plate detection
        plates = self.model(img, size=1080)
        list_plates = plates.pandas().xyxy[0].values.tolist()

        conf_rate = 0
        list_read_plates = []

        if len(list_plates) == 0:
            return False, conf_rate
        else:
            conf_rate = list_plates[0][4]
            for plate in list_plates:
                x = int(plate[0])
                y = int(plate[1])
                w = int(plate[2] - plate[0])
                h = int(plate[3] - plate[1])

                # Crop the license plate from the image using the coordinates
                crop_img = img[y:y + h, x:x + w]
                # Use EasyOCR to read the license plate numbers
                plate_number = self.read_license_plate(crop_img)
                if len(str(plate_number)) > 2:
                    list_read_plates.append(plate_number)
        return list_read_plates, conf_rate
def Number_plate(img):
    lp_detector = predict()
    status = lp_detector.detect_license_plate(img)
    if status != False:
        pred2, rate2 = status
        if rate2 != 0:
            return pred2, rate2
    return False











