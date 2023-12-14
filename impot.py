import tkinter as tk
from tkinter import ttk, messagebox
import math

import tkinter as tk
from tkinter import ttk

class Tranche(tk.Frame):
    def __init__(self, parent, from_value=0, percent_value=0, addTo=False):
        super().__init__(parent)

        self.from_var = tk.StringVar(value=str(from_value))
        self.percent_var = tk.StringVar(value=str(percent_value))

        self.label_from = ttk.Label(self, text="From:")
        self.label_from.grid(row=0, column=0, padx=5, pady=5)

        self.spin_from = ttk.Spinbox(self, from_=0, to=float('inf'), increment=1, width=10, textvariable=self.from_var)
        self.spin_from.grid(row=0, column=1, padx=5, pady=5)

        self.spin_percent = ttk.Spinbox(self, from_=0, to=100, increment=1, width=5, textvariable=self.percent_var)
        self.spin_percent.grid(row=0, column=2, padx=5, pady=5)

        self.label_percent = ttk.Label(self, text="%")
        self.label_percent.grid(row=0, column=3, padx=5, pady=5)

        if addTo :
            self.label_to = ttk.Label(self, text="To:")
            self.label_to.grid(row=0, column=4, padx=5, pady=5)

    # Définition des getters
    def get_from_value(self):
        return float(self.from_var.get())

    def get_percent_value(self):
        return float(self.percent_var.get())

    # Définition des setters
    def set_from_value(self, value):
        self.from_var.set(str(value))

    def set_percent_value(self, value):
        self.percent_var.set(str(value))

class CalculateurTranche(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Les limites des tranches d'imposition
        self.tranches = [0, 10777, 27479, 78570, 168994]
        
        # Les taux d'imposition correspondants
        self.taux_imposition = [0.0, 0.11, 0.3, 0.41, 0.45]

        self.tranches_ui = []

        self.info_enfant = ttk.Label(self, text="Barème 2023")
        self.info_enfant.pack()

        self.frame = tk.Frame(self)
        self.frame.pack()

        for i, from_value in enumerate(zip(self.tranches, self.taux_imposition)):
            is_last = i == len(self.tranches) - 1
            tranche = Tranche(self.frame, from_value=from_value[0], percent_value=from_value[1]*100, addTo=not is_last)
            tranche.pack(padx=10, pady=5, side=tk.LEFT)

            self.tranches_ui.append(tranche)

    def get_tranches(self):
        res = []
        for tranche in self.tranches_ui:
            res.append([tranche.get_from_value(), tranche.get_percent_value()])

        return res

    def calcule_tranches(self, revenu):
        tranches = self.get_tranches()

        impot = 0
        text = ""
        nb_tranche = 0
        
        for i in range(len(tranches) - 1):
            nb_tranche += 1
            tranche_inf = tranches[i]
            tranche_sup = tranches[i+1]

            impot_partiel = (min(revenu, tranche_sup[0]) - tranche_inf[0]) * tranche_inf[1]/100
            around_impot_partiel = math.floor(impot_partiel)
            impot += around_impot_partiel

            text_partiel = f"Tranche {i + 1}: {min(revenu, tranche_sup[0])} - {tranche_inf[0]} x {tranche_inf[1]/100} = {around_impot_partiel}"
            text += text_partiel

            if revenu <= tranche_sup[0]:
                break
            else:
                text += "\n"

        text += "\n" + " + ".join([f"Tranche {i+1}" for i in range(nb_tranche)]) + f" = {impot}\n\n"

        return impot, text

class Foyer(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # Création de tk.StringVar avec une valeur par défaut
        self.etat_revenu = tk.StringVar()
        self.etat_revenu.set("32000")
        self.etat_abattement = tk.StringVar()
        self.etat_abattement.set("10")
        self.etat_parts = tk.StringVar()
        self.etat_parts.set("1")

        # Créer et positionner les sélecteurs de nombres et les étiquettes
        self.etiquette_revenu = ttk.Label(self, text="Revenu par ans:")
        self.etiquette_revenu.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

        self.champ_revenu = ttk.Spinbox(self, from_=0, to=float('inf'), increment=1, width=10, textvariable=self.etat_revenu)
        self.champ_revenu.grid(row=0, column=1, padx=10, pady=10)

        self.etiquette_abattement = ttk.Label(self, text="Abattement (en %):")
        self.etiquette_abattement.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

        self.champ_abattement = ttk.Spinbox(self, from_=0, to=float('inf'), increment=1, width=10, textvariable=self.etat_abattement)
        self.champ_abattement.grid(row=1, column=1, padx=10, pady=10)

        self.info_enfant = ttk.Label(self, text="1 demi-part pour chacun des 2\npremiers enfants à charge.\n1 part entière à partir du 3.")
        self.info_enfant.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        self.etiquette_parts = ttk.Label(self, text="Nombre de parts:")
        self.etiquette_parts.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)

        self.champ_parts = ttk.Spinbox(self, from_=1, to=float('inf'), increment=0.5, width=10, textvariable=self.etat_parts)
        self.champ_parts.grid(row=3, column=1, padx=10, pady=10)

    # Définition des getters
    def get_revenu(self):
        return float(self.etat_revenu.get())

    def get_abattement(self):
        return float(self.etat_abattement.get())

    def get_parts(self):
        return float(self.etat_parts.get())

    # Définition des setters
    def set_revenu(self, value):
        self.etat_revenu.set(str(value))

    def set_abattement(self, value):
        self.etat_abattement.set(str(value))

    def set_parts(self, value):
        self.etat_parts.set(str(value))

class Deduction(tk.Frame):
    def __init__(self, parent, montant=1000, taux_abatement=50, limite_exoneration=0):
        super().__init__(parent)
        self.parent = parent
        
        self.montant_var = tk.DoubleVar(value=montant)
        self.taux_abatement_var = tk.DoubleVar(value=taux_abatement)
        self.limite_exoneration_var = tk.DoubleVar(value=limite_exoneration)
        
        # Spinbox pour montant, taux d'abatement et limite d'exonération
        ttk.Label(self, text="Montant:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        ttk.Spinbox(self, from_=0, to=float('inf'), increment=1, textvariable=self.montant_var).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self, text="Taux d'abatement (en %):").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        ttk.Spinbox(self, from_=0, to=float('inf'), increment=0.1, textvariable=self.taux_abatement_var).grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self, text="Limite d'exonération:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        ttk.Spinbox(self, from_=0, to=float('inf'), increment=1, textvariable=self.limite_exoneration_var).grid(row=2, column=1, padx=5, pady=5)

        # Bouton pour supprimer la déduction
        ttk.Button(self, text="Supprimer", command=lambda: self.remove()).grid(row=3, column=0, columnspan=2, pady=5)

    # Définition des getters
    def get_montant(self):
        return self.montant_var.get()
    
    def remove(self):
        self.parent.remove_deduction(self)
        self.destroy()

    def get_taux_abatement(self):
        return self.taux_abatement_var.get()

    def get_limite_exoneration(self):
        return self.limite_exoneration_var.get()
    
    def get_deduction(self):
        return {
            "montant": self.get_montant(),
            "abattement": self.get_taux_abatement(),
            "limite": self.get_limite_exoneration()
        }

    # Définition des setters
    def set_montant(self, value):
        self.montant_var.set(value)

    def set_taux_abatement(self, value):
        self.taux_abatement_var.set(value)

    def set_limite_exoneration(self, value):
        self.limite_exoneration_var.set(value)

class ListeDeductions(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.deductions = []
        
        # Bouton pour ajouter une nouvelle déduction
        ttk.Button(self, text="Ajouter une déduction", command=self.ajouter_deduction).pack(pady=10)
        
    def ajouter_deduction(self):
        nouvelle_deduction = Deduction(self)
        nouvelle_deduction.pack(pady=10, side=tk.LEFT)
        self.deductions.append(nouvelle_deduction)

    def remove_deduction(self, deduction):
        self.deductions.remove(deduction)

    def get_deductiuon_list(self):
        return [deduction.get_deduction() for deduction in self.deductions]
    
    def get_deduction_charges(self, revenu):
        liste_somme_charges = []
        text = ""
        charges = self.get_deductiuon_list()

        for i, charge in enumerate(charges):
            montant = charge["montant"]
            abattement = charge["abattement"]
            limite = charge["limite"]

            abat = abattement/100
            m = montant*abat
            arround_m = math.floor(m)

            text += f"Déduction {i} : {montant} x {abat} = {m} = {arround_m}\n"
            if arround_m > limite and limite != 0:
                text += f"Déduction {i} : min({arround_m}, {limite}) = {limite}\n"
            deduction = arround_m if limite == 0 else min(arround_m, limite)
            liste_somme_charges.append(deduction)

        if liste_somme_charges != []:
            s = sum(liste_somme_charges)
            text += " + ".join([f"Déduction {i}" for i in range(len(liste_somme_charges))]) + f" = {s}\n"
            revenu_abattement = revenu - s
            text += f"Revenu après déduction des charges : {revenu} - {s} = {revenu_abattement}\n"
        else:
            revenu_abattement = revenu

        return revenu_abattement, text

##################################################################################################

def calcul_revenu_apres_abattement(revenu, taux_abattement):
    revenu_apres_abattement = revenu * (1 - taux_abattement / 100)
    arrond_r = math.floor(revenu_apres_abattement)

    calcul = f"{revenu} x (1 - {taux_abattement / 100}) = {revenu_apres_abattement} = {arrond_r}"

    return arrond_r, calcul

def get_credit_impot(montant, taux=50, limite=None):
    credit = montant
    text_initial = f"{montant}"

    if limite is not None and limite != '' and limite > montant:
        credit = limite
        text_initial = f"min({montant},{limite})"

    res = credit * taux / 100
    text_final = f"{text_initial} x {taux/100} = {res}"

    return res, text_final

##################################################################################################

class CalculateurImpotUI:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Calculateur d'impôt")
        
        self.font=("serif", 14)

        self.mainFrame = tk.Frame(fenetre)

        self.tranches = CalculateurTranche(fenetre)
        self.tranches.pack(padx=10, pady=10)
        

        self.foyer = Foyer(self.mainFrame)
        self.foyer.grid(row=0, column=0, padx=10, pady=10)

        self.liste_deductions = ListeDeductions(self.mainFrame)
        self.liste_deductions.grid(row=0, column=1, padx=10, pady=10)

        self.mainFrame.pack()

        # Créer le bouton pour calculr l'impôt
        self.bouton_calculr = ttk.Button(fenetre, text="calculer l'impôt", command=self.calculr_impot)
        self.bouton_calculr.pack(padx=10, pady=10)

        # Étiquette pour afficher le résultat
        self.resultat = tk.Text(fenetre, wrap="word", width=30, height=20)
        self.resultat.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    def calculr_impot(self):
        #try:
        revenu = self.foyer.get_revenu()
        abattement = self.foyer.get_abattement()
        parts = self.foyer.get_parts()

        final_text = ""
        final_text += f"{revenu=}\n"
        final_text += f"{abattement=}%\n"
        final_text += f"{parts=}\n\n"

        if revenu < 0 or abattement < 0 or parts <= 0:
            raise ValueError("Les valeurs doivent être positives et le nombre de parts doit être supérieur à zéro.")

        # calcul de l'abattement 
        revenu_apres_abattement, text = calcul_revenu_apres_abattement(revenu, abattement)
        final_text += f"revenu apres abattement : {text}\n"

        # calcul des charges
        revenu_deduction_des_charges, text = self.liste_deductions.get_deduction_charges(revenu_apres_abattement)
        final_text += text

        # calcul par part
        assiette_fiscale = revenu_deduction_des_charges/parts # revenu moyen
        around_assiette_fiscale = math.floor(assiette_fiscale)
        final_text += f"assiette fiscale = {revenu_deduction_des_charges} / {parts} = {assiette_fiscale} = {around_assiette_fiscale}\n\n"

        # calcul des tranches
        impot, text = self.tranches.calcule_tranches(around_assiette_fiscale)
        final_text += text

        # calcul de la somme final
        final = impot * parts
        final_text += f"Somme des impots : {impot} x {parts} = {final}\n"

        # calcul du taux d'imposition
        taux_imposition = final/revenu_deduction_des_charges
        around_taux_imposition = math.floor(taux_imposition*10000)/100
        final_text += f"Taux d'imposition : {final} / {revenu_deduction_des_charges} = {taux_imposition} = {around_taux_imposition} %\n"

        # calcul du taux de prélèvement
        taux_prélèvement_source = final/(revenu_apres_abattement/parts)
        around_taux_prélèvement_source = math.floor(taux_prélèvement_source*10000)/100
        final_text += f"Taux de prélèvement à la source : {final} / ({revenu_apres_abattement} / {parts}) = {taux_prélèvement_source} = {around_taux_prélèvement_source} %\n"

        self.resultat.delete("1.0", tk.END)
        # Insère le nouveau texte
        self.resultat.insert(tk.END, final_text)

"""         except ValueError as e:
            messagebox.showerror("Erreur de saisie", str(e)) """

def main():
    fenetre = tk.Tk()
    app = CalculateurImpotUI(fenetre)
    fenetre.mainloop()

if __name__ == "__main__":
    main()
