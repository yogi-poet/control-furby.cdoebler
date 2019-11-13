from mycroft import MycroftSkill, intent_file_handler
import subprocess


class ControlFurby(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('furby.tell.intent')
    def handle_furby_tell(self, message):
        self.speak_dialog('furby.tell')

    @intent_file_handler('furby.dance.intent')
    def handle_furby_dance(self, message):
        self.speak_dialog('furby.dance')

    @intent_file_handler('furby.sing.intent')
    def handle_furby_sing(self, message):
        self.speak_dialog('furby.sing')
        subprocess.call(["perl", "~/Hacksby/bin/furby-send.pl", "820"])
        subprocess.call(["perl", "~/Hacksby/bin/furby-send.pl", "868"])


def create_skill():
    return ControlFurby()
