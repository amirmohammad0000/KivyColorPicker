##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start Import
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
import clipboard

Window.clearcolor = (1, 1, 1, 1)
##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ End Import


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start Class Main App
class MainApp(App):
    # Start Function Main App
    def build(self):
        return Builder.load_file("style.kv")

    # End Function Main App

    # Start Function Result
    def result(self):
        input_get_red = self.root.ids.input_get_red
        input_get_green = self.root.ids.input_get_green
        input_get_blue = self.root.ids.input_get_blue

        input_set_red = self.root.ids.input_set_red
        input_set_green = self.root.ids.input_set_green
        input_set_blue = self.root.ids.input_set_blue

        try:
            if input_get_red.text != "" and input_get_green.text != "" and input_get_blue.text != "":
                int_input_get_red = int(input_get_red.text)
                int_input_get_green = int(input_get_green.text)
                int_input_get_blue = int(input_get_blue.text)

                if int_input_get_red < 256 and int_input_get_green < 256 and int_input_get_blue < 256:
                    res_input_red = (int_input_get_red / 255)
                    res_input_green = (int_input_get_green / 255)
                    res_input_blue = (int_input_get_blue / 255)

                    format_float_red = "{:.2f}".format(res_input_red)
                    format_float_green = "{:.2f}".format(res_input_green)
                    format_float_blue = "{:.2f}".format(res_input_blue)

                    input_set_red.text = format_float_red
                    input_set_green.text = format_float_green
                    input_set_blue.text = format_float_blue

                    input_get_red.text = ""
                    input_get_green.text = ""
                    input_get_blue.text = ""
        except:
            input_get_red.text = ""
            input_get_green.text = ""
            input_get_blue.text = ""

    # End Function Result

    # Start Function Copy Number
    def copy(self):
        input_set_red = self.root.ids.input_set_red
        input_set_green = self.root.ids.input_set_green
        input_set_blue = self.root.ids.input_set_blue

        if input_set_red.text != "" and input_set_green.text != "" and input_set_blue.text != "":
            clipboard.copy(f"{input_set_red.text}, {input_set_green.text}, {input_set_blue.text}")
            input_set_red.text = ""
            input_set_green.text = ""
            input_set_blue.text = ""
    # End Function Copy Number


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ End Class Main App


##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Start Run App
MainApp().run()
##$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ End Run App
