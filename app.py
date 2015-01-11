import rumps
import subprocess
from random import randint

from texts.texts import TEXTS as t


class HPLorem(rumps.App):
    def __init__(self):
        super(HPLorem, self).__init__("(;,;)")

    def copy_to_clipboard(self, text):
        p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
        p.stdin.write(text)
        p.stdin.close()

    @rumps.clicked("Title")
    def one_word(self, _):
        texts = t['titles']
        text = texts[randint(0, len(texts))]
        self.copy_to_clipboard(text)

if __name__ == "__main__":
    HPLorem().run()
