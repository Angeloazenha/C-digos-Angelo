# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
import tkinter as tk

class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.questions = questions
        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(root, text="")
        self.question_label.pack()

        self.radio_var = tk.IntVar()
        self.radio_var.set(-1)

        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(root, text="", variable=self.radio_var, value=i)
            self.radio_buttons.append(radio_button)
            radio_button.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.next_button = tk.Button(root, text="Next", state=tk.DISABLED, command=self.next_question)
        self.next_button.pack()

        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            question_text = question_data[0]
            answers = question_data[1:5]
            correct_answer = question_data[5]

            self.question_label.config(text=question_text)
            for i in range(4):
                self.radio_buttons[i].config(text=answers[i])

            self.radio_var.set(-1)

            self.submit_button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.DISABLED)

    def check_answer(self):
        selected_answer = self.radio_var.get()
        correct_answer = self.questions[self.current_question][5]

        if selected_answer == correct_answer - 1:
            self.score += 1

        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        result_text = f"Score: {self.score}/{len(self.questions)}"
        self.question_label.config(text=result_text)
        for radio_button in self.radio_buttons:
            radio_button.pack_forget()
        self.submit_button.pack_forget()
        self.next_button.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quiz App")
    app = QuizApp(root, questions = [
    ["Qual é a capital da França?", "Paris", "Londres", "Berlim", "Roma", 1],
    ["Qual é o resultado de 8 + 5?", "12", "13", "15", "18", 2],
    ["Quem pintou a Mona Lisa?", "Picasso", "Da Vinci", "Van Gogh", "Warhol", 2],
    ["Quanto é 6 multiplicado por 7?", "36", "42", "48", "54", 2],
    ["Qual é o maior planeta do sistema solar?", "Marte", "Saturno", "Júpiter", "Vênus", 3],
    ["Quem escreveu a obra 'Dom Quixote'?", "Machado de Assis", "Miguel de Cervantes", "Jorge Luis Borges", "Gabriel García Márquez", 2],
    ["Qual é a fórmula química da água?", "H2O", "CO2", "NaCl", "CH4", 1],
    ["Quem foi o primeiro presidente dos Estados Unidos?", "George Washington", "Abraham Lincoln", "Thomas Jefferson", "John F. Kennedy", 1],
    ["Qual é o resultado de 4 ao cubo?", "16", "32", "64", "128", 3],
    ["Qual é a capital da Rússia?", "Moscou", "São Petersburgo", "Kiev", "Varsóvia", 1],
    ["Quem descobriu a teoria da relatividade?", "Isaac Newton", "Galileu Galilei", "Albert Einstein", "Nikola Tesla", 3],
    ["Qual é o símbolo químico do ouro?", "Au", "Ag", "Cu", "Fe", 1],
    ["Quem foi o autor da obra 'Romeu e Julieta'?", "William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen", 1],
    ["Qual é a capital do Brasil?", "Rio de Janeiro", "Brasília", "São Paulo", "Salvador", 2],
    ["Qual é o resultado de 9 dividido por 3?", "1", "2", "3", "4", 3],
    ["Quem pintou a obra 'A Noite Estrelada'?", "Leonardo da Vinci", "Michelangelo", "Salvador Dalí", "Vincent van Gogh", 4],
    ["Qual é o maior oceano do mundo?", "Atlântico", "Índico", "Pacífico", "Ártico", 3],
    ["Qual é o resultado de 2 elevado a 8?", "8", "16", "64", "256", 4],
    ["Quem escreveu a obra '1984'?", "George Orwell", "Aldous Huxley", "Ernest Hemingway", "F. Scott Fitzgerald", 1],
    ["Qual é o resultado de 15 menos 7?", "5", "6", "7", "8", 3],
    ["Quem foi o pintor do quadro 'A Última Ceia'?", "Pablo Picasso", "Salvador Dalí", "Michelangelo", "Leonardo da Vinci", 4]
])
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
