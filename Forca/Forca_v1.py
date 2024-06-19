# JOGO DA FORCA V2.0 - 09/12/2023
# ----------------------------------------------------------------------
import unidecode

quadros = (
    (
        ("  _______"),
        ("  |    !"),
        ("  |     "),
        ("  |     "),
        ("  |     "),
        (" _|___________"),
        ("/__F_O_R_C_A__\\"),
    ),
    (
        ("  _______"),
        ("  |    !"),
        ("  |    O"),
        ("  |     "),
        ("  |     "),
        (" _|___________"),
        ("/__F_O_R_C_A__\\"),
    ),
    (
        ("  _______"),
        ("  |    !"),
        ("  |    O"),
        ("  |    | "),
        ("  |     "),
        (" _|___________"),
        ("/__F_O_R_C_A__\\"),
    ),
    (
        ("  _______"),
        ("  |    !"),
        ("  |    O"),
        ("  |    | "),
        ("  |   / "),
        (" _|___________"),
        ("/__F_O_R_C_A__\\"),
    ),
    (
        ("  _______"),
        ("  |    !"),
        ("  |    O"),
        ("  |    | "),
        ("  |   / \\"),
        (" _|___________"),
        ("/__F_O_R_C_A__\\"),
    ),
    (
        ("  _______"),
        ("  |    !"),
        ("  |    O"),
        ("  |   /| "),
        ("  |   / \\"),
        (" _|___________"),
        ("/__F_O_R_C_A__\\"),
    ),
    (
        ("  _______"),
        ("  |    !"),
        ("  |    O"),
        ("  |   /|\\ "),
        ("  |   / \\"),
        (" _|___________"),
        ("/__F_O_R_C_A__\\"),
    ),
    (
        ("  _______"),
        ("  |    !"),
        ("  |     "),
        ("  |   \O/"),
        ("  |    | "),
        (" _|___/_\\_____"),
        ("/__F_O_R_C_A__\\"),
    ),
)


def imagem_jogo(frame: int) -> None:
    """
    Imprime uma tupla dentro da tupla `quadros`, acessada pelo valor do
    seu index inserido em `frame`
    :param frame: Int usado como valor de index em `quadros`
    :return: Sem retorno
    """
    for quadro in quadros[frame]:
        print(quadro)


def quant_chars(palavra_contar: str) -> int:
    total = 0
    for char in palavra_contar:
        if char == "-":
            total += 0
        else:
            total += 1
    return total


def print_repetido(chave: str) -> None:
    """
    Imprime a mensagem inserida abaixo para avisar o jogador que
    determinada letra já foi escolhida. A mensagem é impressa de acordo
    com o valor de `chave`
    :param chave: Dependendo de seu valor, imprime ou não a mensagem
    :return: Sem retorno
    """
    if chave == 'sim':
        print(f'Você já chutou a letra {trocar}. Mais atenção!')


def input_palavra() -> str:
    """
    Pede um input de palavra para jogo de forca. Caso a palavra contenha
    números, caracteres especiais (exceto '-') o loop segue e a palavra
    é requisitada novamente. Palavras menores que 2 (dois) caracteres
    de extensão não são aceitas
    :return: Valor de input (palavra para o jogo) em uppercase
    """
    while True:
        palavra = input("FORCA - Digite uma palavra: ")
        erro = []
        for letra in palavra:
            if not letra.isdigit() and letra.isalnum() or "-" in letra:
                continue
            else:
                erro.append(letra)

        if erro or len(palavra) <= 2:
            print("Palavra não aceita. Tente outra vez.")
        else:
            break
    return palavra.upper()


# Função para retornar a palavra aceita e deixá-la pronta pro jogo
palavra = input_palavra()
#print(palavra)

# Criar listas: 1. Da palavra; 2. Dos traços; 3. Da palavra sem acentos
lista_palavra = list(palavra)
lista_tracos = []
for traco in lista_palavra:
    if traco == '-':
        lista_tracos.append(traco)
    else:
        lista_tracos.append("_")
lista_palavra_limpa = []
for limpa in lista_palavra:
    lista_palavra_limpa.append(unidecode.unidecode(limpa))
lista_palavra_limpa.append(palavra)


# Contagem de chutes errados
contagem = 0

# Condição para print de aviso de letra repetida - 'sim' para imprimir
aviso = 'não'

# Lista de letras utilizadas
tentativas = []

while lista_tracos != lista_palavra:
    print("\n" * 10)
    imagem_jogo(contagem)
    print()
    for char in lista_tracos:
        print(char, end=" ")
    print()
    print(quant_chars(palavra), "letras")
    print()
    print(*tentativas)
    print_repetido(aviso)

    trocar = input("Chute uma letra ou arrisque a palavra: ")
    trocar = trocar.upper()
    aviso = 'não'

    if trocar in lista_palavra_limpa:
        if len(trocar) < 2:
            # Colocar na lista 'posicoes' o index (todos possíveis) da
            # letra selecionada dentro de 'lista_palavra'
            posicoes = []
            for posicao, procura in enumerate(lista_palavra):
                if unidecode.unidecode(procura) == trocar:
                    posicoes.append(posicao)

            # Comparar indexes de 'posicoes' e 'lista_tracos' e
            # substituir traços de 'lista_tracos' por letras de
            # 'lista_palavra'
            for pos in posicoes:
                for numeritos, letritas in enumerate(lista_tracos):
                    if numeritos == pos:
                        lista_tracos[numeritos] = lista_palavra[numeritos]
        else:
            imagem_jogo(7)
            print('PARABÉNS! Acertou a palavra e venceu com glórias!!!')
            print(palavra)
            break

    else:
        if trocar == "":
            continue
        elif trocar in tentativas:
            aviso = 'sim'
        else:
            contagem += 1
            tentativas.append(trocar)
            if len(trocar) > 2:
                imagem_jogo(6)
                print('ERROU A PALAVRA! Você perdeu o jogo.')
                break
            else:
                if contagem > 5:
                    imagem_jogo(6)
                    print('Você gastou todos os seus palpites. Fim de jogo.')
                    break

else:
    # Fim do 'while loop'; venceu por acertar todos os palpites
    imagem_jogo(contagem)
    print('Você descobriu a palavra e venceu o jogo!')
    print(palavra)
