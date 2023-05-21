from tkinter import *

from ui.first_option_result import present_first_option_result


def present_first_option(master):
    window = Toplevel(master)
    window.title("Partícula na caixa")

    def eletron_result_action_handler():
        present_first_option_result(window)
    
    def proton_result_action_handler():
        present_first_option_result(window)

    description_label = Label(window, text="Determinação da função de onda quântica e outros parâmetros")
    description_label.grid(column=0, row=0, padx=10, pady=10)

    box_size_label = Label(window, text="L - Largura da caixa [un]:")
    box_size_label.grid(column=0, row=1, padx=0, pady=10)
    box_size_entry = Entry(window)
    box_size_entry.grid(column=1, row=1, padx=10, pady=10)

    initial_n_label = Label(window, text="ni - N inicial da particula:")
    initial_n_label.grid(column=0, row=2, padx=10, pady=10)
    initial_n_entry = Entry(window)
    initial_n_entry.grid(column=1, row=2, padx=10, pady=10)

    final_n_label = Label(window, text="nf - N final da particula:")
    final_n_label.grid(column=0, row=3, padx=10, pady=10)
    final_n_entry = Entry(window)
    final_n_entry.grid(column=1, row=3, padx=10, pady=10)

    probability_description_label = Label(window, text="Dados para probabilidade (𝑃(𝑎 ≤ 𝑥 ≤ b))")
    probability_description_label.grid(column=0, row=4, padx=0, pady=10)

    final_n_label = Label(window, text="a [un]:")
    final_n_label.grid(column=0, row=5, padx=10, pady=10)
    final_n_entry = Entry(window)
    final_n_entry.grid(column=1, row=5, padx=10, pady=10)

    final_n_label = Label(window, text="b [un]:")
    final_n_label.grid(column=0, row=6, padx=10, pady=10)
    final_n_entry = Entry(window)
    final_n_entry.grid(column=1, row=6, padx=10, pady=10)

    final_n_label = Button(window, text="Elétron", command=eletron_result_action_handler)
    final_n_label.grid(column=0, row=7, padx=0, pady=10)
    final_n_entry = Button(window, text="Próton", command=proton_result_action_handler)
    final_n_entry.grid(column=1, row=7, padx=0, pady=10)