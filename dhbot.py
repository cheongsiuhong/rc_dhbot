

# Import Scraping Components 
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#Initialize Telebot
from telegram.ext import Updater
updater = Updater(token='712599513:AAGhEcVjSfqGp4uue-WotcCwUtZ2Z0kEm8k')
dispatcher = updater.dispatcher

#Data logging
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Welcome to Cookhouse!")

from telegram.ext import CommandHandler, CallbackQueryHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def avg(arr):
    if len(arr) == 0:
      return "no votes yet"
    else:
      num = round(float(sum(arr)) / float(len(arr)))
      bstar = u"\u2605"
      wstar = u"\u2606"
      string = ""
      for i in range(5):
        num = num - 1
        if num >= 0:
          string = string + bstar
        else:
          string = string + wstar
      return string 

def dinner(bot, update):

    first_average = avg(firstls)
    second_average = avg(secondls)
    third_average = avg(thirdls)
    fourth_average = avg(fourthls)
    fifth_average = avg(fifthls)
    sixth_average = avg(sixthls)
    seventh_average = avg(seventhls)
    eighth_average = avg(eighthls)
    ninth_average = avg(ninthls)

    # Menu URL and HTML Scrape

    browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    browser.get('https://uci.nus.edu.sg/ohs/current-residents/students/daily-menu/')
    elem = browser.find_element_by_class_name("tbl-menuu")

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    browser.close()
    #Replacements
    help_yourself = "<td>HELP YOURSELF   ~   RATING: " + first_average +"\n</td>"
    western = "<td>WESTERN   ~   RATING: " + second_average +"\n</td>"
    noodle = "<td>NOODLE   ~   RATING: " + third_average +"\n</td>"
    asian = "<td>ASIAN   ~   RATING: " + fourth_average +"\n</td>"
    veg = "<td>VEGETARIAN   ~   RATING: " + fifth_average +"\n</td>"
    muslim = "<td>MUSLIM   ~   RATING: " + sixth_average +"\n</td>"
    grab = "<td>GRAB AND GO   ~   RATING: " + seventh_average +"\n</td>"
    indian = "<td>INDIAN   ~   RATING: " + eighth_average +"\n</td>"
    special = "<td>SPECIAL   ~   RATING: " + ninth_average +"\n</td>"

    for td in soup.select("td.imgtd"):
        for img in td.select("img"):
            if "https://www.hg.sg/nus_ohs_admin/images/menu/helpyourself.png" in img['src']:
                    td.replace_with(BeautifulSoup(help_yourself, 'html.parser'))
            if "https://www.hg.sg/nus_ohs_admin/images/menu/western.png" in img['src']:
                    td.replace_with(BeautifulSoup(western, 'html.parser'))
            if "//www.hg.sg/nus_ohs_admin/images/menu/noodle.png" in img['src']:
                    td.replace_with(BeautifulSoup(noodle, 'html.parser'))
            if "https://www.hg.sg/nus_ohs_admin/images/menu/asian.png" in img['src']:
                    td.replace_with(BeautifulSoup(asian, 'html.parser'))
            if "https://www.hg.sg/nus_ohs_admin/images/menu/veg.png" in img['src']:
                    td.replace_with(BeautifulSoup(veg, 'html.parser'))
            if "https://www.hg.sg/nus_ohs_admin/images/menu/muslim.png" in img['src']:
                    td.replace_with(BeautifulSoup(muslim, 'html.parser'))
            if "https://www.hg.sg/nus_ohs_admin/images/menu/grab.png" in img['src']:
                    td.replace_with(BeautifulSoup(grab, 'html.parser'))
            if "https://www.hg.sg/nus_ohs_admin/images/menu/indian.png" in img['src']:
                    td.replace_with(BeautifulSoup(indian, 'html.parser'))
            if "https://www.hg.sg/nus_ohs_admin/images/menu/specials.png" in img['src']:
                    td.replace_with(BeautifulSoup(special, 'html.parser'))

    for br in soup.find_all("br"):
        br.replace_with("\n")

    name_box = soup.find('table', attrs={'class': 'tbl-menuu'})

    name = name_box.get_text()
    bot.send_message(chat_id=update.message.chat_id, text=name)
    
dinner_handler = CommandHandler('dinner', dinner)
dispatcher.add_handler(dinner_handler)

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton

def menu1(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=menu1_message(),
                        reply_markup=menu1_keyboard())

def menu2(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=menu1_message(),
                        reply_markup=menu2_keyboard())
def menu3(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=menu1_message(),
                        reply_markup=menu3_keyboard())

def menu4(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=menu1_message(),
                        reply_markup=menu4_keyboard())

def menu5(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=menu1_message(),
                        reply_markup=menu5_keyboard())

def menu6(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=menu1_message(),
                        reply_markup=menu6_keyboard())

def menu7(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=menu1_message(),
                        reply_markup=menu7_keyboard())

def menu8(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=menu1_message(),
                        reply_markup=menu8_keyboard())

def menu9(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=menu1_message(),
                        reply_markup=menu9_keyboard())

def rate_menu(bot, update):
  update.message.reply_text(main_menu_message(),
                            reply_markup=main_menu_keyboard())

def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Help Yourself', callback_data='m1')],
              [InlineKeyboardButton('Western', callback_data='m2')],
              [InlineKeyboardButton('Noodle', callback_data='m3')],
              [InlineKeyboardButton('Asian', callback_data='m4')],
              [InlineKeyboardButton('Vegetarian', callback_data='m5')],
              [InlineKeyboardButton('Muslim', callback_data='m6')],
              [InlineKeyboardButton('Grab N Go', callback_data='m7')],
              [InlineKeyboardButton('Indian', callback_data='m8')],
              [InlineKeyboardButton('Special', callback_data='m9')]]
  return InlineKeyboardMarkup(keyboard)

def menu1_keyboard():
  keyboard = [[InlineKeyboardButton('1', callback_data='11')],
              [InlineKeyboardButton('2', callback_data='12')],
              [InlineKeyboardButton('3', callback_data='13')],
              [InlineKeyboardButton('4', callback_data='14')],
              [InlineKeyboardButton('5', callback_data='15')]]
  return InlineKeyboardMarkup(keyboard)

def menu2_keyboard():
  keyboard = [[InlineKeyboardButton('1', callback_data='21')],
              [InlineKeyboardButton('2', callback_data='22')],
              [InlineKeyboardButton('3', callback_data='23')],
              [InlineKeyboardButton('4', callback_data='24')],
              [InlineKeyboardButton('5', callback_data='25')]]
  return InlineKeyboardMarkup(keyboard)

def menu3_keyboard():
  keyboard = [[InlineKeyboardButton('1', callback_data='31')],
              [InlineKeyboardButton('2', callback_data='32')],
              [InlineKeyboardButton('3', callback_data='33')],
              [InlineKeyboardButton('4', callback_data='34')],
              [InlineKeyboardButton('5', callback_data='35')]]
  return InlineKeyboardMarkup(keyboard)

def menu4_keyboard():
  keyboard = [[InlineKeyboardButton('1', callback_data='41')],
              [InlineKeyboardButton('2', callback_data='42')],
              [InlineKeyboardButton('3', callback_data='43')],
              [InlineKeyboardButton('4', callback_data='44')],
              [InlineKeyboardButton('5', callback_data='45')]]
  return InlineKeyboardMarkup(keyboard)

def menu5_keyboard():
  keyboard = [[InlineKeyboardButton('1', callback_data='51')],
              [InlineKeyboardButton('2', callback_data='52')],
              [InlineKeyboardButton('3', callback_data='53')],
              [InlineKeyboardButton('4', callback_data='54')],
              [InlineKeyboardButton('5', callback_data='55')]]
  return InlineKeyboardMarkup(keyboard)

def menu6_keyboard():
  keyboard = [[InlineKeyboardButton('1', callback_data='61')],
              [InlineKeyboardButton('2', callback_data='62')],
              [InlineKeyboardButton('3', callback_data='63')],
              [InlineKeyboardButton('4', callback_data='64')],
              [InlineKeyboardButton('5', callback_data='65')]]
  return InlineKeyboardMarkup(keyboard)

def menu7_keyboard():
  keyboard = [[InlineKeyboardButton('1', callback_data='71')],
              [InlineKeyboardButton('2', callback_data='72')],
              [InlineKeyboardButton('3', callback_data='73')],
              [InlineKeyboardButton('4', callback_data='74')],
              [InlineKeyboardButton('5', callback_data='75')]]
  return InlineKeyboardMarkup(keyboard)

def menu8_keyboard():
  keyboard = [[InlineKeyboardButton('1', callback_data='81')],
              [InlineKeyboardButton('2', callback_data='82')],
              [InlineKeyboardButton('3', callback_data='83')],
              [InlineKeyboardButton('4', callback_data='84')],
              [InlineKeyboardButton('5', callback_data='85')]]
  return InlineKeyboardMarkup(keyboard)

def menu9_keyboard():
  keyboard = [[InlineKeyboardButton('1', callback_data='91')],
              [InlineKeyboardButton('2', callback_data='92')],
              [InlineKeyboardButton('3', callback_data='93')],
              [InlineKeyboardButton('4', callback_data='94')],
              [InlineKeyboardButton('5', callback_data='95')]]
  return InlineKeyboardMarkup(keyboard)


firstls = []
secondls = []
thirdls = []
fourthls = []
fifthls = []
sixthls = []
seventhls = []
eighthls = []
ninthls = []

def button(bot, update):
    query = update.callback_query
    num = int(query.data)
    score = num % 10
    cat = int(num / 10)
    if cat == 1:
      firstls.append(score)
      print(firstls)
    if cat == 2:
      secondls.append(score)
      print(secondls)
    if cat == 3:
      thirdls.append(score)
      print(thirdls)
    if cat == 4:
      fourthls.append(score)
      print(fourthls)
    if cat == 5:
      fifthls.append(score)
      print(fifthls)
    if cat == 6:
      sixthls.append(score)
      print(sixthls)
    if cat == 7:
      seventhls.append(score)
      print(seventhls)
    if cat == 8:
      eighthls.append(score)
      print(eighthls)
    if cat == 9:
      ninthls.append(score)
      print(ninthls)
    bot.edit_message_text(text="Your rating: {}".format(score),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)

############################# Messages #########################################
def main_menu_message():
  return 'Choose the cuisine you\'d like to rate:'

def menu1_message():
  return 'Please rate your food from 1 - Worst to 5 - Great:'


############################# Handlers #########################################

updater.dispatcher.add_handler(CallbackQueryHandler(menu1, pattern='m1'))
updater.dispatcher.add_handler(CallbackQueryHandler(menu2, pattern='m2'))
updater.dispatcher.add_handler(CallbackQueryHandler(menu3, pattern='m3'))
updater.dispatcher.add_handler(CallbackQueryHandler(menu4, pattern='m4'))
updater.dispatcher.add_handler(CallbackQueryHandler(menu5, pattern='m5'))
updater.dispatcher.add_handler(CallbackQueryHandler(menu6, pattern='m6'))
updater.dispatcher.add_handler(CallbackQueryHandler(menu7, pattern='m7'))
updater.dispatcher.add_handler(CallbackQueryHandler(menu8, pattern='m8'))
updater.dispatcher.add_handler(CallbackQueryHandler(menu9, pattern='m9'))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

rate_handler = CommandHandler('rate', rate_menu)
dispatcher.add_handler(rate_handler)


updater.start_polling() 