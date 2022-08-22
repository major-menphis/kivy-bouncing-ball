from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Ellipse
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.screenmanager import Screen
from random import randint

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_press_button(self):
        self.add_widget(Ball())

class Ball(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.random_value = randint(1, 15)
        self.ball_size = dp(10)
        self.ball_speed_x = dp(self.random_value)
        self.ball_speed_y = dp(self.random_value)
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1 / 60)

    def on_load(self,*args):
        self.ball.pos = self.center_x - self.ball_size / 2, self.center_y - self.ball_size / 2
    
    def move(self):
        x, y = self.ball.pos
        x += self.ball_speed_x
        y += self.ball_speed_y

        if x > self.width - self.ball_size or x < 0:
            self.ball_speed_x *= -1
        if y > self.height - self.ball_size or y < 0:
            self.ball_speed_y *= -1

        self.ball.pos = (x, y)

    def update(self, dt):
        self.move()

class MainApp(App):
    pass

if __name__ == "__main__":
    MainApp().run()