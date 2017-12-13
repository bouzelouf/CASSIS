import subprocess
import sys


def cdiscount(nombre_produit, key_word, fichier):
    subprocess.check_call([sys.executable, 'Cdiscount\Scrapping_cdiscount.py', nombre_produit, key_word, fichier])

def Priceminister(nombre_produit,key_word, fichier):
    subprocess.check_call([sys.executable, 'Priceminister\Scrapping_pm.py', nombre_produit, key_word, fichier])

def EBAY(nombre_produit,key_word, fichier):
    subprocess.check_call([sys.executable, 'EBAY\Scrapping_Ebay.py', nombre_produit, key_word, fichier])

def Rue_du_commerce(nombre_produit,key_word, fichier):
    subprocess.check_call([sys.executable, 'Rue_du_commerce\Scrapping_RDC.py', nombre_produit, key_word, fichier])

list_keywords = ["samsung", "Smartphone", "Jeux video","vitre trempee", "Ipod", "Appareil photo", "Ordinateur portable", "Televiseur", "ecouteurs apple airpods","ecouteurs apple earpods", "apple iphone 7","apple iphone 7 plus", "Imprimantes laser","Imprimantes 3D"]

for i in list_keywords:
    f = "Big_Data/" + i
    #Rue_du_commerce('3', i, f+"_RDC.qaz")
    Priceminister('3', i, f+"_PM.qaz")
    #EBAY('3', i, f+"_EBAY.qaz")
    #cdiscount('3', i,f+"_CD.qaz")
