import rumps
import random
import subprocess
from texts.texts import TEXTS


class HPLorem(rumps.App):

    def __init__(self, titles, paragraphs):
        super(HPLorem, self).__init__("(;,;)")
        self.paragraphs = paragraphs
        self.titles = titles
        self.latest_paragraph, self.latest_title = 0, 0

    def copy_to_clipboard(self, text):
        p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
        p.stdin.write(text)
        p.stdin.close()

    def get_new_random_item(self, items, previous_item):
        new_item = previous_item
        while new_item == previous_item:
            # Keep going until we get a different one
            new_item = random.choice(items)
        return new_item

    @rumps.clicked("Title")
    def title(self, _):
        self.latest_title = self.get_new_random_item(self.titles, self.latest_title)
        return self.copy_to_clipboard(self.latest_title)

    @rumps.clicked("Paragraph")
    def paragraph(self, _):
        self.latest_paragraph = self.get_new_random_item(self.paragraphs, self.latest_paragraph)
        return self.copy_to_clipboard(self.latest_paragraph)

if __name__ == "__main__":
    HPLorem(
        titles=TEXTS['titles'],
        paragraphs=TEXTS['paragraphs'],
    ).run()
