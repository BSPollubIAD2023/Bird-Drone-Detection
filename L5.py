# # import cv2
# # import matplotlib
# # import numpy as np
# # import pandas as pd
# #
# # matplotlib.use('AGG')
# # import matplotlib.pyplot as plt
# # import os
# #
# #
# #
# # def ramka_zrob(folder):
# #     sciezki = []
# #     etykiety = []
# #     for file in os.listdir(folder):
# #         sciezka=os.path.join(folder, file)
# #         if file.startswith("B"):
# #             label="Bird"
# #         elif file.startswith("D"):
# #             label="Drone"
# #         sciezki.append(sciezka)
# #         etykiety.append(label)
# #     return  pd.DataFrame({
# #         "Sciezka": sciezki,
# #         "Etykiety": etykiety
# #     })
# # folder_train='Dataset/train/images'
# # folder_valid='Dataset/valid/images'
# # folder_test='Dataset/test/images'
# # Ramka_train=ramka_zrob(folder_train)
# # Ramka_train.to_csv('Ramka_train.csv', sep=';', decimal=',', index=False)
# # Ramka_val = ramka_zrob(folder_valid)
# # Ramka_val.to_csv('Ramka_val.csv', sep=';', decimal=',', index=False)
# # Ramka_test = ramka_zrob(folder_test)
# # Ramka_test.to_csv('Ramka_test.csv', sep=';', decimal=',', index=False)
# #
# #
# #
# #
# #
# #
# #
# # Ramka_train["Etykiety"] = Ramka_train["Etykiety"].map({
# #     "Bird": 0,
# #     "Drone": 1
# # })
# #
# # Ramka_val["Etykiety"] = Ramka_val["Etykiety"].map({
# #     "Bird": 0,
# #     "Drone": 1
# # })
# #
# # Ramka_test["Etykiety"] = Ramka_test["Etykiety"].map({
# #     "Bird": 0,
# #     "Drone": 1
# # })
# #
# # #####
# # from PIL import Image
# # from torch.utils.data import Dataset, DataLoader
# # from torchvision import transforms
# #
# # class BirdDroneDataset(Dataset):
# #
# #     def __init__(self, dataframe, transform=None):
# #
# #         self.df = dataframe
# #         self.transform = transform
# #
# #     def __len__(self):
# #
# #         return len(self.df)
# #
# #     def __getitem__(self, idx):
# #
# #         image_path = self.df.iloc[idx]["Sciezka"]
# #         label = self.df.iloc[idx]["Etykiety"]
# #
# #         image = Image.open(image_path).convert("RGB")
# #
# #         if self.transform:
# #             image = self.transform(image)
# #
# #         return image, label, image_path
# #
# #
# # transform = transforms.Compose([
# #     transforms.Resize((256,256)),
# #     transforms.RandomHorizontalFlip(),
# #     transforms.RandomRotation(30),
# #     transforms.ToTensor()
# # ])
# #
# #
# # train_dataset = BirdDroneDataset(Ramka_train, transform)
# # val_dataset = BirdDroneDataset(Ramka_val, transform)
# # test_dataset = BirdDroneDataset(Ramka_test, transform)
# #
# #
# train_loader = DataLoader(train_dataset,
#                           batch_size=32,
#                           shuffle=True,
#                           num_workers=0)

# val_loader = DataLoader(val_dataset,
#                         batch_size=32)

# test_loader = DataLoader(test_dataset,
#                          batch_size=32)
# #
# #
# # import torch.nn as nn
# #
# class CNN(nn.Module):

#     def __init__(self):

#         super().__init__()

#         self.conv = nn.Sequential(

#             nn.Conv2d(3,32,3),  #wejscie 3 kanaly rgb, out: 16 filtrow 3x3x3
#             nn.ReLU(),  #nie wiem
#             nn.MaxPool2d(2),  #mapa cech x/2 y/2 z zostaje na 16

#             nn.Conv2d(32,64,3), #wejscie 16 (z mapy cech), 32 filtry 3x3x16
#             nn.ReLU(),
#             nn.MaxPool2d(2) #((x/2) -2 )/2,((y/2) -2 )/2 z zostaje na 32
#         )

#         self.fc = nn.Sequential(

#             nn.AdaptiveAvgPool2d((1, 1)),
#             nn.Flatten(),
#             nn.Dropout(0.3),

#             nn.Linear(64, 32),
#             nn.ReLU(),

#             nn.Linear(32, 2)
#         )

#     def forward(self,x):

#         x = self.conv(x)
#         x = self.fc(x)

#         return x
# # import torch
# # from torch import device
# #
# #
# # # ======================================================
# # # WYBÓR URZĄDZENIA (GPU lub CPU)
# # # ======================================================
# #
# # # Jeżeli komputer posiada kartę graficzną CUDA,
# # # model będzie trenowany na GPU.
# # # W przeciwnym razie użyte zostanie CPU.
# #
# # device = torch.device(
# #     "cuda" if torch.cuda.is_available() else "cpu"
# # )
# #
# # # Tworzymy model i przenosimy go na wybrane urządzenie.
# # model = CNN().to(device)
# #
# #
# # # ======================================================
# # # FUNKCJA STRATY
# # # ======================================================
# #
# # # CrossEntropyLoss jest standardową funkcją dla problemów klasyfikacji.
# # # Będzie porównywać przewidywania modelu z prawdziwymi etykietami.
# #
# # criterion = nn.CrossEntropyLoss()
# #
# #
# # # ======================================================
# # # OPTYMALIZATOR
# # # ======================================================
# #
# # # Adam będzie aktualizował wszystkie parametry sieci.
# # # model.parameters() zawiera wszystkie wagi filtrów i warstw Linear.
# # # lr = learning rate = wielkość pojedynczego kroku podczas uczenia.
# #
# # optimizer = torch.optim.Adam(
# #     model.parameters(),
# #     lr=0.001
# # )
# #
# #
# # # ==========================================
# # # LISTY DO ZAPISYWANIA HISTORII UCZENIA
# # # ==========================================
# #
# # train_losses = []
# # val_losses = []
# #
# # train_accuracies = []
# # val_accuracies = []
# #
# #
# # # ==========================================
# # # LICZBA EPOK
# # # ==========================================
# #
# # num_epochs = 3
# #
# #
# # # ==========================================
# # # PĘTLA UCZENIA
# # # ==========================================
# #
# # for epoch in range(num_epochs):
# #
# #     # -----------------------------
# #     # TRYB TRENINGOWY
# #     # -----------------------------
# #     model.train()
# #
# #     train_loss = 0
# #     train_correct = 0
# #     train_total = 0
# #
# #     # przechodzimy po batchach treningowych
# #     for batch_idx, (images, labels, paths) in enumerate(train_loader):
# #
# #         if batch_idx % 50 == 0:
# #             print(f"Batch {batch_idx}/{len(train_loader)}")
# #
# #         images = images.to(device)
# #         labels = labels.to(device)
# #
# #
# #         # wyzerowanie poprzednich gradientów
# #         optimizer.zero_grad()
# #
# #         # forward pass
# #         outputs = model(images)
# #
# #         # obliczenie błędu
# #         loss = criterion(outputs, labels)
# #
# #         # backpropagation
# #         loss.backward()
# #
# #         # aktualizacja wag
# #         optimizer.step()
# #
# #         # suma strat
# #         train_loss += loss.item()
# #
# #         # przewidywana klasa
# #         _, predicted = torch.max(outputs, 1)
# #
# #         # liczba wszystkich obserwacji
# #         train_total += labels.size(0)
# #
# #         # liczba poprawnych klasyfikacji
# #         train_correct += (predicted == labels).sum().item()
# #
# #
# #     # średnia strata dla train
# #     train_loss /= len(train_loader)
# #
# #     # accuracy dla train
# #     train_accuracy = train_correct / train_total
# #
# #
# #     # =====================================
# #     # WALIDACJA
# #     # =====================================
# #
# #     model.eval()
# #
# #     val_loss = 0
# #     val_correct = 0
# #     val_total = 0
# #
# #     # podczas walidacji nie liczymy gradientów
# #     with torch.no_grad():
# #
# #         for images, labels, paths in val_loader:
# #
# #             images = images.to(device)
# #             labels = labels.to(device)
# #
# #             outputs = model(images)
# #
# #             loss = criterion(outputs, labels)
# #
# #             val_loss += loss.item()
# #
# #             _, predicted = torch.max(outputs, 1)
# #
# #             val_total += labels.size(0)
# #
# #             val_correct += (predicted == labels).sum().item()
# #
# #
# #     # średnia strata walidacyjna
# #     val_loss /= len(val_loader)
# #
# #     # accuracy walidacyjne
# #     val_accuracy = val_correct / val_total
# #
# #
# #     # =====================================
# #     # ZAPIS HISTORII
# #     # =====================================
# #
# #     train_losses.append(train_loss)
# #     val_losses.append(val_loss)
# #
# #     train_accuracies.append(train_accuracy)
# #     val_accuracies.append(val_accuracy)
# #
# #
# #     # =====================================
# #     # PODSUMOWANIE EPOKI
# #     # =====================================
# #
# #     print(
# #         f"Epoka {epoch+1}/{num_epochs} | "
# #         f"Train Loss: {train_loss:.4f} | "
# #         f"Train Acc: {train_accuracy:.4f} | "
# #         f"Val Loss: {val_loss:.4f} | "
# #         f"Val Acc: {val_accuracy:.4f}"
# #     )
# #
# # epochs=range(1, num_epochs+1)
# # fig, ax1 = plt.subplots(figsize=(10,6))
# #
# #
# # line1,=ax1.plot(epochs, train_losses, label='Train Loss')
# # line2,=ax1.plot(epochs, val_losses, label='Val Loss')
# # ax1.set_ylabel('Loss')
# # plt.legend()
# #
# # ax2 = ax1.twinx()
# # line3,=ax2.plot(epochs, train_accuracies, '--', label='Train Accuracy')
# # line4,=ax2.plot(epochs, val_accuracies, '--', label='Val Accuracy')
# # ax2.set_ylabel('Accuracy')
# #
# # lines = [line1, line2, line3, line4]
# # labels = [line.get_label() for line in lines]
# #
# # ax1.legend(lines, labels, loc='upper left')
# # plt.title('Training history')
# #
# # plt.savefig('Accuracy_over_epochs.png')
# # plt.close()
# #
# #
# #
# # # =====================================
# # # TEST
# # # =====================================
# #
# # model.eval()
# #
# # test_loss = 0
# # test_correct = 0
# # test_total = 0
# #
# # all_predictions = []
# # all_labels = []
# # all_paths = []
# # all_probs=[]
# #
# # with torch.no_grad():
# #
# #     for images, labels, paths in test_loader:
# #
# #         images = images.to(device)
# #         labels = labels.to(device)
# #
# #         all_paths.extend(paths)
# #
# #
# #         outputs = model(images)
# #
# #
# #         loss = criterion(outputs, labels)
# #
# #         test_loss += loss.item()
# #
# #
# #         _, predicted = torch.max(outputs, 1)
# #         probs=torch.softmax(outputs, dim=1)
# #         drone_probs=probs[:,1]
# #
# #
# #         all_predictions.extend(predicted.cpu().numpy())
# #         all_labels.extend(labels.cpu().numpy())
# #         all_probs.extend(drone_probs.cpu().numpy())
# #
# #
# #         test_total += labels.size(0)
# #         test_correct += (predicted == labels).sum().item()
# #
# #
# #
# # test_loss /= len(test_loader)
# # test_accuracy = test_correct / test_total
# #
# # print(f"Test Loss: {test_loss:.4f}")
# # print(f"Test Accuracy: {test_accuracy:.4f}")
# #
# #
# #
# #
# #
# #
# #
# #
# # wyniki=pd.DataFrame({
# #     "Sciezka": all_paths,
# #     "Rzeczywista": all_labels,
# #     "Predykcja": all_predictions,
# # })
# # wyniki['Rzeczywista']=wyniki['Rzeczywista'].map({0:"Bird", 1:"Drone"})
# # wyniki['Predykcja']=wyniki['Predykcja'].map({0:"Bird", 1:"Drone"})
# #
# # macierz_pomylek = pd.crosstab(
# #     wyniki["Rzeczywista"],
# #     wyniki["Predykcja"],
# #     rownames=["True"],
# #     colnames=["Predicted"]
# # )
# #
# # import seaborn as sns
# #
# # plt.figure(figsize=(10,4))
# # sns.heatmap(macierz_pomylek, annot=True, cbar=False, fmt='d', cmap="Blues")
# # plt.savefig('Macierz_pomylek.png')
# # plt.close()
# #
# #
# # print(Ramka_train["Etykiety"].value_counts())
# # print(Ramka_val["Etykiety"].value_counts())
# # print(Ramka_test["Etykiety"].value_counts())
# #
# #
# #
# #
# # TN=len(
# #     wyniki[
# #         (wyniki['Predykcja']=="Bird") &
# #         (wyniki["Rzeczywista"]=="Bird")
# #     ]
# # ) #358
# #
# # FN=len(
# #     wyniki[
# #         (wyniki['Predykcja']=="Bird") &
# #         (wyniki["Rzeczywista"]=="Drone")
# #     ]
# # ) #345
# # TP=len(
# #     wyniki[
# #         (wyniki['Predykcja']=="Drone") &
# #         (wyniki["Rzeczywista"]=="Drone")
# #     ]
# # ) #183
# # FP=len(
# #     wyniki[
# #         (wyniki['Predykcja']=="Drone") &
# #         (wyniki["Rzeczywista"]=="Bird")
# #     ]
# # ) #3
# #
# # Precision_drone=TP/(TP+FP)
# # Recall_drone=TP/(TP+FN)
# # F1_drone=2*Precision_drone*Recall_drone/(Precision_drone+Recall_drone)
# #
# # Precision_bird=TN/(TN+FN)
# # Recall_bird=TN/(TN+FP)
# # F1_bird=2*Precision_bird*Recall_bird/(Precision_bird+Recall_bird)
# #
# # F1_macro=(F1_drone+F1_bird)/2
# # F1_wazone=(
# #     (F1_drone*pd.Series(all_labels).value_counts()[1] +F1_bird*pd.Series(all_labels).value_counts()[0])/(pd.Series(all_labels).value_counts()[1]+pd.Series(all_labels).value_counts()[0])
# # )
# #
# # metryki_drone=[Precision_drone, Recall_drone, F1_drone]
# # metryki_bird=[Precision_bird, Recall_bird, F1_bird]
# #
# # Metryki=pd.DataFrame({
# #     "Metryki-dron": metryki_drone,
# #     "Metryki-ptak": metryki_bird,
# #     "F1_srednie": F1_macro,
# #     "F1_wazone": F1_wazone
# # },
# #  index=["Precision", "Recall","F1"]
# # )
# #
# # thresholds = np.linspace(0, 1, 100)
# #
# # tpr_list = []
# # fpr_list = []
# #
# # for threshold in thresholds:
# #
# #     preds = (np.array(all_probs) >= threshold).astype(int)
# #
# #     TPs = np.sum((preds == 1) & (np.array(all_labels) == 1))
# #     TNs = np.sum((preds == 0) & (np.array(all_labels) == 0))
# #     FPs = np.sum((preds == 1) & (np.array(all_labels) == 0))
# #     FNs = np.sum((preds == 0) & (np.array(all_labels) == 1))
# #
# #     tpr = TPs / (TPs + FNs)
# #     fpr = FPs / (FPs + TNs)
# #
# #     tpr_list.append(tpr)
# #     fpr_list.append(fpr)
# #
# #
# # plt.figure(figsize=(6,6))
# #
# # plt.plot(fpr_list, tpr_list)
# # plt.plot([0,1], [0,1], '--')
# #
# # plt.xlabel("False Positive Rate")
# # plt.ylabel("True Positive Rate")
# # plt.title("ROC Curve: drone-positive")
# #
# # plt.savefig("ROC.png")
# # plt.close()
# #
# # Metryki.to_csv('Metryki.csv', sep=';', decimal=',')
# #
# # plt.figure(figsize=(10,4))
# # sns.heatmap(Metryki, annot=True, cmap='Blues', fmt='.2f', cbar=False)
# # plt.savefig('Metryki.png')
# # plt.close()
# #
# #
# # torch.save(model.state_dict(), "cnn_bird_drone_pt.pth")
# import cv2
#
# # torch.save({
# #     "model_state_dict": model.state_dict(),
# #     "optimizer_state_dict": optimizer.state_dict(),
# #     "epoch": num_epochs
# # }, "checkpoint.pth")
# wyniki["Prob_drone"]=all_probs
# wyniki_bird_idx=wyniki[(wyniki["Rzeczywista"]=="Bird")&(wyniki["Predykcja"]=="Drone")].index
# wyniki_bird_idx=np.random.choice(wyniki_bird_idx,3)
# wyniki_bird=wyniki.iloc[wyniki_bird_idx]
#
# Sciezki_bird=wyniki_bird["Sciezka"].tolist()
# Sciezki_bird
# Ptaki=[]
# for sciezka in Sciezki_bird:
#     p=cv2.imread(sciezka)
#     p=cv2.cvtColor(p, cv2.COLOR_BGR2RGB)
#     Ptaki.append(p)
#
#
# wyniki_drone_idx=wyniki[(wyniki["Rzeczywista"]=="Drone")&(wyniki["Predykcja"]=="Bird")].index
# wyniki_drone_idx=np.random.choice(wyniki_drone_idx,3)
# wyniki_drone=wyniki.iloc[wyniki_drone_idx]
#
# Sciezki_drone=wyniki_drone["Sciezka"].tolist()
# Sciezki_drone
# Drony=[]
# for sciezka in Sciezki_drone:
#     d=cv2.imread(sciezka)
#     d=cv2.cvtColor(d, cv2.COLOR_BGR2RGB)
#     Drony.append(d)
#
#
# fig, axes = plt.subplots(2, 3, figsize=(15,10))
#
#
# for i in range(3):
#
#     axes[0, i].imshow(Ptaki[i])
#
#     prob = wyniki_bird.iloc[i]["Prob_drone"]
#
#     axes[0, i].set_title(
#         f"Looks like a drone...\nP(Drone)={prob:.3f}"
#     )
#
#     axes[0, i].axis("off")
#
#
#
# for i in range(3):
#
#     axes[1, i].imshow(Drony[i])
#
#     prob = wyniki_drone.iloc[i]["Prob_drone"]
#
#     axes[1, i].set_title(
#         f"Looks like a bird...\nP(Drone)={prob:.3f}"
#     )
#
#     axes[1, i].axis("off")
#
#
# plt.tight_layout()
# plt.savefig("bledne_klasyfikacje.png")
# plt.close()
#
