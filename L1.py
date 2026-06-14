# import cv2
# import matplotlib
# import numpy as np
# import matplotlib.pyplot as plt
# matplotlib.use('AGG')
# #ptak
# image_path_bird = "Dataset/train/images/BTR (1).jpg"
#
#
# plt.figure(figsize=(10,4))
# ptak = cv2.imread(image_path_bird)
# ptak_rgb = cv2.cvtColor(ptak, cv2.COLOR_BGR2RGB)
# plt.imshow(ptak_rgb)
# plt.title("Oryginalny obraz - ptak")
# plt.axis("off")
# plt.savefig('Ptak_rgb.png')
# plt.close()
# #dron
# image_path_dron="Dataset/train/images/DTR (4437).jpg"
# dron=cv2.imread(image_path_dron)
# dron_rgb=cv2.cvtColor(dron, cv2.COLOR_BGR2RGB)
# plt.figure(figsize=(10,4))
# plt.imshow(dron_rgb)
# plt.title("Oryginalny obraz - dron")
# plt.axis("off")
# plt.savefig('dron_rgb.png')
# plt.close()
#
#
# #przestrzenie barw
#
# ptak_hsv=cv2.cvtColor(ptak, cv2.COLOR_RGB2HSV)
# ptak_gray=cv2.cvtColor(ptak, cv2.COLOR_RGB2GRAY)
# plt.figure(figsize=(10,4))
# plt.subplot(1,3,1)
# plt.imshow(ptak_rgb)
# plt.title("Ptak w rgb ")
# plt.axis("off")
# plt.subplot(1,3,2)
# plt.imshow(ptak_hsv)
# plt.title('Ptak w hsv')
# plt.axis("off")
# plt.subplot(1,3,3)
# plt.imshow(ptak_gray, cmap='gray')
# plt.title('Ptak szary')
# plt.axis("off")
# plt.savefig('rgb_hsv_gray.png')
# plt.close()
#
# #samo hsv
#
# H = ptak_hsv[:,:,0]
# S = ptak_hsv[:,:,1]
# V = ptak_hsv[:,:,2]
#
# plt.figure(figsize=(12,4))
#
# plt.subplot(1,3,1)
# plt.imshow(H, cmap='gray')
# plt.title("Kanał H")
#
# plt.subplot(1,3,2)
# plt.imshow(S, cmap='gray')
# plt.title("Kanał S")
#
# plt.subplot(1,3,3)
# plt.imshow(V, cmap='gray')
# plt.title("Kanał V")
#
# plt.savefig("HSV_kanaly.png")
#
#
# #poziomy szarosci
# poziomy = [256, 64, 16, 4]
#
# plt.figure(figsize=(12,8))
#
# for i, level in enumerate(poziomy):
#
#     quant = (
#         ptak_gray // (256 // level)
#     ) * (256 // level)
#
#     plt.subplot(2,2,i+1)
#     plt.imshow(quant, cmap='gray')
#     plt.title(f"{level} poziomów")
#     plt.axis("off")
#
# plt.savefig("kwantyzacja_porownanie.png")
# plt.close()
#
#
#
# plt.figure(figsize=(10,4))
# plt.hist(ptak_gray.ravel(), bins=256,histtype='step', linewidth=2,color='blue', label='Przed')
# plt.hist(quant.ravel(), bins=256,histtype='step',linewidth=2, color='red', label='Po' )
# plt.title('Poziomy-jasnosci-histogram-pikseli')
# plt.legend()
# plt.tight_layout()
# plt.xlabel('Jasnosc')
# plt.ylabel('Liczba_pikseli')
# plt.savefig('Poziomy-jasnosci-histogram-pikseli.png')
# plt.close()