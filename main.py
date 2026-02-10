import telebot

# Render အတွက် Proxy လုံးဝ မလိုတော့ပါ
TOKEN = '8225664945:AAFkByoevUyukF8sulcSoiDoFvFCs_Ona3g'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🎬 La Yaung Shein Bot အောင်မြင်စွာ အလုပ်လုပ်နေပါပြီ (Render.com)!")

if __name__ == "__main__":
    bot.polling(none_stop=True)

