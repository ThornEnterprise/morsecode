import numpy as np
import sounddevice as sd
import time

# Define the Morse code lookup table
morse_table = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", ".": ".-.-.-", ",": "--..--",
    "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...",
    ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-", "_": "..--.-", "\"": ".-..-.",
    "$": "...-..-", "@": ".--.-.", " ": " "
}

# Define the frequency and duration of the white noise signal
noise_freq = 440
noise_duration = 0.1

# Define the duration of a dot and a dash in Morse code
dot_duration = 0.1
dash_duration = 3 * dot_duration

# Define the duration of a space between dots and dashes within a letter
element_space_duration = dot_duration

# Define the duration of a space between letters in a word
letter_space_duration = 3 * dot_duration

# Define the duration of a space between words
word_space_duration = 7 * dot_duration

# Define the input message
input_message = "HELLO WORLD"

# Generate the white noise signal
t = np.linspace(0, noise_duration, int(noise_duration * 44100), False)
noise_signal = np.sin(noise_freq * 2 * np.pi * t)

# Convert the input message to Morse code
morse_message = ""
for char in input_message:
    if char.upper() in morse_table:
        morse_message += morse_table[char.upper()] + " "
    else:
        morse_message += " "

# Play the Morse code signal
for char in morse_message:
    if char == ".":
        sd.play(noise_signal)
        time.sleep(dot_duration)
    elif char == "-":
        sd.play(noise_signal)
        time.sleep(dash_duration)
    elif char == " ":
        time.sleep(letter_space_duration)
    else:
        time.sleep(word_space_duration)
