import rumps
import subprocess


class AwesomeStatusBarApp(rumps.App):
    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__("Awesome App")
        self.menu = ["Clipit"]

    @rumps.clicked("Clipit")
    def clip(self, _):
        stuff = "This is some stuff"
        p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
        p.stdin.write(stuff)
        p.stdin.close()

if __name__ == "__main__":
    AwesomeStatusBarApp().run()
