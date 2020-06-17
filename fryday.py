import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import getpass
import wikipedia
import ctypes
import win32gui, win32con
import time

# The_program_to_hide = win32gui.GetForegroundWindow()
# win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)

from ctypes import wintypes 
from time import gmtime, strftime
import datetime
currentdate=strftime("%d-%m-%Y", gmtime())
currenttime=strftime("%H:%M:%S", gmtime())
username = getpass.getuser()
from selenium import webdriver
from pygame import mixer
speech=sr.Recognizer()

try:
	engine=pyttsx3.init()			#it will check for the driver if method is empty then it wil use default driver
except ImportError:
	print('Requested driver is not found')
except RuntimeError:
	print('Driver fails to initialize')
	
voices= engine.getProperty('voices')

chunk_size = 2048

greetings = ['hey Friday' ,'hey there', 'Friday', 'hello Friday', 'hello', 'hi', 'Hai', 'hey!', 'hey']
question = ['how are you', 'how are you doing', 'how you doing']
var1 = ['who are you', 'what is your name']
var2 = ['who made you', 'who created you']
var3 = ['what time is it', 'what is the time', 'time']
var4 = ['bye', 'Good bye', 'ok bye','see you soon' ]
var5 = ['play', 'song']
var6 = ['tell me a joke' , 'joke' , 'fresh my mind']
var7 = ['favourite colour' ,'what is you favourite colour', 'what is your favourite colour']
var8 = ['what date is it', 'what is the date', 'date', "today's date"]
var9 = ['what can you do for me Friday', 'what can you do for me', 'features of friday', 'command', 'commands', 'open command file for me', 'open command file']
rep1 = ['your welcome', 'glad i could help you....' , 'what else i can do for you boss ?']
info = ['May i know your name boss?']
web  = ['open website']
battery = ['remaining battery' ,'charging', 'battery', 'give me battery status', 'how much charging left in my laptop', 'battery status', 'battery status of my laptop','how much battery is still left', 'give me battery status of my laptop']
calling = ['hey friday', 'friday' , 'hello friday']
jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.']

for voice in voices:						
	print(voice.id)			
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
rate=engine.getProperty('rate')									#machine will speak											
engine.setProperty('rate',rate)

def speak_text_cmd(cmd):
	engine.say(cmd)
	engine.runAndWait()

def read_voice_cmd():

	voice_text=''
	# mixer.init()
	# mixer.music.load('repulsor.mp3')
	# mixer.music.play()
	print('Listening........')


	with sr.Microphone() as source:	
		speech.adjust_for_ambient_noise(source)
		audio=speech.listen(source)

	try:	
		voice_text=speech.recognize_google(audio)	
	except sr.UnknownValueError:
		print("Oops !! Didn't catch that")
		pass
	except	sr.RequestError as e:
		print('Network error.')
	return voice_text
	

if __name__ == '__main__':

	print(username)

	hour=int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak_text_cmd("Good Morning Boss !")

	elif hour>=12 and hour<18:
		speak_text_cmd("Good Afternoon Boss !")

	else:
		speak_text_cmd("Good evening Boss !")

	speak_text_cmd(username+'!! this is fryday your personal assistant !!')

		

	while True:

		voice_note=read_voice_cmd()
		print('Fryday : {}'.format(voice_note))
		mixer.init()
		mixer.music.load('repulsor.mp3')
	
	
		if voice_note in greetings:
			speak_text_cmd('At your service boss , what can i do for you today ?')
			mixer.music.play()
			continue
	

		elif voice_note in question:
			speak_text_cmd('I am fine bosss ....')
			mixer.music.play()
			continue
			
		elif voice_note in var1:
			speak_text_cmd('My name is friday and i am your personal assistant.')
			mixer.music.play()
			continue	
			
		elif voice_note in var2:
			speak_text_cmd('i was created by Mr. Kathan Mehta .... He is my real boss !!')
			mixer.music.play()
			continue
			
		elif voice_note in var3:
			speak_text_cmd('Current time is'+currenttime)
			print (currenttime)
			mixer.music.play()
			continue

		elif voice_note in var6:
			speak_text_cmd(jokes)
			mixer.music.play()
			continue

		elif voice_note in var7:
			speak_text_cmd('i am transaparent , i can fit into any colours boss !!')
			mixer.music.play()
			continue

		elif voice_note in var8:
			speak_text_cmd('Current date is'+currentdate)
			print (currentdate)
			mixer.music.play()
			continue

		elif voice_note in var9:

			# try:
			speak_text_cmd("Opening Command file for you ...")
			f=open("commands.txt",'r').read()
			print(f)
				# f1=readlines()
				# for x in f1:
				# 	print(x)

			# except Exception: 
			
			# 	speak_text_cmd('You can ask me following things boss : ')
			# 	print("['hey Friday' ,'hey there', 'Friday', 'hello Friday', 'hello', 'hi', 'Hai', 'hey!', 'hey']")
			# 	print("['how are you', 'how are you doing']")
			# 	print("['who are you', 'what is your name']")
			# 	print("['who made you', 'who created you']")
			# 	print("['what time is it', 'what is the time', 'time']")
			# 	print("['play', 'song']")
			# 	print("['tell me a joke' , 'joke' , 'fresh my mind']")
			# 	print("['favourite colour' ,'what is you favourite colour', 'what is your favourite colour']")
			# 	print("['what date is it', 'what is the date', 'date', 'date of today'] ")
			# 	print("['what can you do for me friday', 'what can you do for me', 'features of friday']")
			# 	print("['open website']")
			# 	print("['remaining battery' ,'charging', 'battery', 'give me battery status', 'how much charging left in my laptop', 'battery status', 'battery status of my laptop','how much battery is still left', 'give me battery status of my laptop']")
			# 	print("['hey friday', 'friday' , 'hello friday']")
			# 	print("['jokes']")
			
			time.sleep(5)
			mixer.music.play()
			continue

		elif 'play' and 'song' in voice_note:
			speak_text_cmd('playing song for you boss !')
			driver = webdriver.Chrome(executable_path="C:/practice/chromedriver.exe")
			driver.get("https://gaana.com/playlist/gaana-dj-bollywood-top-50-1")
			button = driver.find_element_by_id('p-list-play_all')
			button.click()
			mixer.music.play()
			continue	

		elif voice_note in battery:
			class SYSTEM_POWER_STATUS(ctypes.Structure):
			    _fields_ = [
			        ('ACLineStatus', wintypes.BYTE),
			        ('BatteryFlag', wintypes.BYTE),
			        ('BatteryLifePercent', wintypes.BYTE),
			        ('Reserved1', wintypes.BYTE),
			        ('BatteryLifeTime', wintypes.DWORD),
			        ('BatteryFullLifeTime', wintypes.DWORD),
			    ]

			SYSTEM_POWER_STATUS_P = ctypes.POINTER(SYSTEM_POWER_STATUS)

			GetSystemPowerStatus = ctypes.windll.kernel32.GetSystemPowerStatus
			GetSystemPowerStatus.argtypes = [SYSTEM_POWER_STATUS_P]
			GetSystemPowerStatus.restype = wintypes.BOOL

			status = SYSTEM_POWER_STATUS()
			if not GetSystemPowerStatus(ctypes.pointer(status)):
			    raise ctypes.WinError()
			print ('ACLineStatus', status.ACLineStatus)
			print ('BatteryFlag', status.BatteryFlag)
			print ('BatteryLifePercent', status.BatteryLifePercent)
			print ('BatteryLifeTime', status.BatteryLifeTime)
			print ('BatteryFullLifeTime', status.BatteryFullLifeTime)
			speak_text_cmd('remaning charging is')
			speak_text_cmd(status.BatteryLifePercent)
			speak_text_cmd('Percent Boss')
			mixer.music.play()

		elif 'thank you' in voice_note:
			speak_text_cmd(rep1)
			mixer.music.play()
			continue	


		elif 'information' and 'knowledge' in voice_note:
			wiki = wikipedia.summary(voice_note, sentences=2).strip()
			print(wiki)
			speak_text_cmd('according to wikipedia'+wiki)
			mixer.music.play()
			continue	
			


		elif 'Google' in voice_note:
			webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")
			mixer.music.play()
			continue
		
		elif 'shopping' in voice_note:
			speak_text_cmd('woah ! which website i can open for you sir ?')
			print('1. Amazon 2. Flipkart')
			speak_text_cmd('other shopping websites are dumb')
			mixer.music.play()
			continue
		

		elif 'Amazon' in voice_note:
			webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.amazon.in/s?k="+voice_note)
			mixer.music.play()
			continue
			
		elif 'Flipkart' in voice_note:	
			webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.flipkart.com/search?q="+voice_note)
			mixer.music.play()
			continue	

		elif 'launch' in voice_note:
			speak_text_cmd('Launching sir ! ....')
			os.system('explorer C:\\"{}"'.format(voice_note.replace('launch ', '')))
			# os.system('explorer K:\\"{}"'.format(voice_note.replace('open ', '')))
			# os.system('explorer T:\\"{}"'.format(voice_note.replace('open ', '')))
			print(voice_note)
			mixer.music.play()
			continue

		elif 'lock' in voice_note:
			speak_text_cmd('Your system is locked !')
			for value in ['pc','system','windows']:
				ctypes.windll.user32.LockWorkStation()
	

		elif 'shutdown' in voice_note:
			speak_text_cmd('Shutting of your PC !')
			os.system("shutdown /s /t 1")

		elif 'restart' in voice_note:
			speak_text_cmd('Restarting your PC Boss !')
			os.system("shutdown /r /t 1")

		elif voice_note in var4:
			speak_text_cmd('miss you boss ! ....')
			mixer.music.play()
			exit()
		
		elif 'YouTube' in voice_note:
			speak_text_cmd('Opening youtube for you boss !')
			webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://www.youtube.com/results?q="+voice_note)
			mixer.music.play()
			continue
			
		elif 'search' in voice_note:
			speak_text_cmd('Searching for you !')
			webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("www.google.com/search?q="+voice_note)
			print(voice_note)
			mixer.music.play()
			continue

		elif keyboard.press_and_release('q') :
		
			print("Enter is pressed")
			continue

		else:
			print(voice_note)
			continue
			
