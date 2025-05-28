#!/usr/bin/env python
# coding: utf-8

# In[10]:


import tkinter as tk
from tkinter import filedialog, messagebox
from gtts import gTTS
from gtts.lang import tts_langs
import PyPDF2
import docx
import pygame 

# Get a list of supported languages
languages = tts_langs()

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text-to-Speech Generator")

        pygame.mixer.init()  # initialize the audio module

        # Option1: Text input
        self.text_label = tk.Label(root, text="Enter text:")
        self.text_label.pack()

        self.text_input = tk.Text(root, height=10, width=50)
        self.text_input.pack()

        self.add_context_menu()

        # Option2: Insert button (from the keyboard)
        self.paste_button = tk.Button(root, text="Paste", command=self.paste)
        self.paste_button.pack(pady=2)

        # Option3: Download button from file
        self.load_button = tk.Button(root, text="Load from File", command=self.load_text)
        self.load_button.pack(pady=5)

        # Language selection menu
        self.lang_label = tk.Label(root, text="Select language:")
        self.lang_label.pack()

        self.lang_var = tk.StringVar(root)
        self.lang_var.set("en")  # default

        self.lang_menu = tk.OptionMenu(root, self.lang_var, *languages.keys())
        self.lang_menu.pack()

        self.save_button = tk.Button(root, text="Generate MP3", command=self.generate_audio)
        self.save_button.pack(pady=10)

        # Audio control buttons
        self.play_button = tk.Button(root, text="▶️ Play", command=self.play_audio)
        self.play_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(root, text="⏸ Pause", command=self.pause_audio)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="⏹ Stop", command=self.stop_audio)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.last_audio_path = None
        self.is_paused = False

    def add_context_menu(self):
        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="Cut", command=self.cut)
        self.menu.add_command(label="Copy", command=self.copy)
        self.menu.add_command(label="Paste", command=self.paste)
        self.text_input.bind("<Button-3>", self.show_context_menu)
        self.text_input.bind("<Control-Button-1>", self.show_context_menu)

    def show_context_menu(self, event):
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

    def cut(self):
        self.text_input.event_generate("<<Cut>>")

    def copy(self):
        self.text_input.event_generate("<<Copy>>")

    def paste(self):
        self.text_input.event_generate("<<Paste>>")

    def load_text(self):
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Text files", "*.txt"),
                ("PDF files", "*.pdf"),
                ("Word documents", "*.docx")
            ],
            title="Open File"
        )
        if file_path:
            try:
                content = ""
                if file_path.endswith(".txt"):
                    with open(file_path, "r", encoding="utf-8") as file:
                        content = file.read()
                elif file_path.endswith(".pdf"):
                    with open(file_path, "rb") as file:
                        reader = PyPDF2.PdfReader(file)
                        for page in reader.pages:
                            content += page.extract_text() or ""
                elif file_path.endswith(".docx"):
                    doc = docx.Document(file_path)
                    content = "\n".join([para.text for para in doc.paragraphs])
                else:
                    raise ValueError("Unsupported file type")

                self.text_input.delete("1.0", tk.END)
                self.text_input.insert(tk.END, content.strip())
            except Exception as e:
                messagebox.showerror("Error", f"Could not read file:\n{e}")

    def generate_audio(self):
        text = self.text_input.get("1.0", tk.END).strip()
        lang = self.lang_var.get()

        if not text:
            messagebox.showwarning("Warning", "Please enter some text.")
            return

        try:
            tts = gTTS(text=text, lang=lang)
            save_path = filedialog.asksaveasfilename(
                defaultextension=".mp3",
                filetypes=[("MP3 files", "*.mp3")],
                title="Save MP3"
            )
            if save_path:
                tts.save(save_path)
                self.last_audio_path = save_path
                messagebox.showinfo("Success", f"Audio saved to:\n{save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate audio:\n{e}")

    # Playback
    def play_audio(self):
        if self.last_audio_path:
            try:
                if self.is_paused:
                    pygame.mixer.music.unpause()
                    self.is_paused = False
                else:
                    pygame.mixer.music.load(self.last_audio_path)
                    pygame.mixer.music.play()
            except Exception as e:
                messagebox.showerror("Error", f"Cannot play audio:\n{e}")
        else:
            messagebox.showinfo("Info", "No audio file has been generated yet.")

    # Pause
    def pause_audio(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.is_paused = True

    # Stop
    def stop_audio(self):
        pygame.mixer.music.stop()
        self.is_paused = False

# Launching
if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()


# In[ ]:




