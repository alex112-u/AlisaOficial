
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

Window.clearcolor = (0.09, 0.06, 0.11, 1)

class AlisaApp(App):
    def build(self):
        root = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=12
        )

        titulo = Label(
            text="[color=ff80bd]🌸 ALISA 🌸[/color]",
            markup=True,
            font_size=32,
            size_hint_y=None,
            height=65
        )

        bienvenida = Label(
            text="¡Hola! Soy Alisa. ¿Cómo estás?",
            font_size=18,
            size_hint_y=None,
            height=45
        )

        self.historial = Label(
            text="",
            markup=True,
            size_hint_y=None,
            halign="left",
            valign="top"
        )
        self.historial.bind(
            width=lambda obj, w: setattr(obj, "text_size", (w, None))
        )
        self.historial.bind(
            texture_size=lambda obj, size: setattr(obj, "height", size[1])
        )

        scroll = ScrollView()
        scroll.add_widget(self.historial)

        self.entrada = TextInput(
            hint_text="Escribe a Alisa...",
            multiline=False,
            size_hint_y=None,
            height=52
        )
        self.entrada.bind(on_text_validate=self.enviar)

        boton = Button(
            text="Enviar",
            background_color=(0.95, 0.35, 0.65, 1),
            size_hint_y=None,
            height=52
        )
        boton.bind(on_press=self.enviar)

        root.add_widget(titulo)
        root.add_widget(bienvenida)
        root.add_widget(scroll)
        root.add_widget(self.entrada)
        root.add_widget(boton)

        return root

    def enviar(self, instance):
        mensaje = self.entrada.text.strip()

        if not mensaje:
            return

        self.historial.text += (
            f"[color=ff80bd]Tú:[/color] {mensaje}\n"
            "[color=ffffff]Alisa: ¡Qué interesante! Cuéntame más.[/color]\n\n"
        )

        self.entrada.text = ""

AlisaApp().run()
      
