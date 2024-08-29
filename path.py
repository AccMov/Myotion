import os

MyotionPath = os.getcwd()
ImagePath = MyotionPath + "/images"
IconPath = ImagePath + "/icons"


def checkValidPath(fpath):
    return os.path.exists(fpath)
