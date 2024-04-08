import datetime
import json
from app_class.Translator import Translator
from app_class.MirrorApp import MirrorApp

def main():
    translator = Translator()
    lang = ""

    while lang not in list(translator.languages.keys()):
        primary_keys = [key for key in translator.languages.keys()]
        formatted_keys = "/".join(primary_keys)  
        lang = input(f"Choose a language in the list ({formatted_keys}) ")

    app = MirrorApp(translator)
    app.run(lang)

if __name__ == "__main__":
    main()
