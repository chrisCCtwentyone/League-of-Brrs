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
campioni = ["Aatrox","Ahri","Akali","Alistar","Amumu","Anivia","Annie","Aphelios",
            "Ashe","Aurelion_Sol","Azir",
            
            "Bard","Blitzcrank","Brand","Braum",
            
            "Caitlyn","Camille","Cassiopeia","Cho'Gath","Corki",
            
            "Darius","Diana","Dr._Mundo","Draven",
            
            "Ekko","Elise","Evelynn","Ezreal",
            
            "Fiddlesticks","Fiora","Fizz",
            
            "Galio","Gangplank","Garen","Gnar","Gragas","Graves",
            
            "Hecarim","Heimerdinger",
            
            "Illaoi","Irelia","Ivern",
            
            "Janna","Jarvan_IV", "Jax","Jayce","Jhin","Jinx",
            
            "Kai'Sa","Kalista","Karma","Karthus","Kassadin","Katarina",
            "Kayle","Kayn","Kennen","Kha'Zix","Kindred" ,"Kled",
            "Kog'Maw",
            
            "LeBlanc","Lee_Sin","Leona","Lillia","Lissandra","Lucian",
            "Lulu","Lux",
            
            "Malphite","Malzahar","Maokai","Master_Yi","Miss_Fortune",
            "Mordekaiser","Morgana",
            
            "Nami","Nasus","Nautilus","Neeko","Nidalee",
            "Nocturne","Nunu",
            
            "Olaf","Orianna","Ornn",
            
            "Pantheon","Poppy","Pyke",
            
            "Qiyana","Quinn",
            
            "Rakan","Rammus","Rek'Sai","Rell","Renekton","Rengar","Riven",
            "Rumble","Ryze",
            
            "Samira","Sejuani","Senna","Seraphine","Sett","Shaco","Shen","Shyvana",
            "Singed","Sion","Sivir","Skarner","Sona","Soraka","Swain","Sylas","Syndra",
            
            "Tahm_Kench","Taliyah","Talon","Taric","Teemo","Thresh","Tristana",
            "Trundle","Tryndamere","Twisted_Fate","Twitch",
            
            "Udyr","Urgot",
            
            "Varus","Vayne","Veigar","Vel'Koz","Vi","Viktor","Vladimir","Volibear",
            
            "Warwick","Wukong",
            
            "Xayah","Xerath","Xin_Zhao",
            
            "Yasuo","Yone","Yorick","Yuumi",

            "Zac","Zed","Ziggs","Zilean","Zoe","Zyra"]


randomChampImg = "Immagine Campione casuale"
randomChampSuggestion = "Suggerisci Campione casuale"
searchAChamp = "Cerca un Campione casuale"




"""     METODI      """
#/start
def start(update, context):
    update.message.reply_text("🗡Benvenuto nella landa dei consiglieri🌎")

#Quando deve rispondere
def rispondi(update, context):
    testo = update.message.text.lower()  #text.lower manda tutto in minuscolo a prescindere
    
    #Controllo su nomi strani:
    testo2 = testo
    if testo2 == "Aurelion" or "Aurelion sol":
        testo = "Aurelion_Sol"
    elif testo2 == "Chogath" or "Cho Gath":
        testo = "Cho'Gath"
    elif testo2 == "Mundo" or "Dr. mundo" or "Dr. Mundo": 
        testo = "Dr._Mundo"
    elif testo2 == "Jarvan" or "Jarvan 4"or "Jarvan IV":
        testo = "Jarvan_IV"
    elif testo2 == "Kaisa" or "Kai Sa" or "KaiSa":
        testo = "Kai'Sa"
    elif testo2 == "Kazix" or "Kha Zix" or "KhaZix":
        testo = "Kha'Zix"    
    elif testo2 == "Kog" or "Kog Maw"or "Kogmaw" or "KogMaw":
        testo = "Kog'Maw"
    elif testo2 == "Leblanc" or "Le Blanc":
        testo = "LeBlanc"
    elif testo2 == "LeeSin" or "Lee Sin"or "Leesin" or "Lee sin":
        testo = "Lee_Sin"
    elif testo2 == "MasterYi" or "Master Yii"or "Master Yi" or "Yi":
        testo = "Master_Yi"
    elif testo2 == "Miss Fortune" or "MissFortune" or "MF"or "Miss" or "Tettona":
        testo = "Miss_Fortune"
    elif testo2 == "Nunu and Willupo" or "Nunu&Willump":
        testo = "Nunu"
    elif testo2 == "RekSai" or "Rek Sai":
        testo = "Rek'Sai"
    elif testo2 == "Tahm" or "Tahm Kench" or "TahmKench"or "Kench":
        testo = "Tahm_Kench"
    elif testo2 == "Twisted" or "TF" or "Twisted Fate"or "TwistedFate":
        testo = "Twisted_Fate"
    elif testo2 == "Velkoz" or "Vel Koz" or "Velkoz":
        testo = "Vel'Koz"
    elif testo2 == "Xin" or "Xin Zhao" or "XinZhao" or "Xin Zao":
        testo = "Xin_Zhao"

    #Ricerca campioni
    elif testo in campioni: 
        update.message.reply_text(f'https://leagueoflegends.fandom.com/wiki/{testo}/LoL')

    #Nome casuale campione
    elif randomChampSuggestion in update.message.text:
        update.message.reply_text(random.choice(campioni))
    #Immagine campione casuale
    elif randomChampImg in update.message.text:
        update.message.reply_text(f"https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki?file={random.choice(campioni)}Banner.png")
    #Campione casuale
    elif searchAChamp in update.message.text:
        update.message.reply_text(f"https://leagueoflegends.fandom.com/wiki/{random.choice(campioni)}/LoL")
    
    #Se non è andato nulla
    else: 
        risposta = choice(noncapisco)
        update.message.reply_text(risposta)

#/menu
def menu(update, context):
    #Lista di bottoni dove aggiungo dei keyboard buttons in cui scrivo solo il titolo
    buttons = [[KeyboardButton(randomChampImg), KeyboardButton(randomChampSuggestion)],
                [ KeyboardButton(searchAChamp), KeyboardButton("Do nothing")]]
    
    #Messaggio da inviare quando digito il comando menu
    context.bot.send_message(chat_id = update.effective_chat.id, text="Come posso aiutarti?",
    reply_markup = ReplyKeyboardMarkup(buttons))


"""     RICHIAMO FUNZIONI       """
updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('menu', menu))
updater.dispatcher.add_handler(MessageHandler(Filters.text, rispondi))
print("Bot in ascolto")
updater.start_polling() #resta in ascolto e pronto a rispondere