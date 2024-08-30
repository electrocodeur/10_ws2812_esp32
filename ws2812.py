"""from machine import Pin
from neopixel import NeoPixel

pin = Pin(14, Pin.OUT)   # définir une broche en sortie pour piloter les NeoPixels
pixels = NeoPixel(pin, 24)   # créer un pilote NeoPixel sur la broche pour 24 pixels

pixels[0] = [64,154,227]    # définir la couleur du pixel
pixels[1] = [128,0,128]
pixels[2] = [50,150,50]
pixels[3] = [255,30,30]
pixels[4] = [0,128,255]
pixels[5] = [99,199,0]
pixels[6] = [128,128,128]
pixels[7] = [255,100,0]
pixels[8] = [64,154,227]   
pixels[9] = [128,0,128]
pixels[10] = [50,150,50]
pixels[11] = [255,30,30]
pixels[12] = [0,128,255]
pixels[13] = [99,199,0]
pixels[14] = [128,128,128]
pixels[15] = [255,100,0]
pixels[16] = [64,154,227]    
pixels[17] = [128,0,128]
pixels[18] = [50,150,50]
pixels[19] = [255,30,30]
pixels[20] = [0,128,255]
pixels[21] = [99,199,0]
pixels[22] = [128,128,128]
pixels[23] = [255,100,0]
pixels.write()              # envoyer les données à tous les pixels

"""
from machine import Pin
import neopixel
import time
import random

# Définir le nombre de pixels pour la lumière courante
num_pixels = 24

# Définir la broche de données pour la bande LED RGB
data_pin = Pin(14, Pin.OUT)

# Initialiser l'objet bande LED RGB
pixels = neopixel.NeoPixel(data_pin, num_pixels)

# Boucle continue de la lumière courante
while True:
    for i in range(num_pixels):
        # Générer une couleur aléatoire pour le pixel actuel
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Allumer le pixel actuel avec la couleur aléatoire
        pixels[i] = color

        # Mettre à jour l'affichage de la bande LED RGB
        pixels.write()

        # Éteindre le pixel actuel
        pixels[i] = (0, 0, 0)

        # Attendre une période de temps pour contrôler la vitesse de la lumière courante
        time.sleep_ms(100)
        
