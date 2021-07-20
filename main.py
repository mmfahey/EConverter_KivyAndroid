'''Android application for energy conversions

This program allows for a GUI giving users the ability to enter energy 
values and convert them to a set of other energy units. Usage is mainly
for physical sciences and spectroscopy. GUI built using Kivy and the 
program can be packaged via buildozer for Android. 

'''

import re

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton

from EnergyConversions import convert2eV, convert2hartree, convert2joule, convert2kcal, convert2wavenumber, convert2nm

#Center text in Vertical stuff
#Post

class FloatInput(TextInput):

#Input GUI class that only takes Float inputs, overrides input_text function
#and uses regular expressions to filter non-numerical inputs.

    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)

class WrappedLabel(Label):

#Label class that automatically wraps the text to fit window size, should
#do in .kv but this is easier at the moment

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            width=lambda *x:
            self.setter('text_size')(self, (self.width, None)),
            texture_size=lambda *x: self.setter('height')(self, self.texture_size[1]))

class MainApp(App):

    def build(self):
        main_layout = BoxLayout(orientation='vertical')

        #Creates float input for each unit and binds conversion to pressing enter following value entry

        self.eV = FloatInput(multiline=False, font_size=25)
        self.eV.bind(on_text_validate=self.convert_eV)

        self.wavenumbers = FloatInput(multiline=False, font_size=25)
        self.wavenumbers.bind(on_text_validate=self.convert_wavenumbers)

        self.nanometers = FloatInput(multiline=False, font_size=25)
        self.nanometers.bind(on_text_validate=self.convert_nanometers)

        self.hartrees = FloatInput(multiline=False, font_size=25)
        self.hartrees.bind(on_text_validate=self.convert_hartrees)

        self.kcals = FloatInput(multiline=False, font_size=25)
        self.kcals.bind(on_text_validate=self.convert_kcals)

        self.joules = FloatInput(multiline=False, font_size=25)
        self.joules.bind(on_text_validate=self.convert_joules)

        #box matrix of GUI elements

        objs = [
            ['eV', self.eV],
            ['Wavenumbers', self.wavenumbers],
            ['Nanometers', self.nanometers],
            ['Hartrees', self.hartrees],
            ['kcal/mol', self.kcals],
            ['kJ/mol', self.joules]
        ]

        #loop through matrix to generate GUI

        for row in objs:
            row_layout = BoxLayout()
            l = Label(text=row[0], font_size=25)
            row_layout.add_widget(l)
            row_layout.add_widget(row[1])
            main_layout.add_widget(row_layout)

        #instructions for users

        instructions = WrappedLabel(halign='justify', text='''To use energy converter, enter a value into any of the entry boxes shown. Upon pressing ENTER, the remaining values will be calculated and displayed. The next conversion is not started until ENTER is pressed.''')

        main_layout.add_widget(instructions)
        return main_layout

    #Each function handles a seperate unit/input box, likely could refactor this to clean up.
    #Following the user pressing enter after value entry, the function will be called for the 
    #specific unit. The following function blocks are repeated so only documenting the first one.
    def convert_eV(self, instance):

        #if value is 0, all values are 0 -> needed for div0
        if self.eV.text == '0':
            self.wavenumbers.text = str(0)
            self.nanometers.text = str(0)
            self.hartrees.text = str(0)
            self.kcals.text = str(0)
            self.joules.text = str(0)

        #No value was entered so dont do anything -> crashes when converting without
        elif self.eV.text == '':
            self.wavenumbers.text = ''
            self.nanometers.text = ''
            self.hartrees.text = ''
            self.kcals.text = ''
            self.joules.text = ''

        #Convert the value entered
        else:
            self.wavenumbers.text = str(convert2wavenumber(self.eV.text, 'eV'))
            self.nanometers.text = str(convert2nm(self.eV.text, 'eV'))
            self.hartrees.text = str(convert2hartree(self.eV.text, 'eV'))
            self.kcals.text = str(convert2kcal(self.eV.text, 'eV'))
            self.joules.text = str(convert2joule(self.eV.text, 'eV'))

    def convert_wavenumbers(self, instance):
        if self.wavenumbers.text == '0':
            self.eV.text = str(0)
            self.nanometers.text = str(0)
            self.hartrees.text = str(0)
            self.kcals.text = str(0)
            self.joules.text = str(0)
        elif self.wavenumbers.text == '':
            self.eV.text = ''
            self.nanometers.text = ''
            self.hartrees.text = ''
            self.kcals.text = ''
            self.joules.text = ''
        else:
            self.eV.text = str(convert2eV(self.wavenumbers.text, 'wavenumber'))
            self.nanometers.text = str(convert2nm(self.wavenumbers.text, 'wavenumber'))
            self.hartrees.text = str(convert2hartree(self.wavenumbers.text, 'wavenumber'))
            self.kcals.text = str(convert2kcal(self.wavenumbers.text, 'wavenumber'))
            self.joules.text = str(convert2joule(self.wavenumbers.text, 'wavenumber'))

    def convert_nanometers(self, instance):
        if self.nanometers.text == '0':
            self.eV.text = str(0)
            self.wavenumbers.text = str(0)
            self.hartrees.text = str(0)
            self.kcals.text = str(0)
            self.joules.text = str(0)
        elif self.nanometers.text == '':
            self.eV.text = ''
            self.wavenumbers.text = ''
            self.hartrees.text = ''
            self.kcals.text = ''
            self.joules.text = ''
        else:
            self.eV.text = str(convert2eV(self.nanometers.text, 'nm'))
            self.wavenumbers.text = str(convert2wavenumber(self.nanometers.text, 'nm'))
            self.hartrees.text = str(convert2hartree(self.nanometers.text, 'nm'))
            self.kcals.text = str(convert2kcal(self.nanometers.text, 'nm'))
            self.joules.text = str(convert2joule(self.nanometers.text, 'nm'))

    def convert_hartrees(self, instance):
        if self.hartrees.text == '0':
            self.eV.text = str(0)
            self.wavenumbers.text = str(0)
            self.nanometers.text = str(0)
            self.kcals.text = str(0)
            self.joules.text = str(0)
        elif self.hartrees.text == '':
            self.eV.text = ''
            self.wavenumbers.text = ''
            self.nanometers.text = ''
            self.kcals.text = ''
            self.joules.text = ''
        else:
            self.eV.text = str(convert2eV(self.hartrees.text, 'hartree'))
            self.wavenumbers.text = str(convert2wavenumber(self.hartrees.text, 'hartree'))
            self.nanometers.text = str(convert2nm(self.hartrees.text, 'hartree'))
            self.kcals.text = str(convert2kcal(self.hartrees.text, 'hartree'))
            self.joules.text = str(convert2joule(self.hartrees.text, 'hartree'))

    def convert_kcals(self, instance):
        if self.kcals.text == '0':
            self.eV.text = str(0)
            self.wavenumbers.text = str(0)
            self.nanometers.text = str(0)
            self.hartrees.text = str(0)
            self.joules.text = str(0)
        elif self.kcals.text == '':
            self.eV.text = ''
            self.wavenumbers.text = ''
            self.nanometers.text = ''
            self.hartrees.text = ''
            self.joules.text = ''
        else:
            self.eV.text = str(convert2eV(self.kcals.text, 'kcal/mol'))
            self.wavenumbers.text = str(convert2wavenumber(self.kcals.text, 'kcal/mol'))
            self.nanometers.text = str(convert2nm(self.kcals.text, 'kcal/mol'))
            self.hartrees.text = str(convert2hartree(self.kcals.text, 'kcal/mol'))
            self.joules.text = str(convert2joule(self.kcals.text, 'kcal/mol'))

    def convert_joules(self, instance):
        if self.joules.text == '0':
            self.eV.text = str(0)
            self.wavenumbers.text = str(0)
            self.nanometers.text = str(0)
            self.hartrees.text = str(0)
            self.kcals.text = str(0)
        elif self.joules.text == '':
            self.eV.text = ''
            self.wavenumbers.text = ''
            self.nanometers.text = ''
            self.hartrees.text = ''
            self.kcals.text = ''
        else:
            self.eV.text = str(convert2eV(self.joules.text, 'kJ/mol'))
            self.wavenumbers.text = str(convert2wavenumber(self.joules.text, 'kJ/mol'))
            self.nanometers.text = str(convert2nm(self.joules.text, 'kJ/mol'))
            self.hartrees.text = str(convert2hartree(self.joules.text, 'kJ/mol'))
            self.kcals.text = str(convert2kcal(self.joules.text, 'kJ/mol'))   

if __name__ == "__main__":
    app = MainApp()
    app.run()