# import cv2
# import matplotlib
# import numpy as np
# matplotlib.use('AGG')
# import matplotlib.pyplot as plt
#
# ptak_rgb=cv2.imread('Ptak_rgb.png')
#
# gaussian = cv2.GaussianBlur(ptak_rgb, (5,5), 0)
#
# median = cv2.medianBlur(ptak_rgb, 5)
#
# gray = cv2.cvtColor(ptak_rgb, cv2.COLOR_RGB2GRAY)
#
# laplacian = cv2.Laplacian(gray, cv2.CV_64F)
# laplacian = np.uint8(np.absolute(laplacian))
#
# plt.figure(figsize=(15,8))
# plt.subplot(2,2,1)
# plt.imshow(ptak_rgb)
# plt.title('Zwykly_rgb.png')
# plt.axis('off')
#
# plt.subplot(2,2,2)
# plt.imshow(gaussian)
# plt.title('Gaussian.png')
# plt.axis('off')
#
# plt.subplot(2,2,3)
# plt.imshow(median)
# plt.title('Median.png')
# plt.axis('off')
#
# plt.subplot(2,2,4)
# plt.imshow(ptak_rgb)
# plt.title('Laplacian.png')
# plt.axis('off')
#
# plt.savefig('Filty.png')
# plt.close()
#
# h, w = ptak_rgb.shape[:2]
#
# M = cv2.getRotationMatrix2D((w//2, h//2), 45, 1)
#
# rotated = cv2.warpAffine(ptak_rgb, M, (w, h))
#
#
# scaled = cv2.resize(ptak_rgb, None, fx=0.5, fy=0.5)
#
# flipped = cv2.flip(ptak_rgb, 1)
#
#
#
# plt.figure(figsize=(12,8))
#
# plt.subplot(2,2,1)
# plt.imshow(ptak_rgb)
# plt.title(f"Oryginał{ptak_rgb.shape}")
#
# plt.subplot(2,2,2)
# plt.imshow(rotated)
# plt.title("Obrót 45°")
#
# plt.subplot(2,2,3)
# plt.imshow(scaled)
# plt.title(f"Skalowanie{scaled.shape}")
#
# plt.subplot(2,2,4)
# plt.imshow(flipped)
# plt.title("Odbicie")
#
# for i in range(1,5):
#     plt.subplot(2,2,i)
#     plt.axis("off")
#
# plt.tight_layout()
# plt.savefig("transformacje.png", dpi=300)
#
#
#
# gray = cv2.cvtColor(ptak_rgb, cv2.COLOR_RGB2GRAY)
#
# _, thresh_global = cv2.threshold(
#     gray,
#     127,
#     255,
#     cv2.THRESH_BINARY
# )
#
#
# thresh_adaptive = cv2.adaptiveThreshold(
#     gray,
#     255,
#     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#     cv2.THRESH_BINARY,
#     11,
#     2
# )
#
# plt.figure(figsize=(12,4))
#
# plt.subplot(1,3,1)
# plt.imshow(gray, cmap='gray')
# plt.title("Gray")
#
# plt.subplot(1,3,2)
# plt.imshow(thresh_global, cmap='gray')
# plt.title("Global")
#
# plt.subplot(1,3,3)
# plt.imshow(thresh_adaptive, cmap='gray')
# plt.title("Adaptive")
#
# for i in range(1,4):
#     plt.subplot(1,3,i)
#     plt.axis("off")
#
# plt.tight_layout()
# plt.savefig("progowanie.png", dpi=300)
#
#
#
#
