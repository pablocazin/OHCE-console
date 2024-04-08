import datetime


class MirrorApp:

    def __init__(self, translator):
        self.translator = translator

    def get_greeting(self, lang, current_hour):
        if 6 <= current_hour < 18:
            return self.translator.get_language(lang).greeting_morning
        else:
            return self.translator.get_language(lang).greeting_evening

    def get_goodbye(self, lang):
        return self.translator.get_language(lang).goodbye

    def get_palindrome_response(self, lang):
        return self.translator.get_language(lang).palindrome_response

    def get_enter_text_prompt(self, lang):
        return self.translator.get_language(lang).enter_text_prompt

    def reverse_string(self, s):
        return s[::-1]

    def is_palindrome(self, s):
        return s == s[::-1]

    def run(self, lang):
        current_hour = datetime.datetime.now().hour
        print(self.get_greeting(lang, current_hour))

        while True:
            user_input = input(self.get_enter_text_prompt(lang))
            if user_input.lower() == self.translator.get_language(lang).exit_word:
                break
            reversed_text = self.reverse_string(user_input)
            if self.is_palindrome(user_input):
                print(self.get_palindrome_response(lang))
            else:
                print(f"{self.translator.get_language(lang).mirrored_text}:", reversed_text)
            
        print(self.get_goodbye(lang))