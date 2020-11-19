from PIL import Image, ImageFilter, ImageEnhance


class EditorEngine:

    baseImage = None
    image = None

    def __init__(self):
        self.image = None
        self.baseImage = None

    def readImage(self, path):
        try:
            self.baseImage = Image.open(path)
            self.image = Image.open(path)
        except Exception as e:
            print(e)

    # Enhance section
    def changeContrast(self, value):
        en = ImageEnhance.Contrast(self.image)
        self.image = en.enhance(value)

    def changeColor(self, value):
        en = ImageEnhance.Color(self.image)
        self.image = en.enhance(value)

    def changeBrightness(self, value):
        en = ImageEnhance.Brightness(self.image)
        self.image = en.enhance(value)
    # end of section

    # Filter Section
    def filterBlur(self):
        self.image = self.image.filter(ImageFilter.BLUR)

    def filterContour(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)

    def filterDetail(self):
        self.image = self.image.filter(ImageFilter.DETAIL)

    def filterEmboss(self):
        self.image = self.image.filter(ImageFilter.EMBOSS)

    def filterSharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
    # end of section

    def rotateImage(self, degrees):
        self.image = self.image.rotate(degrees)

    def showImage(self):
        self.image.show()

    def showBaseImage(self):
        self.baseImage.show()

    def saveImage(self, path):
        self.image.save(path)

    def getImage(self):
        return self.image

    def getBaseImage(self):
        return self.baseImage
