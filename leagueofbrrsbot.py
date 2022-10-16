"""     IMPORTAZIONI    """
#Import per scelte casuali
from random import choice

#Import per rendere il bot responsivo
from telegram import *
from telegram.ext import * #Updater, CommandHandler, MessageHandler, Filters
from requests import *
import random



"""     TOKEN       """
#Token identificativo del mio bot "League of Brr's" con tag "leagueofbrrsbot"
TOKEN = "5562164106:AAE2cjpILKLGVnR7HLtshnMk5o2GOZCAkTg"


"""     VARIABILI   """
#Elenco risposte 
noncapisco = ["Non ho capito", "Non capisco", "Ripeti", "Ehm...non ho capito xd",
                "Idk bro, riscrivi", "Prova a riscrivere", "Non ho capito il comando"]
#Elenco Campioni                
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


randomChampImg = "Random Champ Image"
randomChampSuggestion = "Random Champ Suggestions"
searchAChampion = "Search a Champ"
randomChampImgUrl = "Random Champ Image"



"""     METODI      """
#/start
def start(update, context):
    update.message.reply_text("🗡Benvenuto nella landa dei consiglieri🌎")

#Quando deve rispondere
def rispondi(update, context):
    testo = update.message.text.lower() #text.lower così manda tutto in minuscolo a prescindere
    
    if randomChampSuggestion in update.message.text:
        update.message.reply_text(random.choice(campioni))
    elif testo in campioni: 
        update.message.reply_text(f'https://leagueoflegends.fandom.com/wiki/{testo}/LoL')
    elif randomChampImgUrl in update.message.text:
        update.message.reply_text(f"https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki?file={random.choice(campioni)}Banner.png")
    elif searchAChampion in update.message.text:
        update.message.reply_text(f"https://leagueoflegends.fandom.com/wiki/{random.choice(campioni)}/LoL")
    else: 
        risposta = choice(noncapisco)
        update.message.reply_text(risposta)

#/menu
def menu(update, context):
    #Lista di bottoni dove aggiungo dei keyboard buttons in cui scrivo solo il titolo
    buttons = [[KeyboardButton("Random Champ Image"), KeyboardButton("Random Champ Suggestions")],
                [ KeyboardButton("Search a Champ"), KeyboardButton("Do nothing")]]
    #Messaggio da inviare quando digito il comando menu
    context.bot.send_message(chat_id = update.effective_chat.id, text="Select an option from the menu!",
    reply_markup = ReplyKeyboardMarkup(buttons))


"""     RICHIAMO FUNZIONI       """
updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('menu', menu))
updater.dispatcher.add_handler(MessageHandler(Filters.text, rispondi))
print("Bot in ascolto")
updater.start_polling() #resta in ascolto e pronto a rispondere