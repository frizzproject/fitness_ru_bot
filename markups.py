from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# For menu
btnCalories = KeyboardButton(text = '🍩 Рассчитать каллории')
btnBmi = KeyboardButton(text = '🧘‍♀️ ИМТ')

# Share bot
btnShare = InlineKeyboardButton(text = '📫 Поделиться', switch_inline_query = 'Привет!👋Это я - Fitness Bot. Готов помогать тебе оставаться здоровым! Нажмай на ссылку и попробуй мои функции.')

# For select formula
formula_1 = InlineKeyboardButton(text = '1️⃣ Миффлина - Сан Жеора', callback_data = 'formula_1')
formula_2 = InlineKeyboardButton(text = '2️⃣ Харриса-Бенедикта', callback_data = 'formula_2')

# Bmi picture
BMI_NORMS_URL = './static/bmi_banner.png'

# For select gender
maleBtnInline = InlineKeyboardButton(text = '♂ Мужской', callback_data = 'genderMale')
femaleBtnInline = InlineKeyboardButton(text = '♀ Женский', callback_data = 'genderFemale')
moreBtnInline = InlineKeyboardButton(text = '⚧ Другое', callback_data = 'genderMore')

# For select activites
activeMin = InlineKeyboardButton(text = '🕴️ Основной обмен', callback_data = '1.2')
activeWeak = InlineKeyboardButton(text = '🧘‍♂️ Минимальные нагрузки (3 раза в нед.)', callback_data = '1.375')
activeMidle = InlineKeyboardButton(text = '🚴‍♂️ Средняя активность (5-7 раз в нед.)', callback_data = '1.55')
activeHight = InlineKeyboardButton(text = '🏊‍♂️ Высокая активность (к.д интенсивно)', callback_data = '1.725')
activeExtra = InlineKeyboardButton(text = '🏋️‍♂️ Спортсмен', callback_data = '1.9')


kb_menu = ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1).add(btnCalories, btnBmi)
kb_share = InlineKeyboardMarkup(resize_keyboard = True, row_width = 1).add(btnShare)
kb_gender = InlineKeyboardMarkup(resize_keyboard = True, row_width = 2).add(maleBtnInline, femaleBtnInline, moreBtnInline)
kb_active = InlineKeyboardMarkup(resize_keyboard = True, row_width = 1).add(activeMin, activeWeak, activeMidle, activeHight, activeExtra)
kb_formuls = InlineKeyboardMarkup(resize_keyboard = True, row_width = 1).add(formula_1, formula_2)

