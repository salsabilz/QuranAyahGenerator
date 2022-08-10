# Quran Ayah Generator

import requests
import random

# Fetch ayah function via Quran.com API
# https://quran.api-docs.io/v4/verses/by-specific-verse-by-key
def fetch_ayah(surah_no, ayah_no):
    url = "https://api.quran.com/api/v4/verses/by_key/"+str(surah_no)+":"+str(ayah_no)+"?language=en&words=true"

    response = requests.get(url)

    ayah_obj = response.json()
  
    ayah_arr = ayah_obj["verse"]["words"]

    ayah_translated = " ".join([str(words["translation"]["text"]) for words in ayah_arr])
  
    ayah_verse = ayah_obj["verse"]["verse_key"]

    return ayah_translated + ". [" + ayah_verse + "]"

# Input feeling
print("How are you feeling today?\n")
feeling = input("Do you feel JOY? Or do you feel SADNESS? \n [Write JOY or SAD]\n")

# Choose emotion
if feeling.lower() == "joy":
  joy_emotion = input("\nChoose one of these emotions that best describe you. \n[Write CHEERFUL / CONTENT / PROUD]\n")
  
  #joy_emotion
  
  if joy_emotion.lower() == "cheerful":
    cheerful = [fetch_ayah(14,7), fetch_ayah(18,46)]
    verse_cheerful = random.choice(cheerful)
    print("\n"+verse_cheerful)
  elif joy_emotion.lower() == "content":
    content = [fetch_ayah(13,28), fetch_ayah(2,152)]
    verse_content = random.choice(content)
    print("\n"+verse_content)
  elif joy_emotion.lower() == "proud":
    proud = [fetch_ayah(16,18), fetch_ayah(28,73)]
    verse_proud = random.choice(proud)
    print("\n"+verse_proud)
  else:
    print("We can't find an ayah for you right now. Please start over.")
  
elif feeling.lower() == "sad":
  sad_emotion = input("\nI'm sorry you're feeling this way.\nWhich one of these emotions best describe how you feel?\n[Write HURT / DISAPPOINTED / LONELY]\n")

  #sad_emotion
  
  if sad_emotion.lower() == "hurt":
    hurt = [fetch_ayah(2,155), fetch_ayah(2,286)]
    verse_hurt = random.choice(hurt)
    print("\n"+verse_hurt)
  elif sad_emotion.lower() == "disappointed":
    disappointed = [fetch_ayah(3,135), fetch_ayah(16,127)]
    verse_disappointed = random.choice(disappointed)
    print("\n"+verse_disappointed)
  elif sad_emotion.lower() == "lonely":
    lonely = [fetch_ayah(50,16), fetch_ayah(9,40)]
    verse_lonely = random.choice(lonely)
    print("\n"+verse_lonely)
  else:
    print("We can't find an ayah for you right now. Please start over.")
    
else:
  print("We can't find an ayah for you right now. Please start over.")

# END #