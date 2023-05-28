from tkinter import *

from core.first import *


def present_first_option_result(master, L, ni, nf, EouP):
    main_window = Toplevel(master)
    main_window.title("Resultados")

    a_response = get_wave_function(L, ni, nf, EouP)
    b_response = get_energia_nivel_quantico(L, ni, nf, EouP)
    c_response = get_c(L, ni, nf, EouP)
    d_response = get_d(L, ni, nf, EouP)
    e_response = get_e(L, ni, nf, EouP)
    f_response = 'resposta f'

    Label(main_window, text=f"A) Função de onda quântica no SI dos dois níveis: {a_response}").pack()
    Label(main_window, text=f"B) Energia do nível quântico inicial (𝐸𝑖) e final (𝐸𝑓): {b_response}").pack()
    Label(main_window, text=f"C) Energia (𝐸𝑓ó𝑡𝑜𝑛), frequência (𝑓) e comprimento (𝜆) de onda do fóton absorvido ou emitido pela partícula na transição entre os níveis: {c_response}").pack()
    Label(main_window, text=f"D) Velocidade (𝑣) da partícula no nível quântico inicial e final: {d_response}").pack()
    Label(main_window, text=f"E) Comprimento de onda de De Broglie (𝜆n) da partícula no nível quântico inicial e final: {e_response}").pack()
    Label(main_window, text=f"f) Probabilidade (𝑃(𝑎 ≤ 𝑥 ≤ 𝑏)) de encontrar a partícula, em %, entre 𝑎 e 𝑏 no nível inicial e final: {f_response}").pack()