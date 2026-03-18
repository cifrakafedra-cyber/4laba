import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class TelegramBot:
    def __init__(self, token: str):
        self.token = token
        self.application = None

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обработчик команды /start"""
        await update.message.reply_text(
            "👋 Привет! Я простой бот.\n"
            "Доступные команды:\n"
            "/start - Начать работу\n"
            "/search - Поиск\n"
            "/chat - Чат\n"
            "/basic - Базовая информация"
        )
        logger.info(f"User {update.effective_user.id} started the bot")

    async def search_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обработчик команды /search"""
        await update.message.reply_text(
            "🔍 Функция поиска в разработке.\n"
            "Скоро здесь можно будет искать информацию!"
        )
        logger.info(f"User {update.effective_user.id} used search command")

    async def chat_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обработчик команды /chat"""
        await update.message.reply_text(
            "💬 Режим чата активирован!\n"
            "Эта функция пока недоступна."
        )
        logger.info(f"User {update.effective_user.id} used chat command")

    async def basic_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обработчик команды /basic"""
        await update.message.reply_text(
            "ℹ️ Базовая информация:\n"
            "Версия: 1.0.0\n"
            "Автор: Your Name\n"
            "Статус: Активен"
        )
        logger.info(f"User {update.effective_user.id} used basic command")

    def setup_handlers(self):
        """Настройка обработчиков команд"""
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("search", self.search_command))
        self.application.add_handler(CommandHandler("chat", self.chat_command))
        self.application.add_handler(CommandHandler("basic", self.basic_command))

    def run(self):
        """Запуск бота"""
        self.application = Application.builder().token(self.token).build()
        self.setup_handlers()
        
        logger.info("Bot started successfully")
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)


def main():
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    token="8009556866:AAGRCIH66opB9y2ftWS1Y5rTmTjqZV_JfLQ"
    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN environment variable is not set")
    
    bot = TelegramBot(token)
    bot.run()


if __name__ == '__main__':
    main()