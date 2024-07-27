import os
import subprocess
import sys
import time
import pygame
import ctypes
import webbrowser
import colorama
import threading
import fade
from pygame import mixer
from colorama import Fore, init
from pystyle import Center, Write, Colors, Colorate

os.system('cls')

os.system("mode 140,30")

init()

os.system('cls')




ctypes.windll.kernel32.SetConsoleTitleW("Spotify-Tool By PineDragon")




text = """ 
                                 ▄████████    ▄███████▄  ▄██████▄      ███      ▄█     ▄████████ ▄██   ▄   
                                ███    ███   ███    ███ ███    ███ ▀█████████▄ ███    ███    ███ ███   ██▄ 
                                ███    █▀    ███    ███ ███    ███    ▀███▀▀██ ███▌   ███    █▀  ███▄▄▄███ 
                                ███          ███    ███ ███    ███     ███   ▀ ███▌  ▄███▄▄▄     ▀▀▀▀▀▀███ 
                              ▀███████████ ▀█████████▀  ███    ███     ███     ███▌ ▀▀███▀▀▀     ▄██   ███ 
                                       ███   ███        ███    ███     ███     ███    ███        ███   ███ 
                                 ▄█    ███   ███        ███    ███     ███     ███    ███        ███   ███ 
                               ▄████████▀   ▄████▀       ▀██████▀     ▄████▀   █▀     ███         ▀█████▀  
                                                                                                                         
                                                                  Stop
               
                                 Batman                        Novocaine                     HDMI
                                 Bean                          Sodium                        Did It Again
                                 20 Min                        Matte Black                   Down With Me
                                 Miss The Rage                 Pass Out                      Space Cadet
                                 Gee Willikers                 Lot of me                     500lbs
                                 505                           Hex                           Your My Friend
                                 The Color Violet              Ransom                        Off The Leash
                                 Not Available                 For Fun                       Touchable
                                 Limbo                         Holocaust                     Gang Unit
                                 Alien Blues                   Notion                        Beckham
                                 The Grinch                    Left Right                    Roxxane
                                 Walk                          Placeholder                   without me
    """
faded_text = fade.greenblue(text)
print(faded_text)




while True:
    user_input = Write.Input("#Music-Player -?", Colors.green_to_white, interval=0.03)
    user_input = user_input.lower()
    

    if user_input == "batman":
        mixer.init()
        mixer.music.load('Music/batman.mp3')
        mixer.music.play()
    if user_input == "stop":
        mixer.init()
        mixer.music.load('Music/Nothing.mp3')
        mixer.music.play()
    if user_input == "bean":
        mixer.init()
        mixer.music.load('Music/Bean.mp3')
        mixer.music.play()
    if user_input == "gee willikers":
        mixer.init()
        mixer.music.load('Music/GeeWillikers.mp3')
        mixer.music.play()
    if user_input == "20 min":
        mixer.init()
        mixer.music.load('Music/20min.mp3')
        mixer.music.play()
    if user_input == "miss the rage":
        mixer.init()
        mixer.music.load('Music/misstherage.mp3')
        mixer.music.play()
    if user_input == "505":
        mixer.init()
        mixer.music.load('Music/505.mp3')
        mixer.music.play()
    if user_input == "money":
        mixer.init()
        mixer.music.load('Music/money.mp3')
        mixer.music.play()
    if user_input == "the color violet":
        mixer.init()
        mixer.music.load('Music/The Color Violet.mp3')
        mixer.music.play()
    if user_input == "not available":
        mixer.init()
        mixer.music.load('Music/NOT AVAILABLE.mp3')
        mixer.music.play()
    if user_input == "limbo":
        mixer.init()
        mixer.music.load('Music/Limbo.mp3')
        mixer.music.play()
    if user_input == "alien blues":
        mixer.init()
        mixer.music.load('Music/AlienBlues.mp3')
        mixer.music.play()
    if user_input == "novocaine":
        mixer.init()
        mixer.music.load('Music/Novocaine.mp3')
        mixer.music.play()
    if user_input == "sodium":
        mixer.init()
        mixer.music.load('Music/Sodium.mp3')
        mixer.music.play()
    if user_input == "matte black":
        mixer.init()
        mixer.music.load('Music/MATTE BLACK.mp3')
        mixer.music.play()
    if user_input == "pass out":
        mixer.init()
        mixer.music.load('Music/Pass Out.mp3')
        mixer.music.play()
    if user_input == "lot of me":
        mixer.init()
        mixer.music.load('Music/Lot of me.mp3')
        mixer.music.play()
    if user_input == "hex":
        mixer.init()
        mixer.music.load('Music/Hex.mp3')
        mixer.music.play()
    if user_input == "ransom":
        mixer.init()
        mixer.music.load('Music/Ransom.mp3')
        mixer.music.play()
    if user_input == "for fun":
        mixer.init()
        mixer.music.load('Music/For Fun.mp3')
        mixer.music.play()
    if user_input == "holocaust":
        mixer.init()
        mixer.music.load('Music/HOLOCAUST.mp3')
        mixer.music.play()
    if user_input == "notion":
        mixer.init()
        mixer.music.load('Music/notion.mp3')
        mixer.music.play()
    if user_input == "novocaine":
        mixer.init()
        mixer.music.load('Music/Novocaine.mp3')
        mixer.music.play()
    if user_input == "hdmi":
        mixer.init()
        mixer.music.load('Music/HDMI.mp3')
        mixer.music.play()
    if user_input == "left right":
        mixer.init()
        mixer.music.load('Music/LEFT RIGHT.mp3')
        mixer.music.play()
    if user_input == "did it again":
        mixer.init()
        mixer.music.load('Music/Did It Again.mp3')
        mixer.music.play()
    if user_input == "down with me":
        mixer.init()
        mixer.music.load('Music/Down With Me.mp3')
        mixer.music.play()
    if user_input == "space cadet":
        mixer.init()
        mixer.music.load('Music/Space Cadet.mp3')
        mixer.music.play()
    if user_input == "500lbs":
        mixer.init()
        mixer.music.load('Music/500lbs.mp3')
        mixer.music.play()
    if user_input == "your my friend":
        mixer.init()
        mixer.music.load('Music/Your My Friend.mp3')
        mixer.music.play()
    if user_input == "off the leash":
        mixer.init()
        mixer.music.load('Music/Off The Leash.mp3')
        mixer.music.play()
    if user_input == "touchable":
        mixer.init()
        mixer.music.load('Music/Touchable.mp3')
        mixer.music.play()
    if user_input == "gang unit":
        mixer.init()
        mixer.music.load('Music/Gang Unit.mp3')
        mixer.music.play()
    if user_input == "roxxane":
        mixer.init()
        mixer.music.load('Music/ROXANNE.mp3')
        mixer.music.play()
    if user_input == "beckham":
        mixer.init()
        mixer.music.load('Music/Beckham.mp3')
        mixer.music.play()
    if user_input == "walk":
        mixer.init()
        mixer.music.load('Music/I MUST WALK.mp3')
        mixer.music.play()
    if user_input == "the grinch":
        mixer.init()
        mixer.music.load('Music/The Grinch.mp3')
        mixer.music.play()
    if user_input == "without me":
        mixer.init()
        mixer.music.load('Music/Without Me.mp3')
        mixer.music.play()