"""

Este exercício tem duas partes:

    Implemente a função incomodam(n) que devolve uma string contendo
    "incomodam " (a palavra seguida de um espaço) n vezes. Se n não for
    um inteiro estritamente positivo, a função deve devolver uma string
    vazia. Essa função deve ser implementada utilizando recursão.
    Utilizando a função acima, implemente a função elefantes(n) que
    devolve uma string contendo a letra da música "Um elefante incomoda
    muita gente" de 1 até n elefantes. Se n não for maior que 1, a função
    deve devolver uma string vazia. Essa função também deve ser
    implementada utilizando recursão.

Observe que, para um elefante, você deve escrever por extenso e no
singular ("Um elefante..."); para os demais, utilize números e o plural
("2 elefantes...").

Dica: lembre-se que é possível juntar strings com o operador "+".
Lembre-se também que é possível transformar números em strings
com a função str().

Dica: Será que neste caso a base da recursão é diferente de n == 1?

Por exemplo, uma chamada a elefantes(4) deve devolver uma string
contendo:

Um elefante incomoda muita gente
2 elefantes incomodam incomodam muito mais
2 elefantes incomodam muita gente
3 elefantes incomodam incomodam incomodam muito mais
3 elefantes incomodam muita gente
4 elefantes incomodam incomodam incomodam incomodam muito mais

"""

def incomodam(n):
    if n <= 0:
        return ''
    else:
        return 'incomodam ' + incomodam(n-1)


def string(n):
    if n == 2:
        string = 'Um elefante incomoda muita gente\n2 elefantes incomodam incomodam muito mais'
    else:
        string = '\n{0} elefantes incomodam muita gente\n{1} elefantes {2}muito mais'.format(n-1, n, incomodam(n))

    return string



def elefantes(n):

    if n <= 1:
        return ''
    else:
        return elefantes(n-1) + string(n)













