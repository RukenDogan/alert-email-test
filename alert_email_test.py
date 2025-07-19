import smtplib # Module de connexion au serveur SMTP
from email.mime.text import MIMEText # Module pour créer le contenu de l'email
from dotenv import load_dotenv # Module pour charger les variables d'environnement depuis un fichier .env
import os # Module pour interagir avec le système d'exploitation

# Charger les variables d'environnement
load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

def send_test_email(): # Fonction pour envoyer un email de test
    subject = "Alerte" # Objet de l'email
    body = "Bonjour, je suis un test d'envoi d'email avec Python" # Corps de l'email

    msg = MIMEText(body) # Créer le message email
    msg["Subject"] = subject # Définir l'objet de l'email
    msg["From"] = SENDER_EMAIL # Définir l'expéditeur de l'email
    msg["To"] = RECIPIENT_EMAIL # Définir le destinataire de l'email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server: # Connexion au serveur SMTP de Gmail
            server.login(SENDER_EMAIL, APP_PASSWORD) # Authentification avec l'email et le mot de passe d'application
            server.sendmail(SENDER_EMAIL, [RECIPIENT_EMAIL], msg.as_string()) # Envoi de l'email
        print("Email envoyé avec succès !") # Confirmation de l'envoi dans le terminal
    except Exception as e: # Gestion des exceptions en cas d'erreur lors de l'envoi
        print(f"Échec de l'envoi : {e}") # Afficher l'erreur dans le terminal

if __name__ == "__main__": # Point d'entrée du script
    send_test_email() # Appeler la fonction pour envoyer l'email de test

