import telebot
from praisonai import PraisonAI
import os
from dotenv import load_dotenv


# Utilise les variables d'environnement
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_URL")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")


bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN, parse_mode=None)

def generate_content(prompt):
    """
    Utilisez PraisonAI ou une bibliothèque similaire pour générer du contenu basé sur une invite (prompt).
    Retourne le contenu généré.
    """
    # Cet exemple suppose l'existence d'une méthode `generate` pour praisonai qui accepte un prompt
    # et retourne du contenu généré. Remplacez par la méthode réelle fournie par votre bibliothèque.
    praison_ai = PraisonAI(auto=prompt, framework="autogen")
    generated_content = praison_ai.main()  # Adaptez cette ligne selon la méthode réelle
    return generated_content

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """
    Gestionnaire pour chaque message reçu. Utilise le texte du message comme invite pour générer du contenu.
    """
    # Utilise le texte du message comme invite pour générer du contenu
    prompt = message.text
    generated_content = generate_content(prompt)

    # Envoyez le contenu généré en réponse
    bot.reply_to(message, generated_content)

if __name__ == "__main__":
    bot.infinity_polling()
