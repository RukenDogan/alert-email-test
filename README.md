## Description
Ce test permet d'envoyer un email automatique via un script Python en utilisant les variables d'environnement stockées dans un fichier .env.  
L'email est envoyé via un compte Gmail sécurisé avec un mot de passe d'application.

---

## Installation

1. Installer la bibliothèque `python-dotenv` :

```
    pip install python-dotenv
```

2. Créer un script Python pour envoyer un email.

3. Créer un fichier .env contenant :  
- L'adresse email de l'expéditeur (`SENDER_EMAIL`)  
- Le mot de passe d'application Gmail (`APP_PASSWORD`)  
- L'adresse email du destinataire (`RECIPIENT_EMAIL`)

---

## Génération du mot de passe d'application Gmail

1. Activer la validation en deux étapes sur ton compte Google (avec un numéro de téléphone).  
2. Dans la même rubrique **Validation en 2 étapes**, accéder à **Mots de passe des applications**.  
3. Générer un mot de passe d'application pour l'envoi d'email.
4. Utiliser ce mot de passe dans le fichier .env.

---

## Utilisation

- Remplir le fichier .env avec les informations demandées.  
- Lancer le script Python pour tester l'envoi d'email.
- Vérifier la réception du mail dans la boîte destinataire.

---