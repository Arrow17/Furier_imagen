#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 17:59:16 2019

@author: francisco
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt            
from PIL import Image                      
ruta = '/home/francisco/Documentos/Semestre Enero-Junio/Optoelectronica/Furier/Code/Resultados/'

im= Image.open('prueba2.jpg')

img = cv2.imread('prueba2.jpg',0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.figure(1)
plt.imshow(im)
plt.savefig(ruta + 'Imagen_original.jpg')
plt.figure(2)
plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.savefig(ruta + 'Furier.jpg')
plt.figure(3)
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.savefig(ruta + 'Resultados.jpg')
plt.show()
