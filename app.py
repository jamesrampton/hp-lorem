import rumps
import subprocess
from random import randint

from texts.texts import TEXTS as t


class HPLorem(rumps.App):
    def __init__(self):
        super(HPLorem, self).__init__("(;,;)")
        self.prev_rand = None
        self.curr_rand = None

    def copy_to_clipboard(self, text):
        p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
        p.stdin.write(text)
        p.stdin.close()

    def get_number(self, length=1, start=0):
        self.curr_rand = randint(start, length)
        if self.prev_rand >= 0:
            if self.curr_rand == self.prev_rand:
                self.get_number(length, start)
        self.prev_rand = self.curr_rand
        return self.curr_rand

    def get_text(self, texts):
        length = len(texts)-1
        return texts[self.get_number(length)]

    @rumps.clicked("Title")
    def title(self, _):
        texts = t['titles']
        self.copy_to_clipboard(self.get_text(texts))

    @rumps.clicked("Paragraph")
    def paragraph(self, _):
        texts = t['paragraphs']
        self.copy_to_clipboard(self.get_text(texts))

if __name__ == "__main__":
    HPLorem().run()
