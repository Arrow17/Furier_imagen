#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 17:59:16 2019

@author: francisco
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
ruta = '/home/francisco/Documentos/Semestre Enero-Junio/Optoelectronica/Practica2/Furier/Code/Resultados'

img = cv2.imread('prueba1.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
rows, cols = img.shape
crow,ccol = int(rows/2) , int(cols/2)
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Fourier'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back,cmap = 'gray')
plt.title('Inversa Fourier'), plt.xticks([]), plt.yticks([])
plt.savefig(ruta + '/Resultado')
