from tkinter import *
from tkinter import messagebox
import sqlite3


window = Tk()
window.title('YCT FINAL YEAR PROJECT Development of Credit Card Prevention & Detection System Using Luhn Algorithm')
window.geometry('1000x900')

window.configure(background='#aaaaaa')


window.columnconfigure(0, weight=1) # make the column 1 expand when the window is resized


#FOR DRY CODE
colspan = 2
labelcol = 0
labelfonts = ('Ariel', 16)
labelpady = 1
labelpadx = 10
labelsticky = 'W'
labelgridpady = 6
labelgridpadx = 30
labelgridipady = 10
labelgridipadx = 40

entrycol = 1
entrybd = 2
entryfonts = (15)
entrywidth = 20
entrypady = 6
entrypadx = 20
entrysticky = 'E'
entrygridpady = 4
entrygridpadx = 40
entrygridipady = 10
entrygridipadx = 70

#OUTPUT LABEL CLASS DECLARATION

label1A = StringVar()

label1B = StringVar()

label2A = StringVar()

label2B = StringVar()

label3A = StringVar()

label3B = StringVar()

label4A = StringVar()

label4B = StringVar()

label5A = StringVar()

label5B = StringVar()




#system's lists of pins
pinList = ("0846", "2028", "4004", "2102", "3333", "8725", "0606", "9070", "1019", "1116", "4401", "1070", "2348", "6111", "9133")

def accumulator(List):
    Sum = 0
    for p in List:
        Sum += p
    return Sum

def intConverter(oldList, newList):
    for j in oldList:
        numConv = int(j)
        newList.append(numConv)
    return newList

def tableName(a):
    if a == 'master card' or a == 'mastercard':
        return 'MASTER_CARD'
            
    else:
        return 'VISA_CARD'

def cardPinVerification(pinVar, pinList):
    if len(pinVar) < 1:
        return "empty"
    else:
        if (pinVar in pinList):
            return "true"
        else:
            return "false"


def cardOverallValidation(a, c, d, e, f, g, h, i, j, k):
    if (((a == "This Credit Card No and the pin is Valid")) and ((c == d) and (e == f) and (g == h) and (i == j))):
        return "This Card's Overall Details look good from here"
    
    elif ((a == "This Credit Card No is Valid but the pin is not given") and ((c == d) and (e == f) and (g == h) and (i == j))):
        return "This Card's Overall Details look good from here"

    elif ((a == "This Credit Card No and the pin is Valid") and not((c == d) and (e == f) and (g == h) and (i == j))):
        return "This Card's No is Valid but other Details of the card are inconsistence"
    
    elif ((a == "This Credit Card No is Valid but the pin is not given") and not((c == d) and (e == f) and (g == h) and (i == j))):
        return "This Card's No is Valid but other Details of the card are inconsistence"
    
    elif ((a == "This Credit Card No is Valid but the pin is Invalid") and(c == d) and (e == f) and (g == h) and (i == j)):
        return "This Card's No is Valid but other Details of the card are inconsistence"
    
    elif (a == "This Credit Card No is Invalid but the pin is valid" and ((c == d) and (e == f) and (g == h) and (i == j))):
        return "This Card's No is Invalid but other Details of the card are Valid"

    else:
        return "Scam!!!  Too many Details of this Card are Invalid"

def cardNoValidation(a, cardpinverify):
    if (a % 10 == 0) and (cardpinverify == "true"):
        b = "This Credit Card No and the pin is Valid"
        return b
    elif (a % 10 == 0) and (cardpinverify == "empty"):
        b = "This Credit Card No is Valid but the pin is not given"
        return b
    elif (a % 10 == 0) and (cardpinverify == "false"):
        b = "This Credit Card No is Valid but the pin is Invalid"
        return b
    elif not(a % 10 == 0) and (cardpinverify == "true"):
        b = "This Credit Card No is Invalid but the pin is valid"
        return b
    else:
        b = "This Credit Card No and the pin are Invalid"
        return b

def cardIndValidation(list):

    if list[0] == '1' or list[0] == '2':
        return "Aviation Industry"
    elif list[0] == '3':
        return "Travel Agency"
    elif list[0] == '4' or list[0] == '5':
        return "Banking Industry"
    elif list[0] == '6':
        return "Merchandising, Banking or Financial Industry"
    elif list[0] == '7':
        return "Petroleum Industry"
    elif list[0] == '8':
        return "Healthcare or Telecommunication Industry"
    elif list[0] == '9':
        return "National Assignment"



FirstDigitSet = []
SecondDigitSet = []
convintlist = []

# THE CARD VALIDATOR FUNCTION

def CardValidator():
    
    try:
        
        CardNo = cardNoVar.get()
          
        CardTypeUserEntry = cardTypeVar.get().lower()
        
        table_name = tableName(CardTypeUserEntry)

        CardIndUserEntry = cardIndVar.get()
        
        C = list(CardNo)
    
        CardInd = cardIndValidation(C)
    
        checkno = CardNo[:6]

        CardIssuerNameUserEntry = cardIssuerNameVar.get()

        CardIssuerLocationUserEntry = cardIssuerLocationVar.get()

        cardPinUserEntry = cardPinVar.get()
              

        #Database

        conn = sqlite3.connect('FDS.sqlite3')

        cur = conn.cursor()

        cur.execute ('DROP TABLE IF EXISTS MASTER_CARD')
        cur.execute ('CREATE TABLE MASTER_CARD(Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Issuing_Bank_Name TEXT, BRAND_TYPE TEXT, ISSUER_IDENTIFYING_NUMBER NUMBER, CARD_TYPE TEXT, ISO_COUNTRY_NAME TEXT)')
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ECO BANK NIGERIA PLC", "MASTER CARD", 512269, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ECO BANK NIGERIA PLC", "MASTER CARD", 512450, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ECO BANK NIGERIA PLC", "MASTER CARD", 512451, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ECO BANK NIGERIA PLC", "MASTER CARD", 528917, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ECO BANK NIGERIA PLC", "MASTER CARD", 532968, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ECO BANK NIGERIA PLC", "MASTER CARD", 537010, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ECO BANK NIGERIA PLC", "MASTER CARD", 537011, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ECO BANK NIGERIA PLC", "MASTER CARD", 548712, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ECO BANK NIGERIA PLC", "MASTER CARD", 558773, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ECO BANK NIGERIA PLC", "MASTER CARD", 531667, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ECO BANK NIGERIA PLC", "MASTER CARD", 528916, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ECO BANK NIGERIA PLC", "MASTER CARD", 548458, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ECO BANK NIGERIA PLC", "MASTER CARD", 548644, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("CSC BANK", "MASTER CARD", 515692, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("CSC BANK", "MASTER CARD", 515883, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("CSC BANK", "MASTER CARD", 528047, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("CSC BANK", "MASTER CARD", 532330, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("CSC BANK", "MASTER CARD", 535955, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("CSC BANK", "MASTER CARD", 547638, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("CSC BANK", "MASTER CARD", 550019, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("CSC BANK", "MASTER CARD", 557972, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("CSC BANK", "MASTER CARD", 533897, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("CSC BANK", "MASTER CARD", 557669, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("CSC BANK", "MASTER CARD", 528955, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("INTERCONTINENTAL BANK PLC", "MASTER CARD", 517754, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("INTERCONTINENTAL BANK PLC", "MASTER CARD", 520053, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("INTERCONTINENTAL BANK PLC", "MASTER CARD", 521623, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("INTERCONTINENTAL BANK PLC", "MASTER CARD", 524311, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("INTERCONTINENTAL BANK PLC", "MASTER CARD", 529975, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("INTERCONTINENTAL BANK PLC", "MASTER CARD", 553420, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("INTERCONTINENTAL BANK PLC", "MASTER CARD", 557693, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("INTERCONTINENTAL BANK PLC", "MASTER CARD", 531213, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("INTERCONTINENTAL BANK PLC", "MASTER CARD", 525634, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("INTERCONTINENTAL BANK PLC", "MASTER CARD", 531165, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ZENITH BANK", "MASTER CARD", 531525, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ZENITH BANK", "MASTER CARD", 539941, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ZENITH BANK", "MASTER CARD", 540884, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ZENITH BANK", "MASTER CARD", 542231, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ZENITH BANK", "MASTER CARD", 547160, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ZENITH BANK", "MASTER CARD", 512336, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ZENITH BANK", "MASTER CARD", 533301, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ZENITH BANK", "MASTER CARD", 559443, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ZENITH BANK", "MASTER CARD", 530519, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("GT BANK", "MASTER CARD", 532732, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("GT BANK", "MASTER CARD", 541508, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("GT BANK", "MASTER CARD", 541569, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("GT BANK", "MASTER CARD", 552264, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("GT BANK", "MASTER CARD", 552279, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("GT BANK", "MASTER CARD", 539983, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("GT BANK", "MASTER CARD", 533853, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("GT BANK", "MASTER CARD", 533856, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("FIRST BANK OF NIGERIA PLC", "MASTER CARD", 539923, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("FIRST BANK OF NIGERIA PLC", "MASTER CARD", 543338, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("UNITY BANK PLC", "MASTER CARD", 551609, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("UNITY BANK PLC", "MASTER CARD", 536399, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("STANBIC IBTC BANK", "MASTER CARD", 552160, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("STANBIC IBTC BANK", "MASTER CARD", 542077, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("CITIBANK NIGERIA LTD", "MASTER CARD", 555060, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("CITIBANK NIGERIA LTD", "MASTER CARD", 555061, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("CITIBANK NIGERIA LTD", "MASTER CARD", 555062, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ACCESS BANK", "MASTER CARD", 536613, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("UBA", "MASTER CARD", 519911, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("Keystone Bank", "MASTER CARD", 555940, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO MASTER_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("First City Monument Bank", "MASTER CARD", 524282, "CREDIT", "NIGERIA"))




        conn.commit()
    
        cur.execute ('DROP TABLE IF EXISTS VISA_CARD')
        cur.execute ('CREATE TABLE VISA_CARD(Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Issuing_Bank_Name TEXT, BRAND_TYPE TEXT, ISSUER_IDENTIFYING_NUMBER NUMBER, CARD_TYPE TEXT, ISO_COUNTRY_NAME TEXT)')
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ZENITH Bank", "VISA CARD", 412053, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ZENITH Bank", "VISA CARD", 413183, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ZENITH Bank", "VISA CARD", 450073, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ZENITH Bank", "VISA CARD", 450075, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ZENITH Bank", "VISA CARD", 450090, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ZENITH Bank", "VISA CARD", 450093, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ZENITH Bank", "VISA CARD", 450074, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ZENITH Bank", "VISA CARD", 413103, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("UBA", "VISA CARD", 404905, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("UBA", "VISA CARD", 407591, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("UBA", "VISA CARD", 420359, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("UBA", "VISA CARD", 422584, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("UBA", "VISA CARD", 444584, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("UBA", "VISA CARD", 444586, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("UBA", "VISA CARD", 484842, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("UBA", "VISA CARD", 422594, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("UBA", "VISA CARD", 428223, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("UBA", "VISA CARD", 422584, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("UBA", "VISA CARD", 420358, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("GT BANK", "VISA CARD", 420319, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("GT BANK", "VISA CARD", 428222, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("GT BANK", "VISA CARD", 445807, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("GT BANK", "VISA CARD", 418742, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("GT BANK", "VISA CARD", 420320, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("SCBN", "VISA CARD", 422127, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("SCBN", "VISA CARD", 423895, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("SCBN", "VISA CARD", 427889, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("SCBN", "VISA CARD", 422808, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("SCBN", "VISA CARD", 439358, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("FIRST BANK OF NIGERIA PLC", "VISA CARD", 427011, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("FIRST BANK OF NIGERIA PLC", "VISA CARD", 427013, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("FIRST BANK OF NIGERIA PLC", "VISA CARD", 427014, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("FIRST BANK OF NIGERIA PLC", "VISA CARD", 427876, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("FIRST BANK OF NIGERIA PLC", "VISA CARD", 427012, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ACCESS BANK", "VISA CARD", 427873, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ACCESS BANK", "VISA CARD", 469665, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ACCESS BANK", "VISA CARD", 469666, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ACCESS BANK", "VISA CARD", 469667, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ACCESS BANK", "VISA CARD", 470484, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ACCESS BANK", "VISA CARD", 475177, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ACCESS BANK", "VISA CARD", 412702, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ACCESS BANK", "VISA CARD", 403660, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ACCESS BANK", "VISA CARD", 407586, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("ACCESS BANK", "VISA CARD", 475175, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("UNION BANK", "VISA CARD", 433960, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("UNION BANK", "VISA CARD", 469023, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("UNION BANK", "VISA CARD", 428272, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("Polaris Bank", "VISA CARD", 419227, "CREDIT", "NIGERIA"))
        cur.execute ('INSERT INTO VISA_CARD ("Issuing_Bank_Name", "BRAND_TYPE", "ISSUER_IDENTIFYING_NUMBER", "CARD_TYPE", "ISO_COUNTRY_NAME") VALUES (?, ?, ?, ?, ?)', ("Diamond BANK", "VISA CARD", 496009, "CREDIT", "NIGERIA"))
    
        conn.commit()
        
        
        cur.execute ('SELECT * FROM ' + table_name + ' WHERE "ISSUER_IDENTIFYING_NUMBER" == ' + str(checkno))
        
        conn.commit()

        r = (cur.fetchall())
        record = r[0]
        
        RealCardIssuerName = record[1]
        RealCardBrandType = record[2]
        RealCardIssuerLocation = record[5]
        

#print(' The total number of row in the database where d condition is true')

        conn.commit()
        
        initFirstDigitSet = C[::2]
        initSecondDigitSet = C[1::2]

        
        

        intConverter(initFirstDigitSet, convintlist)
        intConverter(initSecondDigitSet, SecondDigitSet)


        for i in convintlist:
            num1 = i * 2
            if num1 > 9:
                num1str = str(num1)
                convstr1 = int(num1str[0])
                convstr2 = int(num1str[1])
                num1 = convstr1 + convstr2
        
            FirstDigitSet.append(num1)
        
        
        Sum1 = accumulator(FirstDigitSet)
        Sum2 = accumulator(SecondDigitSet)
        result = Sum1 + Sum2

        pinVerified = cardPinVerification(cardPinUserEntry, pinList)

        actualCardNoValidity = cardNoValidation(result, pinVerified)

        actualCardOverallValidityState = cardOverallValidation(actualCardNoValidity, CardTypeUserEntry.capitalize(), RealCardBrandType.capitalize(), CardIndUserEntry[0:4].capitalize(), CardInd[0:4].capitalize(), CardIssuerNameUserEntry.capitalize(), RealCardIssuerName.capitalize(), CardIssuerLocationUserEntry.capitalize(), RealCardIssuerLocation.capitalize(), pinVerified)


#The Output Color Definition
   
        if ((actualCardNoValidity == "This Credit Card No and the pin is Valid") or (actualCardNoValidity == "This Credit Card No is Valid but the pin is Invalid") or (actualCardNoValidity == "This Credit Card No is Valid but the pin is not given")):
            CardNoOutputColor = '#09c3c3'
        else:
            CardNoOutputColor = '#ff0000'

        if (CardTypeUserEntry.capitalize() == RealCardBrandType.capitalize()):
            RealCardBrandTypeColor = '#09c3c3'
        else:
            RealCardBrandTypeColor = '#ff0000'

        if (CardInd[0:4].capitalize() == CardIndUserEntry[0:4].capitalize()):
            CardIndColor = '#09c3c3'
        else:
            CardIndColor = '#ff0000'

        if (RealCardIssuerName.capitalize() == CardIssuerNameUserEntry.capitalize()):
            RealCardIssuerNameColor = '#09c3c3'
        else:
            RealCardIssuerNameColor = '#ff0000'

        if (RealCardIssuerLocation.capitalize() == CardIssuerLocationUserEntry.capitalize()):
            RealCardIssuerLocationColor = '#09c3c3'
        else:
            RealCardIssuerLocationColor = '#ff0000'

        if ((actualCardNoValidity == "This Credit Card No and the pin is Valid") or (actualCardNoValidity == "This Credit Card No is Valid but the pin is not given")):
            actualCardNoValidityColor = '#09c3c3'
        elif (actualCardNoValidity == "This Credit Card No is Valid but the pin is Invalid"):
            actualCardNoValidityColor = '#FFFF00'
        else:
            actualCardNoValidityColor = '#ff0000'

        if (actualCardOverallValidityState == "This Card's Overall Details look good from here"):
            actualCardOverallValidityStateColor = '#09c3c3'
        elif (actualCardOverallValidityState == "This Card's No is Valid but other Details of the card are inconsistence" or actualCardOverallValidityState == "This Card's No is Invalid but other Details of the card are Valid"):
            actualCardOverallValidityStateColor = '#FFFF00'        
        else:
            actualCardOverallValidityStateColor = '#ff0000'



        window2 = Tk() 
        window2.title('YCT FINAL YEAR PROJECT - Development of Credit Card Prevention & Detection System Using Luhn Algorithm')
        window2.geometry('1000x900')
        window2.configure(background='#ffffff')
        window2.columnconfigure(0, weight=1) # make the column 1 expand when the window is resized

        heading1 = Label(window2, text = 'Credit Card Prevention and Detection System Result', font=("sans serif", 20), bg='#ee44ee', fg='#ffffff')
        heading1.grid(row=0, column=0, sticky='EW', columnspan=colspan, ipady=6) # sticky='ew' expands the label horizontally

#The input fields
        fields = ['Credit Card Number', 'Card Type', 'Card Industry', 'Card Issuer Name', 'Card Issuer Location (Country)']

      #The input fields
        usersinput = [CardNo, CardTypeUserEntry.capitalize(), CardIndUserEntry.capitalize(), CardIssuerNameUserEntry.capitalize(), CardIssuerLocationUserEntry.capitalize()]

#The input fields
        outputColors = [CardNoOutputColor, RealCardBrandTypeColor, CardIndColor, RealCardIssuerNameColor, RealCardIssuerLocationColor]

#The input fields
        databaseinput = [str(CardNo), str(RealCardBrandType).capitalize(), str(CardInd).capitalize(), str(RealCardIssuerName).capitalize(), str(RealCardIssuerLocation).capitalize()]

        formWindow = LabelFrame(window2, text = 'Credit Card Prevention and Detection System Result', bg='#faddfa', fg='#ee44ee', font=("san serif", 14), pady=30)
        formWindow.grid(row=2, column=0, sticky='WE', columnspan=colspan, ipady=2, ipadx=0)

        fieldcolumn1 = Label(formWindow, text = 'DESCRIPTION', font=('san serif', 14), bg='#d7d6d6', pady=1, padx=0, relief='raised') 
        fieldcolumn1.grid(row= 0, column=0, sticky='W', columnspan=colspan, ipady=10, ipadx=40, pady=10, padx=70)

        fieldcolumn2 = Label(formWindow, text = 'USER INPUT', font=('san serif', 14), bg='#d7d6d6', pady=1, padx=25, relief='raised')
        fieldcolumn2.grid(row= 0, column=1, columnspan=colspan, ipady=10, ipadx=30, pady=10, padx=100)

        fieldcolumn3 = Label(formWindow, text = 'REAL DETAILS', font=('Ariel', 14), bg='#d7d6d6', pady=1, padx=35, relief='raised')
        fieldcolumn3.grid(row= 0, column=2, sticky='E', columnspan=colspan, ipady=10, ipadx=20, pady=10, padx=90)

#Dry Code

        for pos in range(len(fields)):
        
            label = Label(formWindow, text = fields[pos], font=("sans serif", 11), bg='#faddfa', fg='#ee44ee', pady=1, padx=0)
            label.grid(row= pos+1, column=0, sticky='W', columnspan=colspan, ipady=7, ipadx=0, pady=10, padx=70)

            label = Label(formWindow, text = usersinput[pos], font=('Ariel', 11), bg='#fafafa', fg=outputColors[pos], pady=1, padx=0)
            label.grid(row= pos+1, column=1, columnspan=colspan, ipady=7, ipadx=10, pady=10, padx=80)

            label = Label(formWindow, text = databaseinput[pos], font=('Ariel', 11), bg='#fafafa', fg=outputColors[pos], pady=1, padx=45)
            label.grid(row= pos+1, column=2, columnspan=colspan, ipady=7, ipadx=10, pady=10, padx=120)

        Valid1 = Label(formWindow, text = 'Credit Card No and Pin Validity', bg='#d7d6d6', font=('Ariel', 12), pady=1, padx=0, relief='raised') 
        Valid1.grid(row= 6, column=0, sticky='W', columnspan=colspan, ipady=7, ipadx=0, pady=10, padx=70)

        Valid2 = Label(formWindow, text = '', bg='#faddfa', pady=1, padx=10)
        Valid2.grid(row= 6, column=1, columnspan=colspan, ipady=7, ipadx=30, pady=10, padx=70)

        Valid3 = Label(formWindow, text = actualCardNoValidity, font=('Ariel', 12), bg='#fafafa', fg=actualCardNoValidityColor, pady=1, padx=30)
        Valid3.grid(row= 6, column=2, sticky='E', columnspan=colspan, ipady=7, ipadx=20, pady=10, padx=50)

        Valid4 = Label(formWindow, text = 'Credit Card Overall Details Validity', bg='#d7d6d6', font=('Ariel', 12), pady=1, padx=0, relief='raised') 
        Valid4.grid(row= 7, column=0, sticky='W', columnspan=colspan, ipady=7, ipadx=0, pady=10, padx=70)

        Valid5 = Label(formWindow, text = '', bg='#faddfa', pady=1, padx=10)
        Valid5.grid(row= 7, column=1, columnspan=colspan, ipady=7, ipadx=30, pady=10, padx=70)

        Valid6 = Label(formWindow, text = actualCardOverallValidityState, font=('Ariel', 12), bg='#ffffff', fg=actualCardOverallValidityStateColor, pady=1, padx=30)
        Valid6.grid(row= 7, column=2, sticky='E', columnspan=colspan, ipady=7, ipadx=20, pady=10, padx=50)

        label = Label(window2, text ='@Copyright.\t\t\t \t\t\t\tDepartment: Computer Science', font=('Ariel', 10), bg='#ffffff', fg='#000000', pady=1, padx=20)
        label.grid(row=8, column=0, sticky='WE', columnspan=colspan, ipady=0, ipadx=40, pady=0, padx=10)

    
        window2.mainloop()
    except:
        #messagebox.showerror('Error Message', 'Invalid input')
        messagebox.showerror('Error Message', 'Invalid input:  Check your Card Details OR Refer to the User manual for valid inputs into the entries;\n THEN TRY AGAIN!!')
##205584
                
heading1 = Label(window, text = 'Credit Card Pevention and Detection System', font=("sans serif", 20), bg='#ee44ee', fg='#ffffff')
heading1.grid(row=0, column=0, sticky='EW', columnspan=colspan, ipady=3) # sticky='ew' expands the label horizontally

heading2 = Label(window, text = 'Welcome To CCPDS\n Enter the Credit Card Details Below', font=("sans serif", 20), bg='#ff77ff', fg='#ffffff')
heading2.grid(row=1, column=0, sticky='EW', columnspan=colspan, ipady=6) # sticky='ew' expands the label horizontally

formWindow = LabelFrame(window, text = 'Credit Card Entry Field', bg='#ffffff', fg='#ee44ee', font=("Georgia", 14), pady=27)
formWindow.grid(row=2, column=0, sticky='WE', columnspan=colspan, ipady=2, ipadx=10)

# The entries and labels

labelCardno = Label(formWindow, text = 'Credit Card Number', font=labelfonts, pady=labelpady, padx=labelpadx, bg='#ffffff', fg='#000000')
labelCardno.grid(row=1, column=labelcol, sticky=labelsticky, columnspan=colspan, ipady=labelgridipady, ipadx=labelgridipadx, pady=labelgridpady, padx=labelgridpadx)

cardNoVar = Entry(formWindow, bd=entrybd, font=entryfonts, width=entrywidth)
cardNoVar.grid(row=1, column=entrycol, sticky=entrysticky, columnspan=colspan, ipady=entrygridipady, ipadx=entrygridipadx, pady=entrygridpady, padx=entrygridpadx)


labelCardType = Label(formWindow, text = 'Card Type', font=labelfonts, pady=labelpady, padx=labelpadx, bg='#ffffff', fg='#000000')
labelCardType.grid(row=2, column=labelcol, sticky=labelsticky, columnspan=colspan, ipady=labelgridipady, ipadx=labelgridipadx, pady=labelgridpady, padx=labelgridpadx)

cardTypeVar = Entry(formWindow, bd=entrybd, font=entryfonts, width=entrywidth)
cardTypeVar.grid(row=2, column=entrycol, sticky=entrysticky, columnspan=colspan, ipady=entrygridipady, ipadx=entrygridipadx, pady=entrygridpady, padx=entrygridpadx)


labelCardInd = Label(formWindow, text = 'Card Industry', font=labelfonts, pady=labelpady, padx=labelpadx, bg='#ffffff', fg='#000000')
labelCardInd.grid(row=3, column=labelcol, sticky=labelsticky, columnspan=colspan, ipady=labelgridipady, ipadx=labelgridipadx, pady=labelgridpady, padx=labelgridpadx)

cardIndVar = Entry(formWindow, bd=entrybd, font=entryfonts, width=entrywidth)
cardIndVar.grid(row=3, column=entrycol, sticky=entrysticky, columnspan=colspan, ipady=entrygridipady, ipadx=entrygridipadx, pady=entrygridpady, padx=entrygridpadx)


labelCardIH = Label(formWindow, text = 'Card Issuer Name', font=labelfonts, pady=labelpady, padx=labelpadx, bg='#ffffff', fg='#000000')
labelCardIH.grid(row=4, column=labelcol, sticky=labelsticky, columnspan=colspan, ipady=labelgridipady, ipadx=labelgridipadx, pady=labelgridpady, padx=labelgridpadx)

cardIssuerNameVar = Entry(formWindow, bd=entrybd, font=entryfonts, width=entrywidth)
cardIssuerNameVar.grid(row=4, column=entrycol, sticky=entrysticky, columnspan=colspan, ipady=entrygridipady, ipadx=entrygridipadx, pady=entrygridpady, padx=entrygridpadx)


labelCardIHL = Label(formWindow, text = 'Card Issuer Location (Country)', font=labelfonts, pady=labelpady, padx=labelpadx, bg='#ffffff', fg='#000000')
labelCardIHL.grid(row=5, column=labelcol, sticky=labelsticky, columnspan=colspan, ipady=labelgridipady, ipadx=labelgridipadx, pady=labelgridpady, padx=labelgridpadx)

cardIssuerLocationVar = Entry(formWindow, bd=entrybd, font=entryfonts, width=entrywidth)
cardIssuerLocationVar.grid(row=5, column=entrycol, sticky=entrysticky, columnspan=colspan, ipady=entrygridipady, ipadx=entrygridipadx, pady=entrygridpady, padx=entrygridpadx)


labelCCV = Label(formWindow, text = 'CVC Number', font=labelfonts, pady=labelpady, padx=labelpadx, bg='#ffffff', fg='#000000')
labelCCV.grid(row=6, column=labelcol, sticky=labelsticky, columnspan=colspan, ipady=labelgridipady, ipadx=labelgridipadx, pady=labelgridpady, padx=labelgridpadx)

input = Entry(formWindow, bd=entrybd, font=entryfonts, width=entrywidth)
input.grid(row=6, column=entrycol, sticky=entrysticky, columnspan=colspan, ipady=entrygridipady, ipadx=entrygridipadx, pady=entrygridpady, padx=entrygridpadx)

labelPin = Label(formWindow, text = 'Pin Number', font=labelfonts, pady=labelpady, padx=labelpadx, bg='#ffffff', fg='#000000')
labelPin.grid(row=7, column=labelcol, sticky=labelsticky, columnspan=colspan, ipady=labelgridipady, ipadx=labelgridipadx, pady=labelgridpady, padx=labelgridpadx)

cardPinVar = Entry(formWindow, bd=entrybd, font=entryfonts, width=entrywidth)
cardPinVar.grid(row=7, column=entrycol, sticky=entrysticky, columnspan=colspan, ipady=entrygridipady, ipadx=entrygridipadx, pady=entrygridpady, padx=entrygridpadx)

    
# The Validation button
validationbutton = Button(formWindow, command = CardValidator, height="1", width="15", bd='0', bg='#ee44ee', fg='#ffffff', text='Validate', font=('sans serif', 16))
validationbutton.grid(row=8, column=1, pady=8, padx=360)

label = Label(formWindow, text ='@Copyright.\t\t\t \t\t\t\tDepartment: Computer Science', font=('Ariel', 10), bg='#ffffff', fg='#000000', pady=1, padx=20)
label.grid(row=9, column=labelcol, sticky='WE', columnspan=colspan, ipady=1, ipadx=0, pady=0, padx=10)



window.mainloop()

