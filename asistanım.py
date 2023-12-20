from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time #hangi günde olduğumuzu söylemesi için import ettik
from datetime import datetime #sitemden saati almak için import ettik
import random
from random import choice
from pydub import AudioSegment
import webbrowser #asiatana internetten bir şey aratmak için kullanıyoruz.


def speak(string):
    a = gTTS(text= string, lang = "tr",slow=False) #google a bağlanmamızı sağlayan köprü
    file = "answer.mp3"
    a.save(file) #yukarıda gönderilen sesi kaydeder
    speeding()
    playsound('speed.mp3') #çalar
    os.remove(file) #bilgisayarda yer kaplamayıp önceki sesi siliyor
    os.remove("speed.mp3")

def record(ask = False):
    with sr.Microphone() as source: #sesi hangi kaynaktan alacağını belirledik
        if ask:
            print(ask)
        audio = r.listen(source) #sesi dinliyor.
        voice ="" #sesi boş bir değere atıyor
        try:
            voice = r.recognize_google(audio, language = "tr-TR")
            #googleda karşılığını bulursa boş olan ses değişkenine söylediğimiz şeyi atıyor.
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım")
        except sr.RequestError: #İnternet bağlantısı ile ilgili sorun varsa
            print("Asistan: Ses çalışmıyor.")
        return voice

def speed_swifter(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    return sound_with_altered_frame_rate
def speeding():
    in_path = 'answer.mp3'
    ex_path = 'speed.mp3'
    sound = AudioSegment.from_file(in_path)
    slower_sound = speed_swifter(sound, 1.2)
    slower_sound.export(ex_path, format="mp3")


def response(voice):
    if "ismin ne" in voice:
        speak("ismim charlie")
    if "kaç yaşındasın" in voice:
        speak("herhangi bir yaşım yok.")
    if "nerelisin" in voice:
        speak("ankara")
    if "cinsiyetin ne" in voice:
        speak("bir cinsiyetim yok.")
    if "senin üreticin kim" in voice:
        speak("benim üreticim zeynep")
    if "ne yapmalıyım" in voice:
        speak("bol bol gülümsemeyi unutma")
    if "nasılsın" in voice:
        speak("iyiyim sen nasılsın")
    if "bana bir fıkra anlatır mısın" in voice:
        selection = ["bir gün temel çift görüyormuş, dursun’da tek gözünü kapatsana, demiş.","temel aldığı bir daktiloyu bozuk diye geri götürdü. satıcı demişki neresi bozuk, dün aldığında sağlamdı.  temel demişki iki tane a yok, saat yazamıyorum"]
        selection = random.choice(selection)
        speak(selection)

    if "selam" in voice:
        speak("selam")
    if "merhaba" in voice:
        speak("merhaba")
    if "teşekkür ederim" in voice:
        speak("rica ederim")
    if "nasıl görünüyorum" in voice:
        speak("efsanesin")
    if "nasılsın" in voice:
        speak("iyiyim sen nasılsın")
    if "iyiyim" in voice:
        speak("iyi olmana sevindim")
    if "kötüyüm" in voice:
        speak("bunu duyduğuma üzüldüm")
    if "hangi gün" in voice:
        today = time.strftime("%A")
        if today=="Monday":
            today = "Pazartesi"
        elif today=="Tuesday":
            today="Salı"
        elif today=="Wednesday":
            today="Çarşamba"
        elif today == "Thursday":
            today = "Perşembe"
        elif today=="Friday":
            today = "Cuma"
        elif today == "Saturday":
            today = "Cumartesi"
        elif today== "Sunday":
            today= "Pazar"
        print(today)
        speak(today)
    if "saat kaç" in voice:
        selection = ["saat şuan" , "hemen bakıyorum"] #her zaman aynı şeyi söylememesini sağlıyoruz
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selection)
        speak(selection + clock)
    if "araştırma" in voice:
        speak("ne aratmamı istersin")
        search = record()  # söylediğimiz şeyi tutar.
        url = "https://www.google.com.tr/search?q=" + search
        webbrowser.get().open(url)
        speak(search + "için google da bulabildiklerimi gösteriyorum:")
    if "not et" in voice:
        speak("dosya ismi ne olsun")
        txtFile = record() + ".txt"
        speak("ne kaydetmek istiyorsun")
        f = open(txtFile, "w")
        theText = record()
        f.writelines(theText)
        f.close()
    if "görüşürüz" in voice:
        speak("görüşürüz")
        exit() #görüşürüz dedikten sonra program kendini kapattı.
speak("merhaba Zeynep") #üstte tanımladığımız fonksiyonu çağırdık
r =sr.Recognizer() #ses tanıma motorunu değişene atadık
while True: #sistemin kapanmayıp sürekli bizi dinlemesi için yazdık
    voice = record()
    if voice != "":
        voice = voice.lower()  # Ekrana yazdırırken baş harfi büyük yazdırıyordu.Onu ortadan kaldırdık.
        response(voice)








