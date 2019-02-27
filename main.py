from kivy.app import App
from kivy.graphics.texture import Texture
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
import cv2
import numpy as np


class Manager(ScreenManager):
    pass

class Tela(Screen):
    def __init__(self, **kwargs):
        super(Tela, self).__init__(**kwargs)
        # self.frame = cv2.imread('image.jpg', cv2.IMREAD_COLOR)
        self.processando()

    def processando(self):
        self.frame = cv2.imread('data//image.jpg', cv2.IMREAD_GRAYSCALE)
        _, threshold = cv2.threshold(self.frame, 200, 250, cv2.THRESH_BINARY)
        _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        self.frame = threshold

        for cnt in contours:
            approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
            # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)


    def tipo(self, *args):
        self.img = cv2.flip(self.frame, 0)
        self.img = self.img.tostring()
        print(type(self.img))
        tex = Texture.create(size=(self.frame.shape[1], self.frame.shape[0]), colorfmt='bgr')
        # para o blit_buffer() quando estamos trabalhando com formato de cores
        # gray_scale é necessário que que o colorfmt seja "luminance", pois o
        # formato "bgr" tradicional do opencv irá travar o programa.
        tex.blit_buffer(self.img, colorfmt='luminance', bufferfmt='ubyte')
        print(type(tex))
        self.ids.pic.texture = tex

class Principal(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    Principal().run()
