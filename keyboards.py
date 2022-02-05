from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# For menu
btnCalories = InlineKeyboardButton(text = '🍩 Каллории', callback_data = 'btnCalories')
btnBmi = InlineKeyboardButton(text = '🧘‍♀️ ИМТ', callback_data = 'btnBmi')
btnShare = InlineKeyboardButton(text = '📫 Поделиться', switch_inline_query = 'Привет!👋Это я - Fitness Bot. Готов помогать тебе оставаться здоровым! Нажмай на ссылку и попробуй мои функции.')

# For select formula
formula_1 = KeyboardButton('Миффлина - Сан Жеора')
formula_2 = KeyboardButton('Харриса-Бенедикта')

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


kb_menu = InlineKeyboardMarkup(resize_keyboard = True, row_width = 2).add(btnCalories, btnBmi, btnShare)
kb_gender = InlineKeyboardMarkup(resize_keyboard = True, row_width = 2).add(maleBtnInline, femaleBtnInline, moreBtnInline)
kb_active = InlineKeyboardMarkup(resize_keyboard = True, row_width = 1).add(activeMin, activeWeak, activeMidle, activeHight, activeExtra)
kb_formuls = ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1).add(formula_1, formula_2)
