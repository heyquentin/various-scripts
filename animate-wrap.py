#Text Animation -  www.101computing.net/text-based-animations/
import os
import time
import textwrap

def getcontents():
    with open('contents.txt', 'r') as file:
        data = file.read().strip()
        return data

def animate_text(text):
  number_of_characters=1
  while True:
    print("\n")
    wrapper = textwrap.TextWrapper(width=20)
    text = wrapper.fill(text=text)
    print(text[0:number_of_characters])
    number_of_characters += 1
    if number_of_characters > len(text):
      number_of_characters = 0
      text = str(getcontents())
      time.sleep(10)
    time.sleep(0.1)
    os.system('clear')

#Main Program Starts Here....
animate_text(str(getcontents()))
