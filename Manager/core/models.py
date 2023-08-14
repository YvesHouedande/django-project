from django.db import models
from django.contrib.auth.models import User


class ProfileUtisateur(models.Model):
    user = models.ForeignKey(User, verbose_name="", on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    Prenom = models.CharField(max_length=100)
    email = models.EmailField()  
    Bio = models.TextField(max_length=100)

    def __str__(self):
        return self.nom

   
from django.db import models

class Product(models.Model):
    INTRANT = 'Intrant'
    SORTIE = 'Sortie'
    ENTREE = 'Entree'
    OUTILS = 'Outils'

    KIND_CHOICES = [
        (INTRANT, 'Intrant'),
        (SORTIE, 'Sortie'),
        (ENTREE, 'Entree'),
        (OUTILS, 'Outils'),
    ]

    name = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    kind = models.CharField(max_length=100, choices=KIND_CHOICES)
    category= models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    img_url = models.URLField(null=True, blank=True)
    img_upload = models.ImageField(upload_to='product_images/', null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True)

    def img(self):
        if self.img_url:
            return self.img_url
        elif self.img_upload:
            return self.img_upload.url
        else:
            return None

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Les Produits"


class Order(models.Model):
    client = models.ForeignKey(ProfileUtisateur, on_delete=models.CASCADE)
    produts = models.ManyToManyField(Product, through='LigneOrder')
    date_commande = models.DateTimeField(auto_now_add=True)
    validation = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Panier de : {self.client.nom}"
    
    class Meta:
        verbose_name = "Panier"
        verbose_name_plural = "Les Paniers"


class LigneOrder(models.Model):
    commande = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"ProduitCommande: {self.product.name}"
    class Meta:
        verbose_name = "Produit de Commande"
        verbose_name_plural = "Produits de commande"

class Category(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(null=True)
    

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Les Categories"






   