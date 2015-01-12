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

    def get_new_random_item(self, items, previous_item):
        while self.latest_paragraph == self.previous_title:
            self.latest_title = random.choice(self.paragraphs)
        self.copy_to_clipboard(self.latest_title)

    @rumps.clicked("Title")
    def title(self, _):
        self.latest_title = get_new_random_item(self.titles, self.latest_title)
        return copy_to_clipboard(self.latest_item)

    @rumps.clicked("Paragraph")
    def paragraph(self, _):
        self.latest_paragraph = get_new_random_item(self.paragraphs, self.latest_paragraph)
        return copy_to_clipboard(self.latest_paragraph)

if __name__ == "__main__":
    HPLorem().run()
