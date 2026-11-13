import numpy as np
import matplotlib.pyplot as plt

from moabb.datasets import BNCI2014_001
from moabb.paradigms import LeftRightImagery

#-----------------------------------------------------------------------------------#

dataset = BNCI2014_001()
paradigm = LeftRightImagery()
X, y, metadata = paradigm.get_data(
    dataset=dataset,
    subjects=[1]
)

print("\n--- INFORMATIONS EEG ---")
print("Dimensions du tableau :", X.shape)
print("Nombre d'essais :", len(y))
print("Mouvements disponibles :", set(y))
print("Mouvement du premier essai :", y[0])

signal = X[0, 0, :]
frequence = 250
temps = np.arange(len(signal)) / frequence

# affichage
plt.figure(figsize=(12, 5))
plt.plot(temps, signal)
plt.title("Signal EEG - " + str(y[0]))
plt.xlabel("Temps (secondes)")
plt.ylabel("Amplitude EEG (µV)")
plt.grid(True)
plt.show()