# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT) #Rood lichtje output
GPIO.setup(11, GPIO.OUT) #Geel lichtje output
GPIO.setup(22, GPIO.OUT) #Groen lichtje output
GPIO.setup(13, GPIO.IN) #Knop 1 input
GPIO.setup(18, GPIO.IN) #Knop 2 input

ingedrukt = 0;
knipperen = 0;
knipperSnelheid = 0.5;


while True:
        if(GPIO.input(13) == GPIO.HIGH):
                GPIO.output(22, GPIO.LOW);
                knipperen = 1;
                ingedrukt = 1;
        if(knipperen == 1):
                GPIO.output(12, GPIO.HIGH)
                time.sleep(knipperSnelheid);
                GPIO.output(12, GPIO.LOW)
                time.sleep(knipperSnelheid);
        if(GPIO.input(18) == GPIO.HIGH and ingedrukt == 1):
                GPIO.output(11, GPIO.HIGH);
                a = input("Gebruikersnaam: ")
                b = input("Wachtwoord: ")
                if(a == "test1" and b == "test2"):
                    GPIO.output(11, GPIO.LOW);
                    GPIO.output(22, GPIO.HIGH);
                    print("Het alarm is uitgezet");
                    global knipperSnelheid;
                    knipperSnelheid = 0.5;
                    ingedrukt = 0;
                    knipperen = 0;
                else:
                    GPIO.output(11, GPIO.LOW);
                    if(knipperSnelheid > 0.3):
                            print("Verkeerde inlogcombinatie");
                            global knipperSnelheid
                            knipperSnelheid -= 0.1;
                    else:
                            print("de politie is gebeld, teveel foutieve pogingen");
                            continue;

GPIO.cleanup()

