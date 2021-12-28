from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import datetime

# Rozměr okna pomoci kivy conf

Config.set('graphics', 'resizable', True)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

# Class Container atribut GridLayout  kivy.unix


class Container(GridLayout):

    text_input = ObjectProperty()   # Řadka kam se vypisuje počet dovolené

# funkce umožňuje otevřít textoý dokument přečíst a poslat do kivy Label

    def showtext(self):
        with open("dovolena_dni.txt", "r") as f:
            return f.read()

# Funkce umožňuje zobrázit čas a datum

    def showdatatime(self):
        date_d = datetime.datetime.now()
        str_d = str(date_d.strftime("%c"))
        return str_d

# Funkce clear

    def clear_txt(self):
        self.krakozjabra.text = ''

# Funkce umožňuje změnu textu na obrazovce, konkretně zadána hodnota od uživatele

    def change_text(self):
        self.label_widget.text = self.krakozjabra.text
        text = self.krakozjabra.text
        text = text.strip()
        special_char = '@_!#$%^&*()<>?/\|}{~:;[]-'

# Veškeré podmínky pro fungování programu a ukládaní

        for i in special_char:
            text = text.replace(i, ' ')

        if text.isalpha() or text.isspace() or text in special_char:

            self.label_widget.text = 'Zadávejte jen čísla !'

        else:
            try:
                if text != float:
                    text = float(text.replace(',', '.'))
                    text = str(text)
                    with open('dovolena_dni.txt', mode='w') as myfile:
                        myfile.write(f'{float(text)}')
                        print('Počet dnů je uloženo ' + text)
            except ValueError as err:
                print(err)

            self.label_widget.text = 'Máte ' + text + ' dnů !'


class MyApp(App):
    def build(self):

        return Container()

# Start aplikace

if __name__ == '__main__':
    MyApp().run()