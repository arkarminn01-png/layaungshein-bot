import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Render တွင် Proxy လုံးဝ မလိုတော့ပါ
TOKEN = '8225664945:AAFkByoevUyukF8sulcSoiDoFvFCs_Ona3g'
ADMIN_ID = 6248081977 
bot = telebot.TeleBot(TOKEN)

user_credits = {}

# Coin ဈေးနှုန်းနှင့် ငွေလွှဲရန် အချက်အလက်
PRICE_LIST = (
    "💰 *La Yaung Shein Coin ဈေးနှုန်းများ*\n\n"
    "• ၆ Coin (၆ ပုဒ်) = *၅,၀၀၀ ကျပ်*\n"
    "• ၁၅ Coin (၁၅ ပုဒ်) = *၁၂,၀၀၀ ကျပ်*\n"
    "• ၃၀ Coin (VIP) = *၂၀,၀၀၀ ကျပ်*\n\n"
    "🏦 *ငွေလွှဲရန် အကောင့်များ:*\n"
    "🔹 KBZPay: 09899887847 (Arkar Min)\n"
    "🔹 WavePay: 09777170649 (Arkar Min)\n\n"
    "⚠️ ငွေလွှဲပြီးပါက Screenshot ကို @phyolay54298 သို့ ပို့ပေးပါ။"
)

@bot.message_handler(commands=['start'])
def start_message(message):
    uid = message.from_user.id
    if uid not in user_credits:
        user_credits[uid] = 2  # Free ၂ ပုဒ် အစမ်းပေးခြင်း
    
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("💰 Coin ဝယ်ယူရန်", callback_data="buy_coin"))
    markup.row(InlineKeyboardButton("📊 ကျွန်ုပ်၏ လက်ကျန် Coin", callback_data="check_balance"))
    
    msg = (
        "🎬 *La Yaung Shein AI Movie Recap*\n\n"
        f"လက်ရှိလက်ကျန်: *{user_credits[uid]} Coin*\n\n"
        "📹 ဗီဒီယိုဖိုင် သို့မဟုတ် Link ပို့ပေးခြင်းဖြင့် စတင်နိုင်ပါပြီ။"
    )
    bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "buy_coin":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("📩 Screenshot ပို့ရန် (Admin)", url="https://t.me/phyolay54298"))
        bot.send_message(call.message.chat.id, PRICE_LIST, reply_markup=markup, parse_mode="Markdown")
    elif call.data == "check_balance":
        bot.answer_callback_query(call.id, f"သင့်တွင် {user_credits.get(call.from_user.id, 0)} Coin ရှိပါသည်။")

# Admin အတွက် Coin ဖြည့်ပေးသည့် စနစ်
@bot.message_handler(commands=['add'])
def add_coin(message):
    if message.from_user.id == ADMIN_ID:
        try:
            _, target_id, amount = message.text.split()
            target_id = int(target_id)
            amount = int(amount)
            user_credits[target_id] = user_credits.get(target_id, 0) + amount
            bot.reply_to(message, f"✅ User {target_id} ဆီသို့ {amount} Coin ဖြည့်ပြီးပါပြီ။")
            bot.send_message(target_id, f"🎉 လူကြီးမင်းထံသို့ {amount} Coin ဖြည့်သွင်းပေးလိုက်ပါပြီ။")
        except:
            bot.reply_to(message, "❌ ပုံစံ: /add USER_ID AMOUNT")

bot.polling(none_stop=True)
