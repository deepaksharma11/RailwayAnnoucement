import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

# install pyaudio (install pipwin then install pyaudio using pipwin)
# install pydub (used to breaking an audio into small segments)
# install ffmpeg (download it in windows format using browser then put files somewhere in c drive and then set the path in envirnoment variable)
# install gTTS (used for text to speech function)

def textToSpeech(text,  filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang = language, slow = False)
    myobj.save(filename)

def textToSpeechEng(text, filename):
    mytext = str(text)
    language = 'en'
    myobj = gTTS(text=mytext, lang = language, slow = False)
    myobj.save(filename)

def mergeAudios(audios):
    '''this fuunction returns pydubs audio segment'''
    combined = AudioSegment.empty()
    for audion in audios:
        combined += AudioSegment.from_mp3(audion)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('Ex_Railway\\railway.mp3')
    # 1 - Generate Kripya Dhyan Dijiye
    start = 88000 # seconds * 1000 = miliseconds
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("Ex_Railway\\1_hindi.mp3", format = "mp3")

    # 2 is from city

    # 3 - Generate se chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("Ex_Railway\\3_hindi.mp3", format="mp3")

    # 4 is via-city

    # 5 - Generate ke raaste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("Ex_Railway\\5_hindi.mp3", format="mp3")

    # 6 is to-city

    # 7 - Generate ko jaane wali gaadi sakhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("Ex_Railway\\7_hindi.mp3", format="mp3")

    # 8 is train no and name

    # 9 - Generate kuch hi samay mei platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("Ex_Railway\\9_hindi.mp3", format="mp3")

    # 10 is platform number

    # 11 - Generate par aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("Ex_Railway\\11_hindi.mp3", format="mp3")

def generateSkeletonEng():
    audio = AudioSegment.from_mp3('Ex_Railway\\railwayeng.mp3')

    #1 - Generate Kripya Dhyan Dijiye
    start = 88000 # seconds * 1000 = miliseconds
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("Ex_Railway\\1_eng.mp3", format = "mp3")

    #2 is from city

    # 3 - Generate se chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("Ex_Railway\\3_eng.mp3", format="mp3")

    # 4 is via-city

    # 5 - Generate ke raaste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("Ex_Railway\\5_eng.mp3", format="mp3")

    # 6 is to-city

    # 7 - Generate ko jaane wali gaadi sakhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("Ex_Railway\\7_eng.mp3", format="mp3")

    # 8 is train no and name

    # 9 - Generate kuch hi samay mei platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("Ex_Railway\\9_eng.mp3", format="mp3")

    # 10 is platform number

    # 11 - Generate par aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("Ex_Railway\\11_eng.mp3", format="mp3")

def generateAnnouncment(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # generate 2 is From City
        textToSpeech(item["from"], 'Ex_Railway\\2_hindi.mp3')
        textToSpeechEng(item["from"], 'Ex_Railway\\2_eng.mp3')
        # generate 4 is via-city
        textToSpeech(item["via"], 'Ex_Railway\\4_hindi.mp3')
        textToSpeechEng(item["via"], 'Ex_Railway\\4_eng.mp3')
        # generate 6 is to-city
        textToSpeech(item["to"], 'Ex_Railway\\6_hindi.mp3')
        textToSpeechEng(item["to"], 'Ex_Railway\\6_eng.mp3')
        # generate 8 is train no and name
        textToSpeech(item["train_no"] + " " + item["train_name"], 'Ex_Railway\\8_hindi.mp3')
        textToSpeechEng(item["train_no"] + " " + item["train_name"], 'Ex_Railway\\8_eng.mp3')
        # generate 10 is platform number 
        textToSpeech(item["platform"], 'Ex_Railway\\10_hindi.mp3')
        textToSpeechEng(item["platform"], 'Ex_Railway\\10_eng.mp3')

        audios = [f"Ex_Railway\\{i}_hindi.mp3" for i in range(1,12)]
        for i in range(1, 12):
            audios.append(f"Ex_Railway\\{i}_eng.mp3")
        announcement = mergeAudios(audios)
        announcement.export(f"Ex_Railway\\announcement_{item['train_no']}_{index+1}.mp3", format = "mp3")

if __name__ == "__main__":
    print("Generate Skeleton")
    generateSkeleton()
    generateSkeletonEng()
    print("Now Generating Announcement...")
    #file from where we will get information about the train 
    generateAnnouncment("Ex_Railway\\announce_hindi.xlsx")