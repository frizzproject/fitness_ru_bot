from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

# Storage init
storage = MemoryStorage()

# Storage calories data
class FORM_DATA(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()
    active = State()

# Storage bmi data
class FORM_DATA_BMI(StatesGroup):
    growth = State()
    weight = State()