import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from data_file import dict_of_tasks, dict_of_description, dict_tasks_to_number
from data_file import dict_of_commands_tasks
from time import sleep
import pyperclip

def generate_output():
    input_matrix = get_input_matrix()
    number_of_task = dict_tasks_to_number[get_name_of_task()]
    if number_of_task == 1:
        diameter, radius = dict_of_commands_tasks[number_of_task](input_matrix)
        soluthion = f"Диаметр графа: {diameter}\n" + f"Радиус графа: {radius}"
        inser_soluthion(soluthion)

    else:
        matrix = dict_of_commands_tasks[number_of_task](input_matrix)
        frame = ', '.join(['{}' for _ in range(len(matrix[0]))])
        frame = ',\n'.join([frame.format(*matrix[i]) for i in range(len(matrix))])
        inser_soluthion(frame)

    #Добавить решение выбранной задачи

def paste_text_into_line():
    copied_text = pyperclip.paste()
    input_text.delete("1.0", "end-1c")
    input_text.insert('insert', copied_text)
    input_text.tag_configure("custom_font", font=("Roboto", 12))
    input_text.tag_add("custom_font", "1.0", "end")


def configure_style(event):
    input_text.tag_configure("custom_font", font=("Roboto", 12))
    input_text.tag_add("custom_font", "1.0", "end")

def make_window():
    window = tk.Tk()
    window.title("Match Solver")

    style = Style(theme="darkly")
    style.configure('.', font=('Roboto', 12))
    style.configure('TLabel', font=('Roboto', 12))

    description_label = ttk.Label(window, text="Выберите режим программы")
    description_label.grid(row=1, column=0, padx=20, pady=10)

    input_text = tk.Text(window, wrap=tk.WORD, width=40, height=10)
    input_text.grid(row=2, column=0, padx=10, pady=10)
    input_text.bind("<Key>", configure_style)


    output_text = tk.Text(window, wrap=tk.WORD, width=40, height=10)
    output_text.grid(row=3, column=0, padx=10, pady=10)

    generate_button = ttk.Button(window, text="Сгенерировать", command=generate_output)
    generate_button.grid(row=4, column=0, padx=10, pady=10)

    button_paste_text = ttk.Button(window, text="Вставить", command=paste_text_into_line)
    button_paste_text.grid(row=4, column=1, padx=10, pady=10)
    return window, input_text, output_text, description_label

def get_input_matrix():
    matrix = input_text.get("1.0", "end-1c")
    symbols = ['[', ']', ' ', '\r']
    while any([symbol in matrix for symbol in symbols]):
        for symbol in symbols:
            while symbol in matrix:
                matrix = matrix.replace(symbol, '')
    matrix = matrix.split('\n')
    while '' in matrix:
        matrix.remove('')
    matrix = [line.rstrip(',') for line in matrix]
    input_matrix = [list(map(int, line.split(','))) for line in matrix]
    return input_matrix

def inser_soluthion(soluthion):
    output_text.delete("1.0", "end-1c")
    output_text.insert('insert', soluthion)
    output_text.tag_configure("custom_font", font=("Roboto", 12))
    output_text.tag_add("custom_font", "1.0", "end")

def make_combobox(dict_of_tasks, window):
    global combobox
    combobox = ttk.Combobox(window, values=[dict_of_tasks[1], dict_of_tasks[2], dict_of_tasks[3], dict_of_tasks[4]])
    combobox.grid(row=0, column=0, padx=30, pady=10)
    combobox.bind("<<ComboboxSelected>>", on_combobox_select)

def on_combobox_select(event):
    selected_item = combobox.get()
    description_label.config(text=f"Выбран вариант: {dict_of_description[selected_item]}")
    #Добавить появление примера в поле для вывода с помощью словаря и атрибут input_data

def get_name_of_task():
    return combobox.get()

def start_window(window):
    window.mainloop()

def start():
    global description_label, input_text, output_text
    window, input_text, output_text, description_label = make_window()
    make_combobox(dict_of_tasks, window)
    start_window(window)
