from tkinter import *

from ui.first_option import present_first_option
from ui.second_option import present_second_option

janela = Tk()
janela.title("Escolha a simulaçao")

def first_simulation_action_handler():
    present_first_option(janela)

def second_simulation_action_handler():
    present_second_option(janela)

final_n_label = Button(janela, text="Simulação 1", command=first_simulation_action_handler)
final_n_label.grid(column=0, row=7, padx=0, pady=10)
final_n_entry = Button(janela, text="Simulação 2", command=second_simulation_action_handler)
final_n_entry.grid(column=1, row=7, padx=0, pady=10)

janela.mainloop()