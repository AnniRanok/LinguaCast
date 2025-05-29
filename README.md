# LinguaCast: Personal Text-to-Speech Studio

A simple and user-friendly desktop application for converting text to speech (MP3) using the [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/) library. Supports input from manual text, `.txt`, `.pdf`, and `.docx` files. Built with Python and Tkinter. Perfect for language learners, presenters, and anyone who needs text read aloud.

# Why I Built This

As a data scientist working across projects in multiple languages, I needed a tool to turn written materials into audio — so I could listen to them during morning runs, commutes, or while waiting in line.

That’s how **LinguaCast** was born: a practical solution for transforming passive time into active language practice.

# Features

*  Intuitive graphical interface using `tkinter`
*  Load text from `.txt`, `.pdf`, or `.docx` files
*  Convert text to `.mp3` using `gTTS`
*  Choose from 30+ supported languages
*  Built-in audio player: **Play / Pause / Stop**
*  Paste text with right-click menu or keyboard shortcut



# Screenshots

![Screenshot](image.jpg)




# Requirements

* Python 3.7+
* [gTTS](https://pypi.org/project/gTTS/)
* [pygame](https://pypi.org/project/pygame/)
* [PyPDF2](https://pypi.org/project/PyPDF2/)
* [python-docx](https://pypi.org/project/python-docx/)

Install requirements:

```bash
pip install gTTS pygame PyPDF2 python-docx
```



#  How to Run

1. Clone this repository or download the source code.
2. Run the script:

```bash
python app.py
```



#  File Support

* `.txt` — loaded as plain text
* `.pdf` — text is extracted using `PyPDF2`
* `.docx` — text extracted from paragraphs



# Use Cases

* Language learning: create personalized audio flashcards
* Reading notes aloud
* Preparing for presentations
* Text accessibility support

# LinguaCast 

[Read the story on Medium →](https://medium.com/@konar.inna/three-lines-of-code-that-changed-how-i-learn-languages-428b3cb45336)


#  License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.



# Contributing

Pull requests are welcome! If you want to suggest improvements, fix bugs, or add features — go for it.



# Author


Created by Inna Konar,
AI & Data Science enthusiast making language learning more musical, mobile, and meaningful.

“Sometimes three lines of code can do more than three hours of lecture.”
