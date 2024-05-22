from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from functools import partial

class Question:
    def __init__(self, question, options, correct_answer, attempts=1):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.attempts = attempts
        self.answered = False
        self.results = []  # Список для зберігання результатів кожної відповіді


class QuizApp(App):
    def build(self):
        self.window = BoxLayout(orientation='vertical')

        # AnchorLayout для центрування кнопки "Play"
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')

        # Кнопка "Play" з оранжевим кольором
        self.start_button = Button(text="Play", size_hint=(None, None), size=(200, 100), font_size=42, background_color=('#00008B'))
        
        self.start_button.bind(on_press=self.start_quiz)

        anchor_layout.add_widget(self.start_button)
        self.window.add_widget(anchor_layout)

        return self.window

    def start_quiz(self, button):
        self.window.clear_widgets()
        Window.clearcolor = ('#00008B')

        self.questions = [
            Question("What is the capital of France?", ["Paris", "London", "Rome", "Madrid"], "Paris", attempts=2),
            Question("Which planet is known as the Red Planet?", ["Jupiter", "Mars", "Saturn", "Venus"], "Mars",
                     attempts=3),
            Question("Who is the author of 'Romeo and Juliet'?",
                     ["William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain"], "William Shakespeare",
                     attempts=1),
            Question("What is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "Pacific Ocean", attempts=2),
            Question("What is the tallest mountain in the world?", ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"], "Mount Everest", attempts=2),
            Question("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"], "Leonardo da Vinci", attempts=1),
            Question("What is the chemical symbol for water?", ["Wo", "Wt", "Wa", "H2O"], "H2O", attempts=2),
            Question("Which gas is most abundant in the Earth's atmosphere?", ["Oxygen", "Nitrogen", "Carbon dioxide", "Argon"], "Nitrogen", attempts=3),
            Question("Which mammal lays eggs?", ["Platypus", "Kangaroo", "Elephant", "Lion"], "Platypus", attempts=2),
            Question("What is the currency of Japan?", ["Yuan", "Euro", "Dollar", "Yen"], "Yen", attempts=1)
        ]

        self.score = 0
        self.question_index = 0

        self.question_label = Label(text=self.questions[self.question_index].question, color=('white'))  # Білий колір тексту
        
        self.options_buttons = [Button(text=option) for option in
                                self.questions[self.question_index].options]
        for button in self.options_buttons:
            button.bind(on_press=partial(self.check_answer))

        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.question_label)
        for button in self.options_buttons:
            self.layout.add_widget(button)

        self.score_label = Label(text=f'Score: {self.score}', color=('white'))  # Білий колір тексту
        self.layout.add_widget(self.score_label)
        # self.layout.add_widget(self.button_layout)
        self.window.add_widget(self.layout)

    def update_question(self):
        self.question_label.text = self.questions[self.question_index].question
        for button, option in zip(self.options_buttons, self.questions[self.question_index].options):
            button.text = option

    def check_answer(self, button):
        question = self.questions[self.question_index]
        if question.answered or question.attempts <= 0:
            return
        if button:
            selected_answer = button.text
            correct_answer = question.correct_answer
            if selected_answer == correct_answer:
                self.score += 1
                question.results.append(True)  # Додаємо True, якщо відповідь правильна
            else:
                question.attempts -= 1
                question.results.append(False)  # Додаємо False, якщо відповідь неправильна
            question.answered = True
            self.update_score()
            button.unbind(on_press=partial(self.check_answer, button))  # Видалення обробника подій після першого кліку

        # Перевірка на кінець списку питань і відображення результатів
        if self.question_index == len(self.questions) - 1:
            self.show_results()

    def update_score(self):
        self.score_label.text = f'Score: {self.score}'

    def show_results(self):
        # Метод для відображення результатів гри
        result_text = f'Quiz ended!\nYour final score: {self.score}/{len(self.questions)}'
        self.question_label.text = result_text
        for button in self.options_buttons:
            self.layout.remove_widget(button)
        self.button_layout.clear_widgets()

        # Виводимо результати кожної відповіді
        for i, question in enumerate(self.questions):
            result = "Correct" if question.results[-1] else "Incorrect"
            print(f"Question {i + 1}: {result}")

# if name == 'main':
QuizApp().run()