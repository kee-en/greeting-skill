from mycroft import MycroftSkill, intent_file_handler


class Greeting(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('greeting.intent')
    def handle_greeting(self, message):
        self.speak_dialog('greeting')


def create_skill():
    return Greeting()

