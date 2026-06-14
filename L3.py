# import cv2
# import matplotlib
# import numpy as np
# matplotlib.use('AGG')
# import matplotlib.pyplot as plt
#
#
#
# image_name='BTR (1).jpg'
#
# label='Bird' if image_name.startswith('BTR') else 'Drone'
#
#
# import pandas as pd
# import  os
#
#
# import os
# import cv2
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
#
#
#
# def read_polygon(txt_path):
#
#     with open(txt_path) as f:
#         line = f.readline().split()
#
#     coords = list(map(float, line[1:]))
#
#     points = np.array(coords).reshape(-1, 2)
#
#     return points
#
#
#
# def polygon_to_pixels(points, width, height):
#
#     points = points.copy()
#
#     points[:, 0] *= width
#     points[:, 1] *= height
#
#     return points.astype(np.int32)
#
#
#
# image_dir = "Dataset/train/images"
# label_dir = "Dataset/train/labels"
#
# results = []
#
# files = os.listdir(label_dir)[:10]
#
#
#
# for file in files:
#
#     image_name = file.replace(".txt", ".jpg")
#
#     image_path = os.path.join(image_dir, image_name)
#     txt_path = os.path.join(label_dir, file)
#
#     img = cv2.imread(image_path)
#
#     if img is None:
#         continue
#
#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#
#     H, W = img_rgb.shape[:2]
#
#
#     polygon = read_polygon(txt_path)
#
#
#     polygon = polygon_to_pixels(polygon, W, H)
#
#
#     area = cv2.contourArea(polygon)
#
#
#     perimeter = cv2.arcLength(polygon, True)
#
#
#     x, y, w, h = cv2.boundingRect(polygon)
#
#
#     aspect_ratio = w / h
#
#
#     M = cv2.moments(polygon)
#
#     if M["m00"] != 0:
#         cx = int(M["m10"] / M["m00"])
#         cy = int(M["m01"] / M["m00"])
#     else:
#         cx = 0
#         cy = 0
#
#
#     if image_name.startswith("BTR"):
#         label = "Bird"
#     else:
#         label = "Drone"
#
#
#     results.append({
#         "Obraz": image_name,
#         "Klasa": label,
#         "Pole powierzchni": round(area, 2),
#         "Obwód": round(perimeter, 2),
#         "Aspect ratio": round(aspect_ratio, 2),
#         "Srodek ciezkosci":np.array([cx,cy])
#     })
#
#
#
# df = pd.DataFrame(results)
#
# image_path = "Dataset/train/images/BTR (10).jpg"
# txt_path = "Dataset/train/labels/BTR (10).txt"
#
# img = cv2.imread(image_path)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#
# H, W = img.shape[:2]
#
# polygon = read_polygon(txt_path)
# polygon = polygon_to_pixels(polygon, W, H)
#
# area = cv2.contourArea(polygon)
#
# x, y, w, h = cv2.boundingRect(polygon)
#
# M = cv2.moments(polygon)
#
# cx = int(M["m10"] /(M["m00"]+(1e-5)))
# cy = int(M["m01"] /(M["m00"]+(1e-5)))
#
# img_copy = img.copy()
#
#
#
# cv2.polylines(img_copy, [polygon], True, (255,0,0), 2)
#
#
# cv2.rectangle(img_copy, (x,y), (x+w,y+h), (0,255,0), 2)
#
#
# cv2.circle(img_copy, (cx,cy), 5, (0,0,255), -1)
#
# plt.figure(figsize=(8, 8))
# plt.imshow(img_copy)
# plt.axis("off")
# plt.title("Segmentacja + Bounding Box + Centroid")
#
# plt.savefig("L3_wynik.png", dpi=300)
# plt.close()
#
# df.to_csv('tabela_l3.csv', sep=';', decimal=',', index=False)
