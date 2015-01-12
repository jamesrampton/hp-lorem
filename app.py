from pipes import quote
import rumps
import random
import os
from texts.texts import TEXTS


class HPLorem(rumps.App):
    
    def __init__(self, titles, paragraphs):
        super(HPLorem, self).__init__("(;,;)")
        self.paragraphs = paragraphs
        self.titles = titles

    def copy_to_clipboard(self, text):
        os.system('pbcopy "{}"'.format(quote(text)))

    def get_new_random_item(self, items, previous_item):
        new_item = None
        while new_item == previous_item:
            # Keep going until we get a different one
            new_item = random.choice(items)
        return new_item

    @rumps.clicked("Title")
    def title(self, _):
        self.latest_title = get_new_random_item(self.titles, self.latest_title)
        return self.copy_to_clipboard(self.latest_item)

    @rumps.clicked("Paragraph")
    def paragraph(self, _):
        self.latest_paragraph = get_new_random_item(self.paragraphs, self.latest_paragraph)
        return self.copy_to_clipboard(self.latest_paragraph)

if __name__ == "__main__":
    HPLorem(
        titles=TEXTS['titles'],
        paragraphs=TEXTS['paragraphs'],
    ).run()
