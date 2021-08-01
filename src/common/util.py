""" --------------------------------------------------------------------------------------
   Programa com funcoes auxiliares para os programas que implementam o cliente servidor.
   Objetivo: Fornecer funcoes auxiliares para a geracao de chave utilizando Diffie-Hellman
   Restricoes: Nenhuma

   Autor: Brendon e Marllon.
   Disciplina: Redes II
   Data da ultima atualizacao: 28/07/2021
----------------------------------------------------------------------------------------"""

import random


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def generate_random_prime():
    prime = False
    while not prime:
        p = random.randint(2, 997)
        prime = is_prime(p)
    return p

def power(a, b, m):
    return (pow(a,b)) % m
    