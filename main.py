from  aiogram.types import Message
from aiogram import Bot, Dispatcher, executor
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton

api = '6826234032:AAEyVS2Rt0SizWpym_F_SKxQ21QOCMwK1oY'
bot = Bot(api)
dp = Dispatcher(bot)
knopkalar_button = ReplyKeyboardMarkup(
    [
        [KeyboardButton("O'zbek"), KeyboardButton(text='Русский')]

    ]
)

bosh_button = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='Inspektorning harakatlari/harakatsizligi togri...')],
        [KeyboardButton(text='Murojaat holatini tekshirish')],
        [KeyboardButton(text='Mening murojatlarim')],
        [KeyboardButton(text='Murojat jonatish')],
        [KeyboardButton(text='❌Bekor qilish')]
    ]
)
rus_button = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='Жалоба на действия/бездействие инспектора')],
        [KeyboardButton(text='Проверить статус заявки')],
        [KeyboardButton(text='Мои запрос')],
        [KeyboardButton(text='Отправить обращение')],
        [KeyboardButton(text='❌Отменить')]
    ]
)
chiqish_button = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='🏛 Bosh Menyu')]
    ]
)

chiq_button = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='🏛 Bosh Menyu')]
    ]
)

ariza_button = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='🏛 Bosh Menyu')],
        [KeyboardButton(text='Sizda arizalar mavjudmas')]
    ]
)

murojat_button = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='F.I.SH')],
        [KeyboardButton(text='🏛 Bosh Menyu')]
    ]
)

@dp.message_handler(commands='start')
async def start(messaeg: Message):
    chatid = messaeg.chat.id
    await bot.send_message(chat_id=chatid, text="""Assalomu alaykum, iltimos tilni tanlang
Здравствуйте, выберите пожалуйста язык""", reply_markup=knopkalar_button)

@dp.message_handler(text="O'zbek")
async def ozbek(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='🏛 Bosh Menyu',reply_markup=bosh_button)

@dp.message_handler(text="Русский")
async def Русский(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='🏛 Главное меню',reply_markup=rus_button)

@dp.message_handler(text="🏛 Bosh Menyu")
async def harakat(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='🏛 Bosh Menyu',reply_markup=chiqish_button)

@dp.message_handler(text="Inspektorning harakatlari/harakatsizligi togri...")
async def harakat(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='Iltimos ariza raqamini kiriting',reply_markup=chiqish_button)

@dp.message_handler(text="Murojaat holatini tekshirish")
async def murojat(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='Iltimos ariza raqamini kiriting',reply_markup=chiq_button)

@dp.message_handler(text="Mening murojatlarim")
async def ariza(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='Iltimos ariza raqamini kiriting',reply_markup=ariza_button)

@dp.message_handler(text="Murojat jonatish")
async def murojat(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='Iltimos ariza raqamini kiriting',reply_markup=murojat_button)


dp.message_handler(text="❌Bekor qilish")
async def bekorqilish(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='🏛 Bosh Menyu',reply_markup=knopkalar_button)

shu_button = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='🏛 Главное меню')]
    ]
)

chi_button = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='🏛 Главное меню')]
    ]
)

azi_button = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='🏛 Главное меню')],
        [KeyboardButton(text='У вас нет приложений')]
    ]
)

t_button = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='Ф.И.Ш')],
        [KeyboardButton(text='🏛 Главное меню')]
    ]
)

@dp.message_handler(text="Жалоба на действия/бездействие инспектора")
async def sxoi(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='Пожалуйста, введите номер заявки',reply_markup=shu_button)

executor.start_polling(dp, skip_updates=True)
















