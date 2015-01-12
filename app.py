import rumps
import random
import subprocess
from random import randint
from texts.texts import TEXTS as t


class HPLorem(rumps.App):
    
    def __init__(self):
        super(HPLorem, self).__init__("(;,;)")
        self.paragraphs = t['paragraphs']
        self.titles = t['titles']

    def copy_to_clipboard(self, text):
        with p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE):
            p.stdin.write(text)

    @rumps.clicked("Title")
    def title(self, _):
        self.previous_title = self.latest_title
        while self.latest_paragraph == self.previous_title:
            self.latest_title = random.choice(self.paragraphs)
        self.copy_to_clipboard(self.latest_title)

    @rumps.clicked("Paragraph")
    def paragraph(self, _):
        self.previous_paragraph = self.latest_paragraph
        while self.latest_paragraph == self.previous_paragraph:
            self.latest_paragraph = random.choice(self.paragraphs)
        self.copy_to_clipboard(self.latest_paragraph)

if __name__ == "__main__":
    HPLorem().run()
