import math


def get_a(A2, k2, xp, EouP2):
  L2 = (2 / (A2**2))
  L2r = L2 * 1E9
  
  return (L2r)


def get_b(A2, k2, xp, EouP2):
  L2 = (2 / (A2**2))
  n2 = (k2 * L2) / math.pi
  n2 = int(round(n2))
  return (n2)


def get_c(A2, k2, x, EouP2):
  L2 = (2 / (A2**2))
  n2 = (k2 * L2) / math.pi
  n2 = int(round(n2))
  P = (A2**2) * (math.sin(k2 * x * L2)**2)
  return (P)