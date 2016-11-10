# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT) #Rood lichtje output
GPIO.setup(11, GPIO.OUT) #Geel lichtje output
GPIO.setup(22, GPIO.OUT) #Groen lichtje output
GPIO.setup(13, GPIO.IN) #Knop 1 input
GPIO.setup(18, GPIO.IN) #Knop 2 input

ingedrukt = 0; #Om te checken of het alarmknopje is ingedrukt
knipperen = 0; #Om te checken of het lichtje aan het knipperen is
gelockt = 0; #Om te checken of ze eruit gelockt zijn
knipperSnelheid = 0.5; #Om het knippersnelheid te regelen


while True:
        if(GPIO.input(13) == GPIO.HIGH):# Als het eerste knopje wordt ingedrukt
                GPIO.output(22, GPIO.LOW); # Zet het groen lichtje uit (Om zeker te weten dat het groen lichtje uitstaat wanneer het alarm aan staat)
                knipperen = 1; # Zet knipperen naar 1
                ingedrukt = 1; # Zet ingedrukt naar 1
        if(knipperen == 1): # Omdat dit in een while loop zit zal het lichtje dus knipperen
                GPIO.output(12, GPIO.HIGH) # Zet het rood lichtje aan
                time.sleep(knipperSnelheid); # Wacht voor hoe lang knippersnelheid staat (0.5 eerst)
                GPIO.output(12, GPIO.LOW) # Zet het lichtje uit
                time.sleep(knipperSnelheid); # Wacht weer voor hoe lang knippersnelheid staat
        if(GPIO.input(18) == GPIO.HIGH and ingedrukt == 1 and gelockt == 0): # Als het 2de knopje wordt ingedrukt terwijl het alarm aan staat en de persoon niet eruit gelockt is
                GPIO.output(11, GPIO.HIGH); # Zet het gele lichtje aan
                a = input("Gebruikersnaam: ") # Vraag om een gebruikersnaam
                b = input("Wachtwoord: ") # Vraag om een wachtwoord
                if(a == "test1" and b == "test2"): # Als A en B test1 en test2 zijn
                    GPIO.output(11, GPIO.LOW); # Zet het gele lichtje uit
                    GPIO.output(22, GPIO.HIGH); # Zet het groene lichtje aan
                    print("Het alarm is uitgezet"); # Zeg dat het alarm is uitgezet
                    global knipperSnelheid;
                    knipperSnelheid = 0.5; # Verander knippersnelheid terug naar 0.5 om alles te resetten
                    ingedrukt = 0; # Verander ingedrukt naar 0
                    knipperen = 0; # Verander knipperen naar 0 zodat het rood lichtje niet meer knippert
                else: # Als het gebruikersnaam en wachtwoord verkeerd zijn
                    GPIO.output(11, GPIO.LOW); # Zet het gele lichtje uit
                    if(knipperSnelheid > 0.3): # Als knippersnelheid hoger dan 0.3 is
                            print("Verkeerde inlogcombinatie"); # Print verkeerde inlogcombinatie
                            global knipperSnelheid
                            knipperSnelheid -= 0.1; # Laat het lichtje sneller knipperen
                    else: # Als knippersnelheid niet meer hoger dan 0.3 is
                            print("de politie is gebeld, teveel foutieve pogingen"); # Vertel dat de politie is gebeld vanwege teveel foutive pogingen
                            gelockt = 1; # De persoon wordt eruit gelockt
                            continue; # Ga door met knipperen

GPIO.cleanup() #Als we ooit uit de loop gaan stopt dit het GPIO programma

