# Fonction factorielle
# -*- coding:utf-8 -*-
def fac (n):
  f = 1
  i = 1
  while i <= n:
    f = f * i
    i = i + 1
  return f # la valeur retournée
print(fac(6))
