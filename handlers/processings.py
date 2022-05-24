from aiogram import types
from dispatcher import dp
from dispatcher import bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as md
from aiogram.types import ParseMode
from storage import FORM_DATA, FORM_DATA_BMI
from markups import kb_menu, kb_share, kb_gender, kb_active, kb_formuls, BMI_NORMS_URL
from utils import *

"""     
COMMANDS HANDLER
"""
# Обработка команды - /start | !start | /s | !s
@dp.message_handler(commands = ['start', 's', 'menu', 'm'], commands_prefix = "/!")
async def start_processing(msg: types.Message):
    """Answer on start"""
    try:
        await msg.answer('<i>Привет</i> <b>{user.first_name}</b>!\n<i>Меня зовут</i> <b>Fitness Bot</b><i>. Ты попал в главное меню выбора функций, выбери одну из них, чтобы продолжить.</i>'
        .format(user = msg.from_user), parse_mode="HTML", reply_markup = kb_menu)
        await msg.answer('<i>Если захочешь рассказать обо мне друзьям, то нажимай на кнопку «поделиться»!</i>'
        .format(user = msg.from_user), parse_mode="HTML", reply_markup = kb_share)
    except:
        pass


# Обработка команды - /help | !help | /h | !h
@dp.message_handler(commands = ['help', 'h'], commands_prefix = "/!")
async def help_processing(msg: types.Message):
    """Answer on help"""
    try:
        await msg.answer('❗️<i>Чтобы начать пользоваться моими функциями, тебе нужно прописать команду:</i> /start или /menu. <i>После выбрать одну из функцию расчёта. Я попрошу у тебя некоторые данные, чтобы сделать верные расчеты и покажу тебе чек-лист с результатами!</i> 📊\n\n📋 <b>Список основных команд:</b>\n1. /menu (/m, !m) - выбрать функцию (меню)\n2. /help (/h, !h) - помощь в использовании\n3. /info (/i, !i) - информация о работе бота\n4. /calories - функция расчёта калорий\n5. /bmi - функция расчёта имт', parse_mode="HTML")
    except:
        pass


# Обработка команды - /info | !info | /i | !i
@dp.message_handler(commands = ['info', 'i'], commands_prefix = "/!")
async def info_processing(msg: types.Message):
    """Answer on info"""
    try:
        await msg.answer('ℹ️ <b>Fitness Bot</b> <i>имеет несколько функций, которые позволяют узнать состояние своего тела.</i> 🧘\n\n1⃣ <b>Расчёт калорий</b>. <i>Эта функция производит подсчёт суточной нормы калорий на основе данных, которые вы вводите.</i>\n\n<b>Fitness Bot</b> <i>умеет считать по 2 формулам:</i>\n1. <i>Доработанный вариант формулы Миффлина-Сан Жеора, в отличие от упрощенного дает более точную информацию и учитывает степень физической активности человека.</i>\n2. <i>Первый раз о формуле  Харриса-Бенедикта написали в 1919 году Джеймсом Артуром Харрисом и Фрэнсисом Гано Бенедиктом. Она служит для определения базального метаболизма. Различия между формулами практически нет. Первая формула была выведена не так давно, в отличие от второй.</i>\n\n2⃣ <b>Расчёт индекса массы тела (ИМТ)</b>. <i>Используется для определения того, находитесь ли вы в идеальном диапазоне веса для вашего роста. Это дает вам представление о том, имеете ли вы «недостаточный вес», «<b>нормальный вес</b>», «<b>избыточный вес</b>» или «<b>ожирение</b>» с учетом вашего роста.</i>\n\n❗️<i>Все полученные данные от бота являются приблизительными (условными). Каждый человек очень индивидуальный, чтобы получить точную информацию потребуется пройти <b>полное медицинское обследование</b>. Вся информация и формулы для расчётов взяты с открытых источников.</i>', parse_mode="HTML")
    except:
        pass


# Обработка команды - /cancel | !cancel
@dp.message_handler(state = '*', commands = ['cancel'], commands_prefix = "/!")
@dp.message_handler(Text(equals = 'отмена', ignore_case = True), state = '*')
async def cancel_processing(msg: types.Message, state: FSMContext):
    try:
        current_state = await state.get_state()
        if current_state is None:
            return

        await state.finish()
        await msg.reply('<i>Ок. Я отменил твои действия.</i>', parse_mode = 'HTML')
        await msg.answer('<i>Напиши /menu или !m, чтобы вызвать меню выбора функций.</i>', parse_mode = 'HTML')
    except:
        pass


# Обработка команды - /calories | !calories
@dp.message_handler(commands = ['calories'], commands_prefix = "/!")
async def calories_processing(msg: types.Message):
    try:
        await FORM_DATA.age.set()
        await msg.answer('<i>Отлично! Ты выбрал(а) функцию <b>расчёта калоиий</b>. Теперь мне нужна будет некоторая информация про тебя. Если ты вдруг введёшь неправильные данные, то можешь отменить действие командой: /cancel.</i>', parse_mode = 'HTML')
        await msg.answer('<i>Для начала мне нужно узнать сколько тебе лет?</i>', parse_mode = 'HTML')
        calories_function()
    except:
        pass

# Обработка команды - /bmi | !bmi
@dp.message_handler(commands = ['bmi'], commands_prefix = "/!")
async def bmi_processing(msg: types.Message):
    try:
        await FORM_DATA.age.set()
        await msg.answer('<i>Отлично! Ты выбрал(а) функцию <b>расчёта индекса массы тела</b>. Теперь мне нужна будет некоторая информация про тебя. Если ты вдруг введёшь неправильные данные, то можешь отменить действие командой: /cancel.</i>', parse_mode = 'HTML')
        await msg.answer('<i>Для начала мне нужно узнать сколько тебе лет?</i>', parse_mode = 'HTML')
        bmi_function()
    except:
        pass

"""     
/COMMANDS HANDLER
"""

"""     
MENU BUTTONS PROCESSING
"""
# Обработка кнопок меню выбора функций
@dp.message_handler(lambda message: message.text)
async def processing_menu(msg: types.Message):

    kb_menu = types.ReplyKeyboardRemove()

    if ( msg.text == '🍩 Рассчитать калории' ):
        try:
            await FORM_DATA.age.set()
            await bot.send_message(msg.from_user.id,'<i>Отлично! Ты выбрал(а) функцию <b>расчёта калоиий</b>. Теперь мне нужна будет некоторая информация про тебя. Если ты вдруг введёшь неправильные данные, то можешь отменить\nдействие командой: /cancel.</i>', reply_markup = kb_menu, parse_mode = 'HTML')
            await bot.send_message(msg.from_user.id,'<i>Для начала мне нужно узнать сколько тебе лет?</i>', parse_mode = 'HTML')
            calories_function()
        except:
            pass

    elif ( msg.text == '🧘‍♀️ ИМТ' ):
        try:
            await FORM_DATA_BMI.growth.set()
            await bot.send_message(msg.from_user.id,'<i>Отлично! Ты выбрал(а) функцию <b>расчёта индекса массы тела</b>. Теперь мне нужна будет некоторая информация про тебя. Если ты вдруг введёшь неправильные данные, то можешь отменить\nдействие командой: /cancel.</i>', reply_markup = kb_menu, parse_mode = 'HTML')
            await bot.send_message(msg.from_user.id,'<i>Для начала мне нужно узнать твой рост в см.</i>', parse_mode = 'HTML')
            bmi_function()
        except:
            pass

"""     
/MENU BUTTONS PROCESSING
"""

"""BOT FUNCTIONS"""

# Функция расчёта ИМТ
def bmi_function():

    # Принимаем рост
    @dp.message_handler(lambda message: message.text.isdigit(), state = FORM_DATA_BMI.growth)
    async def processing_growth(msg: types.Message, state: FSMContext):
        """Growth"""
        try:
            await state.update_data(growth = int(msg.text))
            await FORM_DATA_BMI.next()
            await msg.answer("<i>Последний вопрос и я смогу расчитать твой имт. Какой твой вес в кг?</i>", parse_mode = 'HTML')
        except:
            pass


    # Принимаем вес
    @dp.message_handler(lambda message: message.text.isdigit(), state = FORM_DATA_BMI.weight)
    async def processing_weight(msg: types.Message, state: FSMContext):
        global bmi, bmiText
        
        """Weight"""
        try:
            await FORM_DATA_BMI.next()
            await state.update_data(weight = int(msg.text))

            async with state.proxy() as data:
                bmi = calc_bmi(data['growth'], data['weight'])

            if bmi < 18.5:
                bmiText = 'недостаток веса ⚠️\n\nТвой ИМТ слишком низкий, старайся держать показатель в пределах нормы! 😕'
            elif bmi > 25:
                bmiText = 'избыток веса ⚠️\n\nТвой ИМТ слишком большой, старайся держать показатель в пределах нормы! 😕'
            else:
                bmiText = 'норма 👍\n\nТвой ИМТ в пределах нормы, постарайся удерживать его таким! 🙂'
            
            await bot.send_message(msg.from_user.id, 
            '✍️ Всё готово! Я посчитал твой индекс массы тела.\n\n✅ Твой ИМТ: <b>{0}</b> - {1}'
            .format(bmi, bmiText), parse_mode = 'HTML')

            await bot.send_message(msg.from_user.id, '<i>На этой картинке можешь посмотреть нормы ИМТ:</i>', parse_mode = 'HTML')

            await bot.send_photo(msg.from_user.id, open(BMI_NORMS_URL, 'rb'))

            await bot.send_message(msg.from_user.id, '<i>Если хочешь пересчитать,\nто напиши: /bmi или вернись в меню.\nЧтобы вернуться в меню выбора функций напиши: /menu или !m.</i>', parse_mode = 'HTML')

            await state.finish()
        except:
            pass

# Функция расчёта калорий
def calories_function():

    # Принимаем возраст
    @dp.message_handler(lambda message: message.text.isdigit(), state = FORM_DATA.age)
    async def processing_age(msg: types.Message, state: FSMContext):
        """Age"""
        try:
            async with state.proxy() as data:
                data['age'] = int(msg.text)
            await FORM_DATA.next()
            await msg.answer('<i>Теперь напиши свой рост в см.</i>', parse_mode = 'HTML')
        except:
            pass


    # Принимаем рост
    @dp.message_handler(lambda message: message.text.isdigit(), state = FORM_DATA.growth)
    async def processing_growth(msg: types.Message, state: FSMContext):
        """Growth"""
        try:
            await FORM_DATA.next()
            await state.update_data(growth = int(msg.text))
            await msg.answer('<i>Для расчёта пригодится твой вес в кг. Жду...</i>', parse_mode = 'HTML')
        except:
            pass


    # Принимаем вес
    @dp.message_handler(lambda message: message.text.isdigit(), state = FORM_DATA.weight)
    async def processing_weight(msg: types.Message, state: FSMContext):
        """Weight"""
        try:
            await FORM_DATA.next()
            await state.update_data(weight = int(msg.text))
            await msg.answer('<i>Выбери свой пол.</i>', reply_markup = kb_gender, parse_mode = 'HTML')
        except:
            pass


    # Обработка кнопок - genderMale и genderFemale
    @dp.callback_query_handler(text_contains = 'gender', state = FORM_DATA.gender)
    async def processing_gender(callback_query: types.CallbackQuery, state: FSMContext):
        try:
            await FORM_DATA.next()
            async with state.proxy() as data:
                data['gender'] = callback_query.data
            await bot.send_message(callback_query.from_user.id,
                '<i>Почти всё! Чтобы получить наиболее точные результаты, мне нужно знать насколько ты актиный(ая). Выбери один из '
                'вариантов.</i>', reply_markup = kb_active, parse_mode = 'HTML')
        except:
            pass


    # Обработка кнопок - active
    @dp.callback_query_handler(lambda call: call.data, state = FORM_DATA.active)
    async def processing_active(callback_query: types.CallbackQuery, state: FSMContext):
        try:
            await FORM_DATA.next()
            async with state.proxy() as data:
                data['active'] = float(callback_query.data)
            await bot.send_message(callback_query.from_user.id, '<i>Теперь я знаю всё, что нужно! По какой формуле расчитать суточную норму?</i>', reply_markup = kb_formuls, parse_mode = 'HTML')
        except:
            pass


    # Обработка кнопок - formuls
    @dp.callback_query_handler(text_contains = 'formula', state = '*')
    async def processing_formuls(callback_query: types.CallbackQuery, state: FSMContext):
        global result, weightKeep, weightLoss, fastWeightLost
        
        try:
            async with state.proxy() as data:
                if callback_query.data == 'formula_1':
                    if data['gender'] == 'genderMale':
                        result = calc_sanJeor_male(data['age'], data['growth'], data['weight'], data['active'])
                    elif data['gender'] == 'genderFemale':
                        result = calc_sanJeor_female(data['age'], data['growth'], data['weight'], data['active'])
                    else:
                        result = calc_sanJeor_male(data['age'], data['growth'], data['weight'], data['active'])
                elif callback_query.data  == 'formula_2':
                    if data['gender'] == 'genderMale':
                        result = calc_benidikt_male(data['age'], data['growth'], data['weight'], data['active'])
                    elif data['gender'] == 'genderFemale':
                        result = calc_benidikt_female(data['age'], data['growth'], data['weight'], data['active'])
                    else:
                        result = calc_benidikt_male(data['age'], data['growth'], data['weight'], data['active'])

            # calories calculation 
            weightKeep = round(result)
            weightLoss = round(result - (result * 0.2))
            fastWeightLost = round(weightLoss - (weightLoss * 0.25))

            if (callback_query.data == 'formula_1') or (callback_query.data == 'formula_2'):
                await bot.send_message(callback_query.from_user.id, md.text(
                    md.text('✍️ Всё готово! Я посчитал для тебя количество калорий в сутки.'),
                    md.text(' '),
                    md.text('✅ Для удержания веса: ', md.bold(weightKeep), 'кк.'),
                    md.text('✅ Для снижения веса: ', md.bold(weightLoss), 'кк.'),
                    md.text('✅ Для быстрого снижения веса: ', md.bold(fastWeightLost), 'кк.'),
                    sep = '\n'), parse_mode = ParseMode.MARKDOWN)

                await bot.send_message(callback_query.from_user.id, '<i>Если хочешь пересчитать,\nто напиши: /calories или вернись в меню.\nЧтобы вернуться в меню выбора функций напиши: /menu или !m.</i>', parse_mode = 'HTML')

                await state.finish()
        except:
            pass

"""/BOT FUNCTIONS"""
