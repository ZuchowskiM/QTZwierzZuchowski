from PIL import Image, ImageFilter, ImageEnhance, ImageFont, ImageDraw


class EditorEngine:

    baseImage = None
    image = None
    imagePath = None

    def __init__(self):
        self.image = None
        self.baseImage = None
        self.imagePath = None

    def readImage(self):
        try:
            self.baseImage = Image.open(self.imagePath)
            self.image = Image.open(self.imagePath)
        except Exception as e:
            print(e)
            raise Exception('Error reading photo')

    def resizeImage(self, newSize):
        self.image = self.image.resize(newSize)

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
        self.image = self.image.rotate(90)

    def placeText(self, text , color='black', fontSize=40):
        if color=='black':
            textFill = (0,0,0,255)
        if color=='white':
            textFill = (255,255,255,255)

        textHolder = Image.new('RGBA', self.image.size, (255,255,255,0))
        font = ImageFont.truetype("FreeMono.ttf", fontSize)
        drawContext = ImageDraw.Draw(textHolder)
        width, height = self.image.size
        drawContext.text((10,height - 50), text, font=font, fill=textFill)
        self.image = self.image.convert('RGBA')
        self.image = Image.alpha_composite(self.image,textHolder)
        self.image = self.image.convert('RGB')

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

