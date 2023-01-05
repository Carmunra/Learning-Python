# -*- coding: utf-8 -*-
"""vetor_ordenado.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FfigtnMee_Kp4Ik90PUbtwki4vusuPfR
"""

import numpy as np

class vetorOrdenado:

  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, dtype=int)

  # O(n)
  def imprime(self):
    if self.ultima_posicao == -1:
      print('O valor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i])

  # O(n)
  def insere(self, valor):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
      return

    posicao = 0
    for i in range(self.ultima_posicao + 1):
      posicao = i
      if self.valores[i] > valor:
        break
      if i == self.ultima_posicao:
        posicao = i + 1

    x = self.ultima_posicao
    while x >= posicao:
      self.valores[x + 1] = self.valores[x]
      x -= 1

    self.valores[posicao] = valor
    self.ultima_posicao += 1

  # O(n)
  def pesquisar(self, valor):
    for i in range(self.ultima_posicao + 1):
      if self.valores[i] > valor:
        return -1
      if self.valores[i] == valor:
        return i
      if i == self.ultima_posicao:
        return -1

    # O(log n)
  def pesquisa_binaria(self, valor):
    limite_inferior = 0
    limite_superior = self.ultima_posicao

    while True:
      posicao_atual = int((limite_inferior + limite_superior) / 2)
      #Se achou na prmiera tentativa
      if self.valores[posicao_atual] == valor:
        return posicao_atual
      #Se não achou
      elif limite_inferior > limite_superior:
        return -1
      #Divida os limites
      else:
        #limite inferior
        if self.valores[posicao_atual] < valor:
          limite_inferior = posicao_atual + 1
        # Limite superior
        else:
          limite_superior = posicao_atual - 1

    """
    for i in range(self.ultima_posicao + 1):
      if self.valores[i] > valor:
        return -1
      if self.valores[i] == valor:
        return i
      if i == self.ultima_posicao:
        return -1
    """

  # O(n)
  def excluir(self, valor):
    posicao = self.pesquisar(valor)
    if posicao == -1:
      return -1
    else:
      for i in range(posicao, self.ultima_posicao):
        self.valores[i] = self.valores[i + 1]

      self.ultima_posicao -= 1

vetor = vetorOrdenado(10)
vetor.imprime()

vetor.insere(6)

vetor.insere(4)
vetor.imprime()

vetor.insere(3)
vetor.insere(5)
vetor.imprime()

vetor.insere(8)
vetor.imprime()

vetor.pesquisar(4)

vetor.pesquisar(2)

vetor.excluir(4)
vetor.imprime()

vetor = vetorOrdenado(10)
vetor.insere(8)
vetor.insere(9)
vetor.insere(1)
vetor.insere(4)
vetor.insere(5)
vetor.insere(6)
vetor.insere(7)
vetor.insere(11)
vetor.insere(13)
vetor.insere(2)
vetor.imprime()

vetor.pesquisa_binaria(7)
vetor.pesquisa_binaria(3)