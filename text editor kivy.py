from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.utils import escape_markup


class TextEditor(BoxLayout):
    def __init__(self, **kwargs):
        super(TextEditor, self).__init__(**kwargs)

        self.orientation = 'vertical'

        # Create the menu bar and move it to the top
        menu_layout = BoxLayout(orientation="horizontal", size_hint=(1, None), height=44)

        menu_spinner = Spinner(text="Menu", values=["Load", "Save"], size_hint=(None, None), size=(80, 32))
        menu_spinner.bind(text=self.menu_selected)
        menu_layout.add_widget(menu_spinner)

        self.add_widget(menu_layout)

        # Create the text input area and make it fill the remaining space
        self.text_input = TextInput(multiline=True)
        self.add_widget(self.text_input)

    def menu_selected(self, instance, text):
        if text == "Load":
            self.open_file()
        elif text == "Save":
            self.save_file()

    def open_file(self):
        # Open a file and load its contents into the text input field
        file_chooser = FileChooserListView()
        file_chooser.bind(on_submit=self.load_file)

        popup = Popup(title="Open File", content=file_chooser, size_hint=(0.8, 0.8), auto_dismiss=False)
        popup.open()

    def load_file(self, instance, selection, *args):
        selected_file = selection and selection[0]
        if selected_file:
            with open(selected_file, "r") as f:
                self.text_input.text = f.read()
        instance.parent.parent.parent.dismiss()

    def save_file(self):
        # Create a popup for renaming the file
        popup_content = BoxLayout(orientation="vertical")
        label = Label(text="Enter file name:")
        popup_content.add_widget(label)
        text_input = TextInput()
        popup_content.add_widget(text_input)
        save_button = Button(text="Save", on_release=lambda x: self.perform_save(x, text_input.text), size_hint=(None, None), size=(80, 32))
        popup_content.add_widget(save_button)

        popup = Popup(title="Save File", content=popup_content, size_hint=(0.8, 0.4), auto_dismiss=False)
        save_button.bind(on_release=lambda x: popup.dismiss())
        popup.open()

    def perform_save(self, instance, filename):
        # Save the contents of the text input field to a file
        if filename:
            with open(filename, "w") as f:
                f.write(self.text_input.text)


class TextEditorApp(App):
    def build(self):
        return TextEditor()


if __name__ == '__main__':
    TextEditorApp().run()
