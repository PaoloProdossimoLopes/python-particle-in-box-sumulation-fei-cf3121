from tkinter import *

from core.second import *


def present_second_option_result(master, A2, k2, xp, EouP2):
    main_window = Toplevel(master)
    main_window.title("Resultados")

    a_response = get_a(A2, k2, xp, EouP2)
    b_response = get_b(A2, k2, xp, EouP2)
    c_response = get_c(A2, k2, xp, EouP2)

    Label(main_window, text=f"A) Largura da caixa: {a_response}").pack()
    Label(main_window, text=f"B) Nível quântico da partícula: {b_response}").pack()
    Label(main_window, text=f"C) Probabilidade de encontrar a partícula na posição 𝑥P : {c_response}").pack()