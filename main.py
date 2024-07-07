import asyncio
from asyncio import WindowsSelectorEventLoopPolicy

asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

import os
import pygame
import pyautogui
import pywhatkit
import speech_recognition as sr
import pyjokes
import webbrowser
import wikipedia
import time
import cv2
import requests
#from bot_scrapper import *
from datetime import datetime
from gpt4_free import GPT
from emailsender import send_email

def speak(text):
    voice = "en-US-EricNeural"
    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "output.mp3"'
    os.system(command)
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)

    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

def greeting():
    current_time = datetime.now()
    hour = current_time.hour
    if 3 <= hour < 12:
        speak('Hello! Good morning. I am VICKY. How can I help you today.')
    elif 12 <= hour < 18:
        speak('Hello! Good afternoon. I am VICKY. How can I help you today.')
    else:
        speak('Hello! Good evening. I am VICKY. How can I help you today.')

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(f"You:{query}\n")
        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return query

sleep_mode = False
greeting()

#click_on_chat_button()
while True:
    query = take_command().lower()

    if 'open gmail' in query:
        webbrowser.open_new_tab("https://www.gmail.com")
        speak("Gmail open now")
        time.sleep(5)

    elif 'open' in query:
        app_name = query.replace('open', '')
        speak('opening' + app_name)
        pyautogui.press('super')
        pyautogui.typewrite(app_name)
        pyautogui.sleep(0.7)
        pyautogui.press('enter')

    elif 'switch tab' in query:
        pyautogui.hotkey('alt', 'tab')
        speak("Tab switched")

    elif 'close tab' in query:
        pyautogui.hotkey('ctrl', 'w')
        speak("Tab closed")

    elif 'close' in query:
        pyautogui.hotkey('alt', 'f4')
        speak("It's done")

    elif 'joke' in query:
        speak(pyjokes.get_joke())

    elif 'play' in query:
        song_name = query.replace('play', '')
        speak('Sure. Playing' + song_name + ' on youtube')
        pywhatkit.playonyt(song_name)

    elif "pause" in query or "continue" in query or "stop" in query or "start" in query:
        pyautogui.press('k')
        speak("It's done")

    elif "full screen" in query:
        pyautogui.press('f')
        speak("It's done")

    elif "theater mode" in query or "theater screen" in query:
        pyautogui.press('t')
        speak("It's done")

    elif 'time' in query:
        time = datetime.now().strftime('%H:%M %p')
        print(time)
        speak('Current time is ' + time)

    elif 'date' in query:
        date = datetime.now().strftime('%d/%m/%y')
        print(date)
        speak("Today's date is " + date)

    elif 'sleep' in query:
        speak("ok sir. I am going to sleep, but, you can just say 'hey vicky' and I will be there for you.")
        sleep_mode = True

    elif 'shutdown' in query:
        speak('shutting down the pc in')
        speak('3. 2. 1')
        os.system("shutdown /r /t 1")

    elif 'restart' in query:
        speak('restarting the pc in')
        speak('3. 2. 1')
        os.system("restart /r /t 1")

    elif 'who are you' in query or 'what can you do' in query or 'what are you' in query:
        speak('I am VICKY, an ai-powered personal assistant, built by S Amith Vikram. I am programmed to minor tasks '
              'like opening youtube, google chrome & gmail, telling a joke, predicting time and date, generate code '
              'snippets for any language, write an essay, send an email, predict weather in different cities, '
              'get top headline news from times of india, taking screenshots, capturing photos from your webcam.')

    elif "who made you" in query or "who created you" in query or "who built you" in query:
        speak("I was developed by S Amith Vikram in the year 2024. He was a student pursuing his final semester in "
              "the Computer Science and Engineering - Master of Computer Applications program at an Autonomous "
              "Engineering College called Jawaharlal Nehru Technological University Anantapur. His enrollment number"
              "for this project was 22001F0027.")

    elif 'code' in query or 'program' in query or 'source code' in query:
        speak('Sure, give me the complete prompt')
        prompt = take_command()
        code = GPT(prompt)
        if code:
            with open('program.txt', 'w') as file:
                file.write(code)
            speak('Code generated successfully and saved as program.txt in the current working directory')
        else:
            speak('Sorry, I encountered an error while generating the code.')


    elif 'essay' in query or 'short note' in query:
        speak('Sure, give the name of the topic and complete prompt')
        topic = take_command()
        essay = GPT(topic)
        if essay:
            with open('essay.doc', 'w', encoding='utf-8') as file:
                file.write(essay)
            speak('Text generated successfully and saved as essay.doc in the current working directory')
        else:
            speak('Sorry, I encountered an error while generating the essay.')

    elif 'write a letter' in query:
        speak('Sure, give me the prompt')
        subject = take_command()
        letter = GPT(subject)
        if letter:
            with open('letter.doc', 'w') as file:
                file.write(letter)
            speak('Text generated successfully and saved as letter.doc in the current working directory')
        else:
            speak('Sorry, I encountered an error while generating the essay.')

    elif 'compose an email' in query or 'send an email' in query:
        speak('Sure sir, can you provide me the name of the user to whom you want to send email below: ')
        receiver = input('Enter his/her email address: ')
        speak('What should be the subject of the email.')
        subject = take_command()
        speak('What should be the content. Just provide me some prompt')
        email_prompt = take_command()
        content = GPT('Write an email about ' + email_prompt)
        send_email(receiver, subject, content)
        speak(f'Done sir. Email sent successfully to {receiver}')

    elif 'news' in query:
        news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        speak('Here are some headlines from the Times of India,Happy reading')
        time.sleep(6)

    elif "camera" in query or "take a photo" in query:
        camera_port = 0
        camera = cv2.VideoCapture(camera_port)
        time.sleep(1.0)
        return_value, image = camera.read()
        cv2.imwrite("capturedbyvicky.jpg", image)
        speak('Photo taken and saved in current working directory')
        del (camera)

    elif "screenshot" in query:
        image = pyautogui.screenshot()
        image.save('screenshotbyvicky.png')
        speak('Screenshot taken and saved in current working directory')

    elif "weather" in query or "temperature" in query:
        api_key = "3c5b006a580350c92b6b98faef74963c"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        speak("whats the city name")
        city_name = take_command()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x['main']
            current_temperature = y["temp"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            speak("Temperature is " + str(current_temperature) + " kelvin. " +
                  "Humidity is " + str(current_humidity) + " percentage. " +
                  "Weather description : " + str(weather_description))
        else:
            speak("City Not Found ")

    elif 'exit' in query or 'goodbye' in query:
        speak('have a nice day')
        exit()

    else:
        #sendQuery(query)
        #isBubbleLoaderVisible()
        #response = retriveData()
        #speak(response)
        res = GPT(query)
        speak(res)

    while sleep_mode:
        query = take_command().lower()
        print(query)
        if 'hey vicky' in query:
            speak('Hello, how can I help you')
            sleep_mode = False
