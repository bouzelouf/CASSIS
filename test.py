import math
def compEtat(etat1,site1,etat2,site2):
    # list_status[0] ==> eBay
    # list_status[1] ==> Priceminister
    # list_status[2] ==> cdiscount
    list_status = [["Neuf", "Reconditionné par le fabricant", "Reconditionné par le vendeur", "Occasion", "Pour pièces détachées/ne fonctionne pas"], ["Neuf", "Comme Neuf", "Très Bon Etat", "Bon Etat", "Etat Correct", "Hors Service"], ["Neuf", "Reconditionné", "Comme neuf","Très Bon Etat", "Bon Etat", "Etat correct"]]
    etat1 = float((len(list_status[site1])-list_status[site1].index(etat1))/len(list_status[site1]))
    etat2 = float((len(list_status[site2])-list_status[site2].index(etat2))/len(list_status[site2]))
    diff_etat = float((1-math.fabs(etat1-etat2))*100)
    return diff_etat


print(compEtat("Pour pièces détachées/ne fonctionne pas", 0, "Hors Service", 1))
