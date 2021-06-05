import requests
import os
print("Made with Love by ❤️❤️❤️Rohan Raj❤️❤️❤️")
print("Made with Love by ❤️❤️❤️Rohan Raj❤️❤️❤️")
print("Version 1.0")
print("\033[91m Checking dependencies... \033[0m")
os.system("bash Requirements.sh")
def menu() :
    print("1):-   Send a Message to Any Number")
    print("2):-   Check if the Message is Delivered or not")
def control() :
    ctrl = input("What are You Gonna Choose : ")
    if ctrl == "1" :
        sms()
    elif ctrl == "2" :
        status()
    else :
        print("Invalid number")
def sms() :
   phone_no = input("Please Enter Your Country Code and Phone Number With a Plus     \n    Example :- +911122334455:\n ")
   msg = input("message to send : ")

   resp = requests.post('https://textbelt.com/text',{
	'phone' : phone_no,
	'message' : msg ,
	'key' : 'textbelt'
   })

   print(resp.text)
   if '"success" : true' in resp.text :
       print('Your Message is Delivered! ')
   if '"success" : false' in resp.text :
       print("Failed to Send Message!\n Sorry!! Try again!! ")
def status() :
  textID = input("Enter textID of sms : ") 
  os.system(f"curl https://textbelt.com/status/{textID}")
os.system("clear")
os.system("toilet --gay -f ascii9.tlf 'SMS_Sender' ")
print("\033[96mCoded by - Rohan Raj")
menu()
control()
