from pynput.keyboard import Key, Controller
import time

sentence = input('<delay><Sentence>(No Space): ')
for i in range(int(sentence[0]), 0, -1):
    print(i)
    time.sleep(1)


keyboard = Controller()
print('Typing...')

for letter in sentence[1:]:
    time.sleep(0.02) # typing speed
    keyboard.press(letter)
