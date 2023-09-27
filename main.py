import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class AppGridLayout(GridLayout):

    def __init__(self, **kwargs):
        super(AppGridLayout, self).__init__(**kwargs)

        self.costs_input = [0 for _ in range(12)]
        self.result = 0

        self.cols = 1

        # Create money_enter frame.
        self.money_enter = GridLayout(size_hint_y=None,
                                      height=400)
        self.money_enter.cols = 3

        # Create money cost labels and inputs.
        # Labels for 1, 3, 5 costs:
        self.money_enter.add_widget(Label(text="1"))
        self.money_enter.add_widget(Label(text="3"))
        self.money_enter.add_widget(Label(text="5"))

        # Inputs for 1, 3, 5 costs:
        # cost 1
        self.costs_input[0] = TextInput(multiline=False)
        self.money_enter.add_widget(self.costs_input[0])
        # cost 3
        self.costs_input[1] = TextInput(multiline=False)
        self.money_enter.add_widget(self.costs_input[1])
        # cost 5
        self.costs_input[2] = TextInput(multiline=False)
        self.money_enter.add_widget(self.costs_input[2])

        # Labels for 10, 20, 50 costs:
        self.money_enter.add_widget(Label(text="10"))
        self.money_enter.add_widget(Label(text="20"))
        self.money_enter.add_widget(Label(text="50"))

        # Inputs for 1, 3, 5 costs:
        # cost 10
        self.costs_input[3] = TextInput(multiline=False)
        self.money_enter.add_widget(self.costs_input[3])
        # cost 20
        self.costs_input[4] = TextInput(multiline=False)
        self.money_enter.add_widget(self.costs_input[4])
        # cost 50
        self.costs_input[5] = TextInput(multiline=False)
        self.money_enter.add_widget(self.costs_input[5])

        # Labels for 100, 200, 500 costs:
        self.money_enter.add_widget(Label(text="100"))
        self.money_enter.add_widget(Label(text="200"))
        self.money_enter.add_widget(Label(text="500"))

        # Inputs for 100, 200, 500 costs:
        # cost 100
        self.costs_input[6] = TextInput(multiline=False)
        self.money_enter.add_widget(self.costs_input[6])
        # cost 200
        self.costs_input[7] = TextInput(multiline=False)
        self.money_enter.add_widget(self.costs_input[7])
        # cost 500
        self.costs_input[8] = TextInput(multiline=False)
        self.money_enter.add_widget(self.costs_input[8])

        # Labels for 1000, 2000, 5000 costs:
        self.money_enter.add_widget(Label(text="1000"))
        self.money_enter.add_widget(Label(text="2000"))
        self.money_enter.add_widget(Label(text="5000"))

        # Inputs for 1000, 2000, 5000 costs:
        # cost 1000
        self.costs_input[9] = TextInput(multiline=False)
        self.money_enter.add_widget(self.costs_input[9])
        # cost 2000
        self.costs_input[10] = TextInput(multiline=False)
        self.money_enter.add_widget(self.costs_input[10])
        # cost 5000
        self.costs_input[11] = TextInput(multiline=False)
        self.money_enter.add_widget(self.costs_input[11])

        # Set all widgets state to zero.
        self.make_input_to_zero()
        self.add_widget(self.money_enter)

        # Create result label
        self.result_lbl = Label(text="Result:\n\n {:10d}".format(self.result), font_size=36)
        self.add_widget(self.result_lbl)

        # Create submit button
        self.submit_btn = Button(text="Submit",
                                 font_size=36,
                                 size_hint_y=None,
                                 height=200
                                 )
        self.add_widget(self.submit_btn)
        self.submit_btn.bind(on_press=self.count_result)

    def make_input_to_zero(self):
        """
        This function set all of TextInput widgets to zero.
        It's need to make default state.
        :return:
        """
        for i in range(12):
            self.costs_input[i].text = "0"

    def count_result(self, instance):
        """
        Count and output result.
        :return:
        """
        count = [int(self.costs_input[i].text) for i in range(12)]
        cost = [1, 3, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
        for i, j in zip(cost, count):
            self.result += i * j

        self.result_lbl.text = "Result:\n\n {:10d}".format(self.result)
        self.result = 0
        self.make_input_to_zero()


class MyApp(App):
    def build(self):
        return AppGridLayout()


if __name__ == "__main__":
    MyApp().run()