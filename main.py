import tkinter as tk
from tkinter import messagebox

# Функция для выполнения арифметических операций
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = eval(screen.get())
            screen_var.set(value)
        except Exception as e:
            screen_var.set("Ошибка")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

# Создание основного окна
root = tk.Tk()
root.title("Калькулятор")

# Переменная для экрана калькулятора
screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="Arial 20 bold", bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
screen.grid(row=0, column=0, columnspan=4)

# Кнопки калькулятора
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Размещение кнопок в окне
row_val = 1
col_val = 0
for button in buttons:
    btn = tk.Button(root, text=button, font="Arial 20 bold", padx=20, pady=20)
    btn.grid(row=row_val, column=col_val)
    btn.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Запуск основного цикла окна
root.mainloop()
