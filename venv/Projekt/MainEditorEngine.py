import EditorEngine as EditorEngine

if __name__ == '__main__':
    editEngine = EditorEngine.EditorEngine()
    editEngine.readImage('lena2.jpg')
    editEngine.changeBrightness(1.5)
    editEngine.filterBlur()
    editEngine.rotateImage(30)
    editEngine.showImage()
    editEngine.showBaseImage()
