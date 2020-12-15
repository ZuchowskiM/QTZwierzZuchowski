import EditorEngine as EditorEngine

if __name__ == '__main__':
    editEngine = EditorEngine.EditorEngine()
    editEngine.imagePath = 'lena2.jpg'
    editEngine.readImage()
    editEngine.changeBrightness(1.5)
    editEngine.filterBlur()
    editEngine.rotateImage(30)
    editEngine.placeText('TAK no cos', fontSize=25)
    editEngine.showImage()
    editEngine.showBaseImage()
