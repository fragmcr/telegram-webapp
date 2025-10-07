import logging
from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# 1. Настройки и токен
# !!! ЗАМЕНИТЕ ЭТО НА ВАШ ТОКЕН БОТА !!!
BOT_TOKEN = "7766785699:AAFeAGqJxdfQ7FbR_rKutsw0_71-iywHYE0"
# !!! ЗАМЕНИТЕ ЭТО НА ССЫЛКУ, ГДЕ РАЗМЕЩЕН ВАШ HTML-ФАЙЛ (ОБЯЗАТЕЛЬНО HTTPS!) !!!
WEB_APP_URL = "https://fragmcr.github.io/telegram-webapp/" 

# Включите логирование для отслеживания ошибок
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 2. Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет приветственное сообщение и кнопку для запуска Web App."""
    
    # Создаем объект WebAppInfo, указывая URL нашего приложения
    web_app_info = WebAppInfo(url=WEB_APP_URL)
    
    # Создаем кнопку, которая запускает Web App
    keyboard = [
        [InlineKeyboardButton(
            "🚀 Запустить Профиль", 
            web_app=web_app_info
        )]
    ]
    
    # Создаем разметку с кнопкой
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с кнопкой
    await update.message.reply_text(
        "👋 Добро пожаловать! Нажмите на кнопку ниже, чтобы запустить анимированный профиль в мини-приложении Telegram.",
        reply_markup=reply_markup
    )

# 3. Основная функция запуска бота
def main() -> None:
    """Запускает бота."""
    # Создаем Application и передаем ему токен бота
    application = Application.builder().token(BOT_TOKEN).build()

    # Добавляем обработчик для команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота, используя механизм "длинного опроса" (polling)
    print("Бот запущен. Нажмите Ctrl+C для остановки.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':

    main()

