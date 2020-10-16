from rumps import *
import os

class DevX(rumps.App):
    def __init__(self):
        self.config = {
            "info": {
                "name": "DevX",
                "icon": "",
            },
            "actions": {
                "add": {
                    "title": "Add",
                    "message": "Enter a new shortcut command",
                    "ok": "Add",
                    "cancel": "Cancel",
                },
                "exit": {
                    "title": "Stop DevX",
                    "message": "Do you want to quit DevX?",
                    "ok": "Exit",
                    "cancel": "Cancel",
                },
            }
        }

        self.commands = []

        # Create app
        super(DevX, self).__init__(type(self).__name__)
        rumps.debug_mode(True)

    @clicked("Add shortcut")
    def add_shortcut(self, sender):
        action = self.config['actions']['add']
        window = rumps.Window(title=action['title'], message=action['message'], ok=action['ok'], cancel=action['cancel'])
        response = window.run()
        if response.clicked:
            command = lambda c: os.system(response.text)
            self.commands.append({ 'title': response.text, 'callback': command })
            self.refresh_menu()

    def refresh_menu(self):
        self.menu = [rumps.MenuItem(title=com['title'], callback=com['callback']) for com in self.commands]

if __name__ == "__main__":
    app = DevX().run()