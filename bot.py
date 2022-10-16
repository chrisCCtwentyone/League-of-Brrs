"""     IMPORTAZIONI        """
from telegram import *
from telegram.ext import *
from requests import *
import random 


"""     TOKEN       """
#Token identificativo del mio bot "______" con tag "______"
TOKEN = "5562164106:AAE2cjpILKLGVnR7HLtshnMk5o2GOZCAkTg"


"""     VARIABILI       """
randomChampImg = "Random Champ Image"
randomChampSuggestion = "Random Champ Suggestions"
searchAChampion = "Search a Champ"

randomChampImgUrl = ""
campioni = ["aatrox","ahri","akali","alistar","amumu","anivia","annie","aphelios",
            "ashe","aurelion sol","azir","bard","blitzcrank","brand","braum",
            "caitlyn","camille","cassiopeia","cho'gath","corki","darius","diana",
            "dr. mundo","draven","ekko","elise","evelynn","ezreal","fiddlesticks",
            "fiora","fizz","galio","gangplank","garen","gnar","gragas","graves",
            "hecarim","heimerdinger","illaoi","irelia","ivern","janna","jarvan IV",
            "jax","jayce","jhin","jinx","kai'sa","kalista","karma","karthus",
            "kassadin","katarina","kayle","kayn","kennen","kha'zix","kindred,kled",
            "kog'Maw","leblanc","lee sin","leona","lillia","lissandra","lucian",
            "lulu","lux","malphite","malzahar","maokai","master yi","miss fortune",
            "mordekaiser","morgana","nami","nasus","nautilus","neeko","nidalee",
            "nocturne","nunu and willump","olaf","orianna","ornn","pantheon",
            "poppy","pyke","qiyana","quinn","rakan","rammus","rek'sai","rell",
            "renekton","rengar","riven","rumble","ryze","samira","sejuani","senna",
            "seraphine","sett","shaco","shen","shyvana","singed","sion","sivir",
            "skarner","sona","soraka","swain","sylas","syndra","tahm kench",
            "taliyah","talon","taric","teemo","thresh","tristana","trundle",
            "tryndamere","twisted fate","twitch","udyr","urgot","varus","vayne",
           " veigar","vel'koz","vi","viktor","vladimir","volibear","warwick",
           "wukong","xayah","xerath","xin zhao","yasuo","yone","yorick","yuumi",
           "zac","zed","ziggs","zilean","zoe","zyra"]

def start(update, context):
    update.message.reply_text("🗡Benvenuto nella landa dei consiglieri🌎")

def messageHandler(update, context):
    if randomChampSuggestion in update.message.text:
        update.message.reply_text(random.choice(campioni))
    if randomChampImgUrl in update.message.text:
        update.message.reply_text("https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki?file="+random.choice(campioni)+"Banner.png")
    if searchAChampion in update.message.text:
        update.message.reply_text("https://leagueoflegends.fandom.com/wiki/"+random.choice(campioni)+"/LoL")

def menu(update, context):
    #Lista di bottoni dove aggiungo dei keyboard buttons in cui scrivo solo il titolo
    buttons = [[KeyboardButton("Random Champ Image"), KeyboardButton("Random Champ Suggestions")],
                [ KeyboardButton("Search a Champ"), KeyboardButton("Do nothing")]]
    #Messaggio da inviare quando digito il comando menu ""non so bene a che serve chat_id ma lo metto""
    context.bot.send_message(chat_id = update.effective_chat.id, text="Select an option from the menu!",
    reply_markup = ReplyKeyboardMarkup(buttons))


updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
updater.dispatcher.add_handler(CommandHandler('menu', menu))
print("Bot in ascolto...")
updater.start_polling()