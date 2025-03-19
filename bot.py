import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from game_data import CATEGORIES, GAMES_PROFESSIONS

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Constants
MAX_GAME_SELECTIONS = 5
MAX_RECOMMENDATIONS = 5
BAR_LENGTH = 20  # Maximum length of the progress bar

# Get bot token from environment variable
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

user_selections = {}
user_states = {}

# Добавим описания профессий
PROFESSION_DESCRIPTIONS = {
    "Гейм-дизайнер": "Создает концепцию игры, разрабатывает механики и балансирует геймплей",
    "Технический художник": "Создает визуальные эффекты и оптимизирует графику для разных платформ",
    "Сценарист игр": "Разрабатывает сюжет, диалоги и нарративную структуру игры",
    "Разработчик игровых механик": "Программирует основные механики и системы игры",
    "3D Моделлер": "Создает 3D модели персонажей, окружения и объектов",
    "Дизайнер уровней": "Проектирует и создает игровые уровни и локации",
    "Разработчик шейдеров": "Создает визуальные эффекты и материалы для 3D графики",
    "UI/UX дизайнер": "Разрабатывает интерфейс и взаимодействие с пользователем",
    "AI инженер": "Разрабатывает искусственный интеллект для NPC и игровых систем",
    "Аналитик данных": "Анализирует игровую статистику и поведение игроков",
    "Разработчик игровой логики": "Программирует основную логику и системы игры",
    "AI программист": "Разрабатывает алгоритмы искусственного интеллекта",
    "Специалист по балансу": "Балансирует игровые механики и экономику",
    "Разработчик тактических систем": "Создает системы тактического геймплея",
    "Разработчик сетевого кода": "Обеспечивает работу многопользовательского режима",
    "Специалист по античиту": "Разрабатывает системы защиты от читерства",
    "Backend разработчик": "Создает серверную часть и базы данных",
    "3D аниматор": "Создает анимации для персонажей и объектов",
    "2D художник": "Создает 2D графику и спрайты",
    "Геймплей-программист": "Программирует игровые механики и взаимодействия",
    "Разработчик платформеров": "Создает механики для платформенных игр",
    "Композитор": "Создает музыку и звуковое оформление",
    "Java разработчик": "Программирует на Java для кроссплатформенной разработки",
    "Разработчик процедурной генерации": "Создает системы генерации контента",
    "Специалист по оптимизации": "Оптимизирует производительность игры",
    "Разработчик систем автоматизации": "Создает системы автоматизации в играх",
    "3D программист": "Программирует 3D графику и рендеринг",
    "Разработчик боевых систем": "Создает системы боя и сражений",
    "Разработчик AI": "Разрабатывает искусственный интеллект",
    "Разработчик симуляций": "Создает физические и игровые симуляции",
    "Сценарист игр": "Разрабатывает сюжет и диалоги",
    "Дизайнер диалогов": "Создает систему диалогов и выборов",
    "Нарративный дизайнер": "Разрабатывает повествовательную структуру",
    "Motion Capture специалист": "Работает с технологиями захвата движения",
    "Sound дизайнер": "Создает звуковые эффекты и атмосферу",
    "Физический программист": "Разрабатывает физический движок",
    "Дизайнер головоломок": "Создает головоломки и механики решения задач",
    "Специалист по базам данных": "Разрабатывает и оптимизирует базы данных",
    "Специалист по безопасности": "Обеспечивает безопасность игровых систем"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send message on `/start`."""
    keyboard = []
    
    # Create category buttons
    for category_id, category_name in CATEGORIES.items():
        keyboard.append([InlineKeyboardButton(category_name, callback_data=f"cat_{category_id}")])
    
    # Add the recommendations button as the last row
    keyboard.append([InlineKeyboardButton("🎯 Получить рекомендации", callback_data="recommend")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Привет! Я помогу тебе найти подходящую IT-профессию на основе твоих игровых предпочтений.\n\n"
        "🎮 Выбери категорию игр:",
        reply_markup=reply_markup
    )
    
    # Initialize user state
    user_id = update.message.from_user.id
    user_states[user_id] = "categories"
    if user_id not in user_selections:
        user_selections[user_id] = set()

async def show_category_games(query: Update.callback_query, category: str) -> None:
    """Show games for selected category."""
    keyboard = []
    user_id = query.from_user.id
    
    # Get games for this category
    category_games = [(game_id, game_info) for game_id, game_info in GAMES_PROFESSIONS.items() 
                     if game_info["category"] == category]
    
    # Create game buttons
    for game_id, game_info in category_games:
        is_selected = game_id in user_selections.get(user_id, set())
        can_select = is_selected or len(user_selections.get(user_id, set())) < MAX_GAME_SELECTIONS
        button_text = f"✓ {game_info['name']}" if is_selected else game_info['name']
        keyboard.append([InlineKeyboardButton(button_text, callback_data=game_id if can_select else "max_reached")])
    
    # Add navigation buttons
    nav_row = [InlineKeyboardButton("⬅️ Назад к категориям", callback_data="back_to_categories")]
    
    # Add reset button if there are selections
    if user_selections.get(user_id, set()):
        nav_row.append(InlineKeyboardButton("🔄 Сбросить выбор", callback_data="reset_selections"))
    
    nav_row.append(InlineKeyboardButton("🎯 Рекомендации", callback_data="recommend"))
    keyboard.append(nav_row)
    
    selected_count = len(user_selections.get(user_id, set()))
    status_text = f"\n\nВыбрано игр: {selected_count}/{MAX_GAME_SELECTIONS}"
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text=f"{CATEGORIES[category]}\nВыбери игры, в которые ты любишь играть:{status_text}",
        reply_markup=reply_markup
    )

async def show_categories(query: Update.callback_query) -> None:
    """Show game categories."""
    keyboard = []
    user_id = query.from_user.id
    
    # Create category buttons
    for category_id, category_name in CATEGORIES.items():
        keyboard.append([InlineKeyboardButton(category_name, callback_data=f"cat_{category_id}")])
    
    # Add the recommendations and reset buttons
    bottom_row = [InlineKeyboardButton("🎯 Получить рекомендации", callback_data="recommend")]
    if user_selections.get(user_id, set()):
        bottom_row.insert(0, InlineKeyboardButton("🔄 Сбросить выбор", callback_data="reset_selections"))
    keyboard.append(bottom_row)
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    selected_count = len(user_selections.get(user_id, set()))
    status_text = f"\n\nВыбрано игр: {selected_count}/{MAX_GAME_SELECTIONS}" if selected_count > 0 else ""
    
    await query.edit_message_text(
        text=f"🎮 Выбери категорию игр:{status_text}",
        reply_markup=reply_markup
    )

def create_bar_chart(percentage):
    """Create an ASCII bar chart with given percentage."""
    filled_length = int(BAR_LENGTH * percentage / 100)
    bar = '█' * filled_length + '▒' * (BAR_LENGTH - filled_length)
    return bar

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button presses."""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    data = query.data
    
    if data == "start":
        await show_categories(query)
    elif data == "back_to_categories":
        await show_categories(query)
    elif data == "back_to_games":
        category = user_states.get(user_id, {}).get("category")
        if category:
            await show_category_games(query, category)
    elif data == "reset":
        user_selections[user_id] = set()
        await show_categories(query)
    elif data.startswith("cat_"):
        category = data[4:]  # Remove 'cat_' prefix
        user_states[user_id] = {"category": category}
        await show_category_games(query, category)
    elif data == "recommend":
        if user_id in user_selections and user_selections[user_id]:
            await show_recommendations(update, context)
        else:
            await query.message.reply_text("⚠️ Пожалуйста, выберите хотя бы одну игру для получения рекомендаций.")
    elif data == "reset_selections":
        user_selections[user_id] = set()
        await show_categories(query)
    elif data in GAMES_PROFESSIONS:
        if user_id not in user_selections:
            user_selections[user_id] = set()
        
        if data in user_selections[user_id]:
            user_selections[user_id].remove(data)
        else:
            if len(user_selections[user_id]) >= MAX_GAME_SELECTIONS:
                await query.answer(
                    f"Достигнут максимум в {MAX_GAME_SELECTIONS} игр! Убери какую-нибудь игру, чтобы выбрать новую.",
                    show_alert=True
                )
                return
            user_selections[user_id].add(data)
        
        # Show the updated game list for the current category
        game_category = GAMES_PROFESSIONS[data]["category"]
        await show_category_games(query, game_category)

async def show_recommendations(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.callback_query.from_user.id
    selected_games = user_selections.get(user_id, set())
    
    if not selected_games:
        await update.callback_query.message.reply_text("⚠️ Пожалуйста, выберите хотя бы одну игру для получения рекомендаций.")
        return
    
    # Подсчет профессий
    profession_counts = {}
    for game_id in selected_games:
        for profession in GAMES_PROFESSIONS[game_id]["professions"]:
            profession_counts[profession] = profession_counts.get(profession, 0) + 1
    
    # Сортировка профессий по частоте
    sorted_professions = sorted(profession_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Формирование сообщения с рекомендациями
    message = "🎮 На основе выбранных игр, вот рекомендуемые IT-профессии:\n\n"
    
    # Показываем только топ-5 профессий
    for profession, count in sorted_professions[:MAX_RECOMMENDATIONS]:
        percentage = (count / len(selected_games)) * 100
        description = PROFESSION_DESCRIPTIONS.get(profession, "")
        message += f"*{profession}* - {percentage:.0f}%\n_{description}_\n\n"
    
    # Добавляем кнопку сброса
    keyboard = [[InlineKeyboardButton("🔄 Сбросить выбор", callback_data="reset_selections")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.callback_query.message.reply_text(
        message,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

def main() -> None:
    """Start the bot."""
    if not BOT_TOKEN:
        raise ValueError("No token provided. Set TELEGRAM_BOT_TOKEN environment variable.")
        
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main() 