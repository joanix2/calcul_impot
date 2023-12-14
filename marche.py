import matplotlib.pyplot as plt
import numpy as np

# Création des données
prix = np.linspace(0, 10, 100)  # Gamme de prix
offre = 2 + prix  # Fonction d'offre (exemple)
demande = 10 - 2 * prix  # Fonction de demande (exemple)

# Tracé des courbes d'offre et de demande
plt.figure(figsize=(8, 6))
plt.plot(prix, offre, label='Offre', color='blue')
plt.plot(prix, demande, label='Demande', color='red')

# Ajout de titres et de légendes
plt.title('Courbes d\'offre et de demande')
plt.xlabel('Prix')
plt.ylabel('Quantité')
plt.legend()

# Affichage du graphique
plt.grid(True)
plt.show()

###################################################################

# Création des données
prix = np.linspace(0, 10, 100)  # Gamme de prix
offre = 2 + prix  # Offre initiale
offre_augmentee = 4 + prix  # Offre augmentée

# Tracé des courbes d'offre et de demande
plt.figure(figsize=(8, 6))
plt.plot(prix, offre, label='Offre initiale', color='blue')
plt.plot(prix, offre_augmentee, label='Offre augmentée', color='green')

# Ajout de titres et de légendes
plt.title('Effet d\'une augmentation de l\'offre')
plt.xlabel('Prix')
plt.ylabel('Quantité')
plt.legend()

# Affichage du graphique
plt.grid(True)
plt.show()

###################################################################

# Création des données
prix = np.linspace(0, 10, 100)  # Gamme de prix
demande = 10 - 2 * prix  # Demande initiale
demande_diminuee = 8 - 2 * prix  # Demande diminuée

# Tracé des courbes d'offre et de demande
plt.figure(figsize=(8, 6))
plt.plot(prix, demande, label='Demande initiale', color='red')
plt.plot(prix, demande_diminuee, label='Demande diminuée', color='orange')

# Ajout de titres et de légendes
plt.title('Effet d\'une diminution de la demande')
plt.xlabel('Prix')
plt.ylabel('Quantité')
plt.legend()

# Affichage du graphique
plt.grid(True)
plt.show()

###################################################################

# Création des données
quantite = np.linspace(0, 10, 100)  # Gamme de quantités
offre = -5 + quantite  # Offre
demande = 10 - 2 * quantite  # Demande
plafond_loyers = np.full_like(quantite, -1)  # Plafond des loyers

# Tracé des courbes d'offre, demande et plafond des loyers
plt.figure(figsize=(8, 6))
plt.plot(quantite, offre, label='Offre', color='blue')
plt.plot(quantite, demande, label='Demande', color='red')
plt.plot(quantite, plafond_loyers, label='Plafond des loyers', linestyle='--', color='green')

# Ajout de titres et de légendes
plt.title('Impact d\'un plafond des loyers')
plt.xlabel('Quantité')
plt.ylabel('Prix')
plt.legend()

# Affichage du graphique
plt.grid(True)
plt.show()