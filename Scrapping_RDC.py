import requests
from bs4 import BeautifulSoup
from time import sleep
from lxml import etree
import os
from random import randint
import sys

arg = sys.argv

MAX_SLEEP = 10000

def r_sleep():
    ''' generates a random sleep between 2.000 and MAX_SLEEP seconds '''

    length = float(randint(2000, MAX_SLEEP)) / 1000
    mylog("Safety Random Sleep has started for {0} sec".format(length))
    sleep(length)
    mylog("Safety Random Sleep is over")


def mylog(msg):
    # Personalized print() tool, used for dummy logging
    print("-- " + msg)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
nbrmc = str(arg[2])

Max_prod = int(arg[1])

print("Max_prod =", Max_prod)
file = open(str(arg[3]),"w")
contenu = ''
products = ''

print(nbrmc)
Product_Number = 0
page = 1
while Product_Number < Max_prod :
    lien = "https://www.rueducommerce.fr/recherche/" + nbrmc + "?page=" + str(page)
    print(lien)
    try:
        contenu = requests.get (lien, headers=headers)
    except:
        break
    url_contenu = BeautifulSoup (contenu.content, "html.parser")
    try:
        products = url_contenu.find_all("a", attrs={"class":"plimg"})
    except:
        break
    print (products)
    for i in products:
        print (Product_Number, "https://www.rueducommerce.fr" + i["href"])
        file.write( i["href"] + "\n")
        Product_Number += 1
        if Product_Number > Max_prod-1:
            break
    page += 1

file.close()

#r_sleep()
prod_Name = ''
Prods_Prix = ''
Prods_Prix_OtherSellers = ''
Prods_Prix_livraison = ''
Prods_Prix_livraison_OtherSellers = ''
Prods_description_produits = ''
Prods_Seller_info = ''
Prods_Seller_rating = ''
Prods_Etat_Occasion = ''
Prods_Etat_Neuf = ''
Prods_Categorie = ''
prods = etree.Element("prods")
Prods_Url_photo = ''

mylog("Start scrapping product infos:")
with open(str(arg[3]),"r") as file:
    for i in file :
        contenu_price = requests.get(i[:-1], headers = headers)
        url_contenu_price = BeautifulSoup(contenu_price.content, "html.parser")
        try:
            Prods_Name = url_contenu_price.find("div", class_="productName").find("span", class_="name").text
        except:
            Prods_Name = "none"
        try:
            Prods_Url_photo = url_contenu_price.find("ul", attrs={"id":"thumbGallery"}).find("a")["data-zoom-image"]
        except:
            Prods_Url_photo = "none"
        try:
            Prods_Prix = url_contenu_price.find("div", class_="price main").find("p").text
        except:
            Prods_Prix = "none"
        try:
            Prods_Prix_OtherSellers = url_contenu_price.find("div", class_="flexGrid-box boxCol6 sellerPrice").find("span", class_="price").text
        except:
            Prods_Prix_OtherSellers = "none"

        Categorie = ''
        try:
            Prods_Categorie = url_contenu_price.find_all("li", attrs={"itemprop":"itemListElement"})
        except:
            print("none")
            Prods_Categorie = "none"

        for j in Prods_Categorie:
            try:
                Categorie += "--" + j.find("span", attrs={"itemprop":"name"}).text
            except:
                print("eror")
        try:
            Prods_Prix_livraison = url_contenu_price.find("table", class_="flexGrid-box boxCol12 table").find("tr", class_="odd").find("td", class_="comment").find("span").text
        except:
            Prods_Prix_livraison = "none"
        try:
            Prods_Etat_Neuf = url_contenu_price.find("div", attrs={"class":"productDetails"}).find("p", attrs={"class":"newUsed"}).text
        except:
            Prods_Etat_Neuf = "none"
        try:
            Prods_Etat_Occasion = url_contenu_price.find("div", attrs={"class":"productDetails"}).find("p", attrs={"class":"newUsed"}).find("a", attrs={"class":"state-link"}).text
        except:
            Prods_Etat_Occasion = "none"
        try:
            Prods_Prix_livraison_OtherSellers = url_contenu_price.find("tbody", id_="sellerList").find("tr", class_="odd").find("td", class_="highlight link").text
        except:
            Prods_Prix_livraison_OtherSellers = "none"
        try:
            Prods_description_produits = url_contenu_price.find("div", class_="productDesc").find("p", class_="productDescText").text
        except:
            Prods_description_produits = "Pas de description produit"
        try:
            Prods_Seller_info = url_contenu_price.find("p", class_="seller").find("span", class_="sellerName").text
        except:
            Prods_Seller_info = "Aucune information sur le vendeur"
        try:
            Prods_Seller_rating = url_contenu_price.find("p", class_="seller").find("span", class_="seller Rating").text
        except:
            Prods_Seller_rating = "Aucune information sur le vendeur"
        print (i, Prods_Prix ,Prods_Prix_OtherSellers, Prods_Prix_livraison, Prods_Seller_info)
        prod_lxml = etree.SubElement(prods, "prod")
        prod_lxml.set("url", i)
        prod_Name = etree.SubElement(prod_lxml, "Name")
        nom = str(Prods_Name)
        i = nom[0]

        while i==' ':
            nom = nom[1:]
            i = nom[0]
        i = nom[-1]
        while i==' ':
            nom = nom[:-1]
            i = nom[-1]
        l = nom[0]
        for k in range(len(nom)-1):
            k += 1

            if not (l[-1] == ' ' and nom[k] == " "):
                l += nom[k]
        nom = l
        prod_Name.text = str(nom)
        Image = etree.SubElement(prod_lxml, "Url_image")
        Image.text = str(Prods_Url_photo)
        price_lxml = etree.SubElement(prod_lxml, "price")
        Price_seller = etree.SubElement(price_lxml, "price_seller")
        Price_seller.text = str(Prods_Prix).replace("€", ".")
        price_otherSellers = etree.SubElement(price_lxml, "price_otherSellers")
        price_otherSellers.text = str(Prods_Prix_OtherSellers).replace(",", ".")[:-1]
        Categorie_lxml = etree.SubElement(prod_lxml, "Categorie")
        Categorie_lxml.text = str(Categorie)
        Etat_lxml = etree.SubElement(prod_lxml, "Etats_Produit")
        Etat_Neuf = etree.SubElement(Etat_lxml, "Etat_Neuf")
        Etat_Neuf.text = str(Prods_Etat_Neuf)
        Etat_Occasion = etree.SubElement(Etat_lxml, "Etat_Occasion")
        Etat_Occasion.text = str(Prods_Etat_Occasion)
        Livraison = etree.SubElement(prod_lxml, "Livraison")
        shipping = etree.SubElement(Livraison, "Price_livraison_Seller")
        shipping.text = str(Prods_Prix_livraison)
        shipping_otherSellers = etree.SubElement(Livraison, "Price_livraison_otherSellers")
        shipping_otherSellers.text = str(Prods_Prix_livraison_OtherSellers)
        sellerInfos = etree.SubElement(prod_lxml, "sellerInfos_and_sellerRating")
        seller = etree.SubElement(sellerInfos, "sellerName")
        seller.text = str(Prods_Seller_info)
        sellerRating = etree.SubElement(sellerInfos, "sellerRating")
        sellerRating.text = str(Prods_Seller_rating)
        Description = etree.SubElement(prod_lxml, "Description")
        Description_produit = etree.SubElement(Description, "Description_produit")
        Description_produit.text = str(Prods_description_produits)


#r_sleep()
mylog("Scrapping is finished!")
mylog("Starting writting xml:")
print(etree.tostring(prods, pretty_print=True))
file = open(str(arg[3]),"wb")
file.write(etree.tostring(prods, pretty_print=True, encoding="UTF-8"))
file.close()
