# Доработанный вариант формулы Миффлина-Сан Жеора для мужчин
def calc_sanJeor_male(age, growth, weight, active):
    return ( ( 10 * weight ) + ( 6.25 * growth ) - ( 5 * age ) + 5 ) * active

# Доработанный вариант формулы Миффлина-Сан Жеора для жунщин
def calc_sanJeor_female(age, growth, weight, active):
    return ( ( 10 * weight ) + ( 6.25 * growth ) - ( 5 * age ) + 161 ) * active

# Формула Харриса-Бенедикта. Базальный метаболизм BMR для мужчин
def calc_benidikt_male(age, growth, weight, active):
    return ( 66.6 + ( 13.7 * weight ) + ( 5 * growth ) - ( 6.8 * age ) ) * active

# Формула Харриса-Бенедикта. Базальный метаболизм BMR для женщин
def calc_benidikt_female(age, growth, weight, active):
    return ( 655  + ( 9.6 * weight ) + ( 1.8  * growth ) - ( 4.7 * age ) ) * active

# Формула для расчёта ИМТ
def calc_bmi(growth, weight):
    return round (weight / ( (growth / 100)**2 ), 1 )
