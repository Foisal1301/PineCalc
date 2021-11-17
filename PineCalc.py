import math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_string("""
<MyLayout>
    BoxLayout:
        orientation:'vertical'
        size:root.width,root.height

        TextInput:
            id:input
            text:'0'
            halign:"right"
            font_size:43
            size_hint: (1,.3)

        GridLayout:
            cols:4

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"%"
                on_press:root.btn_press("%")

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"C"
                on_press:root.clear()

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:u"\u00AB"
                on_press:root.remove()

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"π"
                on_press:root.btn_press("π")

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"e"
                on_press:root.btn_press("e")

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"!"
                on_press:root.btn_press("!")

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"^"
                on_press:root.btn_press("^")
                
            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"x³"
		        on_press:root.btn_press("³")
            
            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"x²"
                on_press:root.btn_press("²")
            
            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"("
                on_press:root.btn_press("(")

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:")"
                on_press:root.btn_press(")")

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"÷"
                on_press:root.btn_press("÷")

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"7"
                background_color:(157/255,157/255,157/255,1)
                on_press:root.btn_press(7)

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"8"
                background_color:(157/255,157/255,157/255,1)
                on_press:root.btn_press(8)

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"9"
                background_color:(157/255,157/255,157/255,1)
                on_press:root.btn_press(9)

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"X"
                on_press:root.btn_press("X")

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"4"
                background_color:(157/255,157/255,157/255,1)
                on_press:root.btn_press(4)

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"5"
                background_color:(157/255,157/255,157/255,1)
                on_press:root.btn_press(5)

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"6"
                background_color:(157/255,157/255,157/255,1)
                on_press:root.btn_press(6)

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"-"
                on_press:root.btn_press("-")

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"1"
                background_color:(157/255,157/255,157/255,1)
                on_press:root.btn_press(1)

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"2"
                background_color:(157/255,157/255,157/255,1)
                on_press:root.btn_press(2)

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"3"
                background_color:(157/255,157/255,157/255,1)
                on_press:root.btn_press(3)

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"+"
                on_press:root.btn_press("+")

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"+/-"
                background_color:(157/255,157/255,157/255,1)
                on_press:root.pos_neg()

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"0"
                background_color:(157/255,157/255,157/255,1)
                on_press:root.btn_press(0)

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"."
                background_color:(157/255,157/255,157/255,1)
                on_press:root.btn_press(".")

            Button:
                size_hint: (.2,.2)
                font_size:32
                text:"="
                on_press:root.equal()
""")


class MyLayout(Widget):
    def remove(self):
        if self.ids.input.text == "ERROR" or self.ids.input.text == "0":
            self.ids.input.text = "0"
        else:
            if len(self.ids.input.text) == 1:
                self.ids.input.text = "0"
            else:
                self.ids.input.text = self.ids.input.text[:-1]

    def pos_neg(self):
        if self.ids.input.text[0] == "-":
            self.ids.input.text = self.ids.input.text[1:]
        else:
            if self.ids.input.text == "0" or self.ids.input.text == "ERROR":
                pass
            else:
                self.ids.input.text = "-" + self.ids.input.text

    def clear(self):
        self.ids.input.text = "0"

    def btn_press(self, btn):
        if self.ids.input.text == "0" or self.ids.input.text == "ERROR":
            if btn in [".","X","+","-","÷"]:
                self.ids.input.text = f"0{btn}"
            elif btn in ["!","%"]:
                self.ids.input.text = f"0"
            elif btn == ")":
                pass
            elif btn in ["²","^","³"]:
                self.ids.input.text = f"0{btn}"
            else:
                self.ids.input.text = f"{btn}"
        else:
            if btn in ["!","X","+","-","÷",".","%","²","^","³"]:
                if self.ids.input.text[::-1][0] in ["!","X","+","÷",".","^","("]:
                    pass
                elif btn in ["²","³"] and self.ids.input.text[::-1][0] in ["²","³"]:
                    pass
                else:
                    self.ids.input.text = f"{self.ids.input.text}{btn}"
            elif btn == "(":
                if self.ids.input.text[::-1][0] in ")0123456789":
                    self.ids.input.text = f"{self.ids.input.text}X{btn}"
                elif self.ids.input.text[::-1][0] == "(":
                    pass
                else:
                    self.ids.input.text = f"{self.ids.input.text}{btn}"
            elif btn == ")":
                if self.ids.input.text[::-1][0] in ["!","X","+","-","÷",".",")","^"] or "(" not in self.ids.input.text:
                    pass
                else:
                    self.ids.input.text = f"{self.ids.input.text}{btn}"
            elif btn in list(range(10)):
                if self.ids.input.text[::-1][0] == ")":
                    self.ids.input.text = f"{self.ids.input.text}X{btn}"
                else:
                    self.ids.input.text = f"{self.ids.input.text}{btn}"
            else:       
                self.ids.input.text = f"{self.ids.input.text}{btn}"

    def equal(self):
        equation = ""
        for i in self.ids.input.text:
            if i == "X":
                i = "*"
            elif i == "÷":
                i = "/"
            elif i == "%":
                i = "*100"
            elif i == "!":
                try:
                    i = ""
                    for p in equation[::-1]:
                        if p in ["+", "-", "*", "/"]:
                            break
                        i = p + i
                    if i in equation:
                        equation = equation.replace(i, '')
                    i = str(math.factorial(int(i)))
                except:
                    equation = "error"
                    break
            elif i == "^":
                i = "**"
            elif i == "π":
                i = str(math.pi)
            elif i == "e":
                i = "2.71828182846"
            elif i == "²":
                i = "**2"
            elif i == "³":
                i = "**3"
            equation += i

        try:
            self.ids.input.text = str(eval(equation))
        except:
            self.ids.input.text = "ERROR"


class PineCalc(App):
    def build(self):
        self.icon = "PineCalc.ico"
        return MyLayout()

if __name__ == "__main__":
    PineCalc().run()
