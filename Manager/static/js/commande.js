// Tous les produits
var products = document.querySelectorAll(".showcase-content");
var total_cart = document.getElementById("count-Unique")





// console.log(products)

function getProductInfos(showcaseContent){
    // Accéder au bouton "ajouter" (le premier bouton avec la classe "bouton-ajouter")
    const addButton = showcaseContent.querySelector('.bouton-ajouterA');
    const RestButton = showcaseContent.querySelector('.bouton-ajouterR');
    
        return {
            'id_produit':showcaseContent.id,
            'quantite':showcaseContent.querySelector('.counter-value').textContent
        }
    
}


products.forEach(product=>{
    // Ajouter au panier
    product.querySelector(".bouton-ajouterA").addEventListener('click', () => {
        // Utilisation de la syntaxe de template littéral pour afficher la valeur du texte
        let productId = product.id;
        let quantityToAdd = product.querySelector('.counter-value').textContent;
            // Envoyer la quantité ajoutée au serveur en utilisant Fetch
    fetch(`/add_to_cart/?product_id=${productId}&quantity=${quantityToAdd}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'X-CSRFToken': getCSRFToken() // Assurez-vous d'obtenir le jeton CSRF correct (voir ci-dessous)
        },
      })
      .then(
        response => response.json()
      ).then(
        data => {
          
          total_cart.textContent = data["cart_total"]
        }
      )
      .catch(error => console.error('Une erreur est survenue', error));
      });



    // restaurer Les Produits
    product.querySelector(".bouton-ajouterR").addEventListener('click', () => {
        // Utilisation de la syntaxe de template littéral pour afficher la valeur du texte
        let productId = product.id;
            // Envoyer la quantité ajoutée au serveur en utilisant Fetch
    fetch(`/restaure/?product_id=${productId}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'X-CSRFToken': getCSRFToken() // Assurez-vous d'obtenir le jeton CSRF correct (voir ci-dessous)
        },
      })
      .then(response => response.json())
      .then(         data => {
        total_cart.textContent = data["cart_total"]
      })
      .catch(error => console.error('Une erreur est survenue', error));
      });
}

)

function getCSRFToken() {
    const csrfCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('csrftoken='));
    if (csrfCookie) {
      return csrfCookie.split('=')[1];
    } else {
      console.error('Le jeton CSRF est introuvable.');
      return null;
    }
  }