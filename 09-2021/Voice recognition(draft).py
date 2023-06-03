import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import threading
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play

# Global variables
recording = False
stop_recording = False
recognizing = False

# Create main window
root = tk.Tk()
root.title("Voice Recognition")
root.geometry("400x300")

# Function to open file dialog for selecting audio file
def open_file():
    file_path = filedialog.askopenfilename()
    # Display audio file path in GUI
    audio_path_label.config(text="Audio File: " + file_path)

# Function to update GUI with recognized text
def update_recognized_text(text):
    recognized_text.config(state=tk.NORMAL)
    recognized_text.delete("1.0", tk.END)
    recognized_text.insert(tk.END, text)
    recognized_text.config(state=tk.DISABLED)

# Function to recognize audio
def recognize_audio():
    global recognizing
    global stop_recording

    if stop_recording:
        return

    # Load audio file
    audio_file_path = audio_path_label["text"][12:]
    audio = AudioSegment.from_file(audio_file_path)
    audio.export("temp.wav", format="wav")

    # Recognize audio
    recognizer = sr.Recognizer()
    with sr.AudioFile("temp.wav") as source:
        try:
            audio_data = recognizer.record(source)
            recognized_text = recognizer.recognize_google(audio_data)
            update_recognized_text(recognized_text)
        except sr.UnknownValueError:
            update_recognized_text("No speech detected")
        except sr.RequestError:
            update_recognized_text("Error recognizing speech")
        except Exception as e:
            update_recognized_text(str(e))

    recognizing = False

# Function to start recording audio
def start_recording():
    global recording
    global stop_recording

    if recording:
        return

    recording = True
    stop_recording = False
    recognized_text.config(state=tk.NORMAL)
    recognized_text.delete("1.0", tk.END)
    recognized_text.config(state=tk.DISABLED)
    record_button.config(text="Stop Recording")

    # Start recording audio in a separate thread
    def record_audio():
        while recording:
            with sr.Microphone() as source:
                recognizer = sr.Recognizer()
                try:
                    audio_data = recognizer.listen(source)
                    audio_data.export("temp.wav", format="wav")
                    play(audio_data)
                    if not stop_recording:
                        root.after(0, recognize_audio)
                except Exception as e:
                    print(str(e))
    threading.Thread(target=record_audio).start()

# Function to stop recording audio
def stop_recording():
    global recording
    recording = False
    record_button.config(text="Start Recording")

# Create UI elements
open_file_button = tk.Button(root, text="Open Audio File", command=open_file)
open_file_button.pack(pady=10)

audio_path_label = tk.Label(root, text="Audio File: ")
audio_path_label.pack()

record_button = tk.Button(root, text="Start Recording", command=start_recording)
record_button.pack(pady=10)

recognized_text = tk.Text(root, height=10, width=40, state=tk.DISABLED)
recognized_text.pack()

root.mainloop()
