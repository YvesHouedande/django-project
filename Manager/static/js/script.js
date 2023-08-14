// 'use strict';

// // modal variables
// const modal = document.querySelector('[data-modal]');
// const modalCloseBtn = document.querySelector('[data-modal-close]');
// const modalCloseOverlay = document.querySelector('[data-modal-overlay]');

// // modal function
// const modalCloseFunc = function () { modal.classList.add('closed') }

// // modal eventListener
// modalCloseOverlay.addEventListener('click', modalCloseFunc);
// modalCloseBtn.addEventListener('click', modalCloseFunc);





// // notification toast variables
// const notificationToast = document.querySelector('[data-toast]');
// const toastCloseBtn = document.querySelector('[data-toast-close]');

// // notification toast eventListener
// toastCloseBtn.addEventListener('click', function () {
//   notificationToast.classList.add('closed');
// });





// // mobile menu variables
// const mobileMenuOpenBtn = document.querySelectorAll('[data-mobile-menu-open-btn]');
// const mobileMenu = document.querySelectorAll('[data-mobile-menu]');
// const mobileMenuCloseBtn = document.querySelectorAll('[data-mobile-menu-close-btn]');
// const overlay = document.querySelector('[data-overlay]');

// for (let i = 0; i < mobileMenuOpenBtn.length; i++) {

//   // mobile menu function
//   const mobileMenuCloseFunc = function () {
//     mobileMenu[i].classList.remove('active');
//     overlay.classList.remove('active');
//   }

//   mobileMenuOpenBtn[i].addEventListener('click', function () {
//     mobileMenu[i].classList.add('active');
//     overlay.classList.add('active');
//   });

//   mobileMenuCloseBtn[i].addEventListener('click', mobileMenuCloseFunc);
//   overlay.addEventListener('click', mobileMenuCloseFunc);

// }





// // accordion variables
// const accordionBtn = document.querySelectorAll('[data-accordion-btn]');
// const accordion = document.querySelectorAll('[data-accordion]');

// for (let i = 0; i < accordionBtn.length; i++) {

//   accordionBtn[i].addEventListener('click', function () {

//     const clickedBtn = this.nextElementSibling.classList.contains('active');

//     for (let i = 0; i < accordion.length; i++) {

//       if (clickedBtn) break;

//       if (accordion[i].classList.contains('active')) {

//         accordion[i].classList.remove('active');
//         accordionBtn[i].classList.remove('active');

//       }

//     }

//     this.nextElementSibling.classList.toggle('active');
//     this.classList.toggle('active');

//   });

// }




// Récupération des éléments du DOM

const decrementButton = document.querySelectorAll(".decrement");
const incrementButton = document.querySelectorAll(".increment");
const valueDisplay = document.querySelectorAll(".counter-value");
const qteFix = document.querySelectorAll(" .qte")

function incrementItem(index) {
  let currentValue = parseInt(valueDisplay[index].textContent);
  let currentQte = parseInt(qteFix[index].textContent);
  if (currentQte> currentValue){
      return currentValue + 1; }
  else { return currentValue}
}

function decrementItem(index) {
  let currentValue = parseInt(valueDisplay[index].textContent);
  if (currentValue> 0){
    return currentValue - 1; }
else { return currentValue}
  
}

decrementButton.forEach((bouton, index) => {
  bouton.addEventListener('click', function () {
    valueDisplay[index].textContent = decrementItem(index);
  });
});

incrementButton.forEach((bouton, index) => {
  bouton.addEventListener('click', function () {
    valueDisplay[index].textContent = incrementItem(index);
  });
});

// Valeur initiale
let value = 0;

// Fonction pour mettre à jour l'affichage de la valeur
function updateDisplay() {
  valueDisplay.textContent = value;
}



// Initialiser l'affichage
updateDisplay();


// restaurer

var products = document.querySelectorAll(".showcase-content");

products.forEach(product=>{
  // Ajouter au panier
  product.querySelector(".bouton-ajouterR").addEventListener('click', () => {
  product.querySelector(".counter-value").textContent = 0;

    });


}

)
