// Ouvrir la fenêtre modale au clic sur l'icon plus"
const openModalBtn = document.getElementById('openModalBtn');
const modal = document.getElementById('myModal');
const closeModalBtn = document.getElementById('closeModalBtn');

openModalBtn.addEventListener('click', function() {
  modal.style.display = 'block';
});

// Fermer la fenêtre modale au clic sur le bouton "X"
closeModalBtn.addEventListener('click', function() {
  modal.style.display = 'none';
});

// Fermer la fenêtre modale si l'utilisateur clique en dehors de celle-ci
window.addEventListener('click', function(event) {
  if (event.target === modal) {
    modal.style.display = 'none';
  }
});

// Soumettre le formulaire de la fenêtre modale (à personnaliser selon vos besoins)
const newsletterForm = document.getElementById('newsletterForm');
newsletterForm.addEventListener('submit', function(event) {
  event.preventDefault();
  
  // Récupérer les valeurs saisies dans le formulaire
  const nom = document.getElementById('nom').value;
  const prenom = document.getElementById('prenom').value;
  const email = document.getElementById('email').value;
  const age = document.getElementById('age').value;
  
  // Vous pouvez utiliser ces valeurs pour effectuer des actions comme envoyer les données à un serveur
  // Ici, nous affichons simplement les valeurs dans la console
  console.log('Nom:', nom);
  console.log('Prénom:', prenom);
  console.log('E-mail:', email);
  console.log('Âge:', age);
  
  // Fermer la fenêtre modale après avoir soumis le formulaire
  modal.style.display = 'none';
});
