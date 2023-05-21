from tkinter import *


def present_second_option_result(master):
    main_window = Toplevel(master)
    main_window.title("Resultados")

    a_response = 'resposta a'
    b_response = 'resposta b'
    c_response = 'resposta c'

    Label(main_window, text=f"A) Largura da caixa: {a_response}").pack()
    Label(main_window, text=f"B) Nível quântico da partícula: {b_response}").pack()
    Label(main_window, text=f"C) Probabilidade de encontrar a partícula na posição 𝑥P : {c_response}").pack()