import math


def get_wave_function(L, ni, nf, EouP):
  A = math.sqrt(2 / L)
  Kni = (ni * math.pi) / L
  Knf = (nf * math.pi) / L

  equacao_01 = 'ψ(x)= %.2f * sen(%.2f x)' %(A,Kni)
  equacao_02 = 'ψ(x)= %.2f * sen(%.2f x)' %(A,Knf)

  return (equacao_01, equacao_02)

def get_energia_nivel_quantico(L, ni, nf, EouP):
  h = 6.626E-34
  Px8mL2 = 8 * 1.673E-27 * (L**2)
  Ex8mL2 = 8 * 9.109E-31 * (L**2)
  if (EouP) == 1:
    Eni = ((ni**2) * (h**2)) / Ex8mL2
    Enf = ((nf**2) * (h**2)) / Ex8mL2
  elif (EouP) == 2:
    Eni = ((ni**2) * (h**2)) / Px8mL2
    Enf = ((nf**2) * (h**2)) / Px8mL2
  eVEni = Eni * 6.242E18
  eVEnf = Enf * 6.242E18

  equacao_01 = 'Ei= %.2f j/s - %.2f eV' %(Eni,eVEni)
  equacao_02 = 'Ef= %.2f j/s - %.2f eV' %(Enf,eVEnf)

  return (equacao_01, equacao_02)

def get_c(L, ni, nf, EouP):
  h = 6.626E-34
  Px8mL2 = 8 * 1.673E-27 * (L**2)
  Ex8mL2 = 8 * 9.109E-31 * (L**2)
  if (EouP) == 1:
    Eni = ((ni**2) * (h**2)) / Ex8mL2
    Enf = ((nf**2) * (h**2)) / Ex8mL2
  elif (EouP) == 2:
    Eni = ((ni**2) * (h**2)) / Px8mL2
    Enf = ((nf**2) * (h**2)) / Px8mL2
  eVEni = Eni * 6.242E18
  eVEnf = Enf * 6.242E18
  if eVEni>eVEnf:
    eAbs = eVEni - eVEnf
  else:
    eAbs = eVEnf - eVEni
  λf = (4.136E-15 * 3E8) / eAbs
  f = 3E8 / λf
  return (
    'A energia do foton absorvido é: %f' % eAbs, 
    'O comprimento de onda desse foton é: %f' % λf,
    'A frequencia vale: %.2f' % f
  )

def get_d(L, ni, nf, EouP):
  h = 6.626E-34
  Px8mL2 = 8 * 1.673E-27 * (L**2)
  Ex8mL2 = 8 * 9.109E-31 * (L**2)
  if (EouP) == 1:
    Eni = ((ni**2) * (h**2)) / Ex8mL2
    Enf = ((nf**2) * (h**2)) / Ex8mL2
    m = 9.101E-31
  elif (EouP) == 2:
    Eni = ((ni**2) * (h**2)) / Px8mL2
    Enf = ((nf**2) * (h**2)) / Px8mL2
    m = 1.673E-27
  print('-------')
  vi = math.sqrt((2 * Eni) / m)
  vf = math.sqrt((2 * Enf) / m)
  return (
    'Vi - Velocidade final: %f' % (vi),
    'Vf - Velocidade final: %f' % (vf)
  )

def get_e(L, ni, nf, EouP):
  h = 6.626E-34
  Px8mL2 = 8 * 1.673E-27 * (L**2)
  Ex8mL2 = 8 * 9.109E-31 * (L**2)
  if (EouP) == 1:
    Eni = ((ni**2) * (h**2)) / Ex8mL2
    Enf = ((nf**2) * (h**2)) / Ex8mL2
    m = 9.101E-31
  elif (EouP) == 2:
    Eni = ((ni**2) * (h**2)) / Px8mL2
    Enf = ((nf**2) * (h**2)) / Px8mL2
    m = 1.673E-27
  λpi = h / math.sqrt(2 * m * Eni)
  λpf = h / math.sqrt(2 * m * Enf)
  return (
    'λi: %d' % (λpi),
    'λf: %d' % (λpf)
  )

from scipy.integrate import quad


def probability(a, b, n, L):
    theta_i = n * math.pi * a / L
    theta_f = n * math.pi * b / L

    integrand = lambda theta: (2 * n * math.pi / L) * math.sin(theta)**2

    result, _ = quad(integrand, theta_i, theta_f)
    return result

def get_f(L, ni, nf, EouP, a, b):
  return (
    'probabilidade inicial (percent.): %.2f' % (probability(a, b, ni, L)),
    'probabilidade final (percent.): %.2f' % (probability(a, b, nf, L))
  )
