import rumps
import subprocess


class HPLorem(rumps.App):
    def __init__(self):
        super(HPLorem, self).__init__("HP Lorem")

    def copy_to_clipboard(self, text):
        p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
        p.stdin.write(text)
        p.stdin.close()

    @rumps.clicked("One word")
    def one_word(self, _):
        text = "Thing"
        self.copy_to_clipboard(text)

    @rumps.clicked("Two words")
    def two_words(self, _):
        text = "Thing things"
        self.copy_to_clipboard(text)

if __name__ == "__main__":
    HPLorem().run()
