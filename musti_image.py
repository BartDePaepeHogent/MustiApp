import os
from datetime import datetime
import numpy as np
from PIL import Image, ImageOps

class MustiImage:

    def __init__(self):
        self.load_and_sort_images()
        self.offset = 0
        self.imageName = ""
        self.timestampFiles = []


    def load_and_sort_images(self):
        self.dirFiles = os.listdir("nieuw")
        self.dirFiles.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
        self.dirFiles.reverse()
        for k, v in enumerate(self.dirFiles):
            work_datetime = datetime.strptime(v, '%Y%m%d_%H%M%S')
            self.timestampFiles.append(work_datetime.timestamp())


    def load_musti_image_for_datetime(self, input_datetime, offset):

        input_timestamp = input_datetime.timestamp()

        index = offset
        while (input_timestamp < self.timestampFiles[index]) and (index < (len(self.timestampFiles) - 1)):
            index += 1

        workFile = self.dirFiles[index]
        workImage = Image.open(os.path.join("nieuw", workFile))
        self.offset = index
        return workImage

    def preprocess_image(raw_image):
        # fotos omzetten in grijswaarde of 2 dimensionele array ipv 3x2
        beeld_grijs = ImageOps.grayscale(raw_image)

        # fotos resizen voor leesbaarheid tijdens testen, en eventueel voor latere experimenten
        beeld_formaat = beeld_grijs.resize((beeld_grijs.width // 1, beeld_grijs.height // 1))

        # fotos omzetten naar numpy array
        data_2dim = np.asarray(beeld_formaat, dtype=np.uint8)
        data = data_2dim.flatten()
        return data

    def getOffset(self):
        return self.offset

    def getImageName(self):
        return self.dirFiles[self.offset]
