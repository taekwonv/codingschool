from gtts import gTTS
import os
import playsound

def TTS(msg):
  tts = gTTS(msg)
  tts.save(msg + '.mp3')
  playsound.playsound(msg + '.mp3')

def main():
  os.system("cls")
  name = input("Your name? ")
  TTS('Hi ' + name)

  os.system("cls")
  print("What is the biggest fish?")
  print("1. whale")
  print("2. sharks")
  print("3. seal")
  answer = input("Your answer : ")
  if answer == '2':
    TTS('Correct. The answer is sharks')
  else:
    TTS('Good try. But the answer is sharks')

if __name__ == '__main__':
  main()
