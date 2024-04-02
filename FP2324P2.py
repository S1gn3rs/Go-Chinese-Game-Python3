"""Projeto de fundamentos da programação "Go" 2023/24

O objetivo deste projeto é escrever um programa em Python que permita jogar ao
Go. Assim, foram definidos um conjunto de tipos abstratos de dados que são
utilizados para manipular a informação necessária no decorrer do jogo,
bem como um conjunto de funções adicionais.
"""

__author__ = "ist1106823 Guilherme Silva"
__version__ = "0.1"

def cria_intersecao(col, lin):
    """Cria uma interseção do goban com a coluna e a linha recebida

    Recebe uma coluna com uma letra (caractér) maiúscula de "A" até "S" e um
    número de 1 a 19 e confere se os argumentos são válidos, retornando a
    interseção se assim o forem e levantando um erro caso não sejam.

    :param col (str): possível representação da coluna
    :param lin (int): possível representação da linha
    :raise (ValueError): se a coluna ou a linha forem inválidos
    :return (intersecao): representação interna da interseção
    """
    if type(col) == str and len(col) == 1 and 65 <= ord(col) <= 83 and\
    type(lin) == int and 1 <= lin <= 19: #ord("A")->65 ord("S")->83
        return (col, lin)

    raise ValueError("cria_intersecao: argumentos invalidos")


def obtem_col(intersec):
    """Devolve a coluna da interseção recebida

    Recebe uma interseção e devolve a letra que pode estar entre 'A' e 'S' que
    representa a coluna da interseção.

    :param intersec (intersecao): representação interna de interseção
    :return (str): coluna da interseção recebida
    """
    return intersec[0]


def obtem_lin(intersec):
    """Devolve a linha da interseção recebida

    Recebe uma interseção e devolve o número que pode estar entre 1 e 19 que
    representa a linha da interseção.

    :param intersec (intersecao): representação interna de interseção
    :return (int): linha da interseção recebida
    """
    return intersec[1]


def eh_intersecao(intersec):
    """Verifica se o argumento é uma interseção

    O argumento é interseção se possuir apenas com dois elementos, o
    primeiro uma letra de A a S e o segundo um número de 1 a 19, sendo que
    as letras representam as colunas e os números as linhas.

    :param intersec (universal): representação interna de possível interseção
    :return (bool): True se for interceção e False caso contrário
    """
    if type(intersec) == tuple and len(intersec) == 2:
        col = obtem_col(intersec)
        lin = obtem_lin(intersec)
        #ord("A")->65 ord("S")->83
        return type(col) == str and len(col) == 1 and 65 <= ord(col) <= 83 and\
            type(lin) == int and 0 < lin < 20 #verificação de colunas e linhas

    return False


def intersecoes_iguais(intersecOne, intersecTwo):
    """Avalia se ambas as interseções recebidas são iguais

    Recebe duas interseções e vai devolver True se estas forem válidas e se
    ambas forem a representação interna da mesma interseção (mesma coluna e
    mesma linha) e False caso contrário.

    :param intersecOne (universal): representação interna de possível interseção
    :param intersecTwo (universal): repr. interna de outra possível interseção
    :return (bool): True se forem interseções iguais e False caso contrário
    """
    if eh_intersecao(intersecOne) and eh_intersecao(intersecTwo):
        return intersecOne[0] == intersecTwo[0] and\
            intersecOne [1] == intersecTwo[1] # intersecao = (coluna, linha)


def intersecao_para_str(intersec):
    """Recebe uma interseção e devolve a sua representação externa

    Ao receber a interseção devolve a cadeia de caracteres formada pela letra da
    coluna e o número da linha da interseção, ou seja, a representação externa
    da interseção.

    :param intersec (intersecao): representação interna de interseção
    :return (str): representação externa da interseção
    """
    return f"{intersec[0]}{intersec[1]}" # intersecao = (coluna, linha)


def str_para_intersecao(strIntersec):
    """Recebe um string que representa uma interseção e devolve essa interseção

    Ao receber uma representação externa da interseção vai transformá-la numa
    representação interna da interseção, o primeiro elemento da cadeia de
    caracteres é a a coluna e os restantes são a linha da interseção.

    :param strIntersec (str): representação externa de interseção
    :return (intersecao): representação interna da interseção
    """
    return cria_intersecao(strIntersec[0], int(strIntersec[1:]))


def obtem_intersecoes_adjacentes(intersec, lastIntersec):
    """Devolve o tuplo ordenado das interseções adjacentes à interseção

    Ao receber a interseção e a última interseção do goban vai ser devolvido um
    tuplo com as interseções adjacentes ordenadas que podem ir de 0 a 4
    dependendo do posição da última interseção e da posição da inters. recebida.

    :param intersec (intersecao): representação interna de interseção
    :param lastIntersec (intersecao): representação interna da última interseção
    :return (tuple): interseções ajacentes à interceção recebida ordenadas
    """
    adjaTuple = () #tuplo que guarda as intersec adjacentes por ordem
    col, lin = obtem_col(intersec), obtem_lin(intersec)
    lastCol, lastLin = obtem_col(lastIntersec), obtem_lin(lastIntersec)

    if lin > 1: #intersec em baixo
        adjaTuple += (cria_intersecao(col, lin - 1),)

    if ord(col) > 65: # ord(A) -> 65, intersec à esquerda
        adjaTuple += (cria_intersecao(chr(ord(col) - 1),lin),)

    if ord(col) < ord(lastCol): # intersec à direita
        adjaTuple += (cria_intersecao(chr(ord(col) + 1),lin),)

    if lin < lastLin: # intersec em cima
        adjaTuple += (cria_intersecao(col, lin + 1),)

    return adjaTuple


def ordena_intersecoes(intersTuple):
    """Recebe um tuplo com um conjunto de interseções e ordena-as

    Ao receber um tuplo de interseções vai ordená-las tomando o valor númerico
    do menor para o maior das linhas e em caso de igual valor númerico organiza
    por ordem alfabética das colunas.

    :param intersTuple (tuple): conjunto das interseções a ordenar
    :return (tuple): conjunto das interseções já ordenado
    """
    return tuple(sorted(intersTuple, key = lambda inters:\
        (obtem_lin(inters), obtem_col(inters)) ))
        #Ordena 1º pelo num. da linha e em caso de igual pela letra das colunas


def cria_pedra_branca():
    """Cria uma pedra que pertence ao jogador branco

    Sem receber argumentos cria uma pedra que pertence ao jogador branco
    devolvendo a representação interna da pedra.

    :return (pedra): representação interna da pedra do jogador branco
    """
    return {"player": "O"}


def cria_pedra_preta():
    """Cria uma pedra que pertence ao jogador preto

    Sem receber argumentos cria uma pedra que pertence ao jogador preto
    devolvendo a representação interna da pedra.

    :return (pedra): representação interna da pedra do jogador preto
    """
    return {"player": "X"}


def cria_pedra_neutra():
    """Cria uma pedra que não pertence a nenhum jogador (pedra neutra)

    Sem receber argumentos cria uma pedra que não pertence a nenhum jogador
    devolvendo a representação interna da pedra.

    :return (pedra): representação interna da pedra neutra
    """
    return {"player": "."}


def eh_pedra(stone):
    """Verifica se o argumento é uma pedra

    O argumento é uma pedra se a sua representação interna condizer com a
    representaçáo interna de uma pedra neutra ou de uma pedra do jogador
    branco ou preto, caso seja devolve True e caso contrário devolve False

    :param stone (universal): representação interna de possível pedra
    :return (bool): True se for pedra e False caso contrário
    """
    return type(stone) == dict and len(stone) == 1 and\
        "player" in stone and stone["player"] in (".", "O", "X")
        # pedra = {"player": "." ou "O" ou "X"}


def eh_pedra_branca(stone):
    """Verifica se o argumento é uma pedra do jogador branco

    A pedra é do jogador branco se a sua representação interna condizer com a
    representaçáo interna de uma pedra do jogador branco, caso
    seja devolve True e caso contrário devolve False.

    :param stone (pedra): represent. interna de possível pedra do jogador branco
    :return (bool): True se for pedra do jogador branco e False caso contrário
    """
    return stone["player"] == "O"


def eh_pedra_preta(stone):
    """Verifica se o argumento é uma pedra do jogador preto

    A pedra é do jogador preto se a sua representação interna condizer com a
    representaçáo interna de uma pedra do jogador preto, caso
    seja devolve True e caso contrário devolve False

    :param stone (pedra): represent. interna de possível pedra do jogador preto
    :return (bool): True se for pedra do jogador preto e False caso contrário
    """
    return stone["player"] == "X"


def pedras_iguais(stoneOne, stoneTwo):
    """Avalia se ambas as pedras recebidas são iguais

    Recebe duas pedras e se estas forem válidas e se ambas forem a representação
    da mesma pedra (mesmo jogador) vai devolver True e False caso contrário.

    :param stoneOne (universal): representação interna de uma pedra
    :param stoneTwo (universal): representação interna de outra pedra
    :return (bool): True se forem pedras iguais e False caso contrário
    """
    return eh_pedra(stoneOne) and eh_pedra(stoneTwo) and\
        stoneOne["player"] == stoneTwo["player"]
        # pedra = {"player": "." ou "O" ou "X"}


def pedra_para_str(stone):
    """Recebe uma pedra e devolve a representação externa do dono da pedra

    Ao receber a pedra devolve o caracter cuja representação externa é o dono
    da pedra, se é neutra ('.'), se é o jogador branco ('O') ou se é o jogador
    preto ('X')

    :param stone (pedra): representação interna de pedra
    :return (str): representação externa do dono da pedra
    """
    return stone["player"] # pedra = {"player": "." ou "O" ou "X"}


def eh_pedra_jogador(stone):
    """Verifica se a pedra pertence a algum jogador

    Recebe uma pedra e verifica se a pedra não é neutra, ou seja, se pertence
    ao jogador branco ou se pertence ao jogador preto e devolve True caso
    pertença e False caso contrário.

    :param stone (pedra): representação interna de pedra
    :return (bool): True se pertencer a um jogador e False caso contrário
    """
    return eh_pedra_branca(stone) or eh_pedra_preta(stone)


def cria_goban_vazio(sizeN):
    """Cria um goban n X n sem interseções ocupadas

    Recebe um n que representa a dimensão do goban e que deve de corresponder
    a 9, 13 ou 19. Se o argumento for inválido gera erro e se for válido cria
    um goban vazio dessa dimensão e devolve a representação interna do mesmo.

    :param sizeN (int): representação de dimensão do goban
    :raise (ValueError): se a dimensão do goban for inválida
    :return (goban): representação interna do goban vazio
    """
    if type(sizeN) != int or sizeN not in {9, 13, 19}:
        raise ValueError("cria_goban_vazio: argumento invalido")

    gob = []
    for sumToCol in range(sizeN): # para ir de 'A' até à letra final
        col = chr(65 + sumToCol) #chr(65) = 'A'
        gob += [[]]

        for lin in range(1, sizeN + 1):
            gob[sumToCol] += [[cria_intersecao(col, lin),cria_pedra_neutra()]]
            #gob = [ [ [inteseção, pedra], ...], ...]

    return gob


def cria_goban(sizeN, interWhite, interBlack):
    """Cria um goban n X n com as interseções ocupadas por pedras dos jogadores

    Recebe um n, a dimensão do goban (9, 13 ou 19), e dois tuplos com as inters.
    ocupadas. Se os arg. forem inválido gera erro se forem válidos cria um goban
    dessa dim. e com essas inters. ocupadas e devolve a repr. interna do mesmo.

    :param sizeN (int): representação de dimensão do goban
    :param interWhite(tuple): interseções ocupadas por pedras brancas
    :param interBlack(tuple): interseções ocupadas por pedras pretas
    :raise (ValueError): se a dimensão do goban ou as inters. forem inválido
    :return (goban): representação interna do goban vazio
    """
    def adiciona_intersecoes_ocupadas_aux(gob, interTuple, newStone):
        """Func. aux que coloca a pedra na interseção livre

        Recebe o goban, um tuplo com as interceções que devem de ter a pedra, se
        o goban não tiver na interseção do tuplo uma pedra neutra (nenhum
        jogador tem uma pedra lá) coloca-a ou caso contrário gera erro.

        :param gob (goban): representação interna de um goban
        :param interTuple (tuple): interseções ocupadas por um tipo de pedra
        :param newStone (pedra): repr. interna da pedra das inters. do tuplo
        :raise (ValueError): se as inters. já possuirem pedra de jogador
        """
        for intersec in interTuple:
            if not eh_intersecao(intersec) or\
                not eh_intersecao_valida(gob,intersec) or\
                    eh_pedra_jogador(obtem_pedra(gob, intersec)):
            # Vê se cada inters. é válida e se o goban não tem já pedra de jog.
                raise ValueError("cria_goban: argumentos invalidos")

            indexCol, indexLin = indices_goban_aux(intersec)
            #gob[indexCol][indexLin] = [interseção, pedra]
            gob[indexCol][indexLin][1] = newStone
    #se sizeN não for válido gera erro
    if type(sizeN) != int or sizeN not in {9, 13, 19}:
        raise ValueError("cria_goban: argumentos invalidos")

    gob = cria_goban_vazio(sizeN)
    if not type(interWhite) == tuple or not type(interBlack) == tuple:
        raise ValueError("cria_goban: argumentos invalidos")

    newStone = cria_pedra_branca() #vai adicionar as pedras brancas nas inters.
    adiciona_intersecoes_ocupadas_aux(gob, interWhite, newStone)
    newStone = cria_pedra_preta() #vai adicionar as pedras pretas nas inters.
    adiciona_intersecoes_ocupadas_aux(gob, interBlack, newStone)

    return gob


def cria_copia_goban(gob):
    """Recebe um goban e devolve uma cópia do goban recebido

    Ao receber um goban vai returnar uma cópia desse mesmo goban, totalmente
    igual (cópia profunda), não tendo ligação ao goban copiado.

    :param gob (goban): representação interna de goban
    :return (goban): representação interna do goban copiado
    """
    sizeN = len(gob)
    gobCopy = cria_goban_vazio(sizeN)

    for indexCol in range(sizeN):
        for indexLin in range(sizeN):
            #gob[indexCol][indexLin] = [interseção, pedra]
            if eh_pedra_jogador(gob[indexCol][indexLin][1]):
                if eh_pedra_branca(gob[indexCol][indexLin][1]):
                    gobCopy[indexCol][indexLin][1] = cria_pedra_branca()

                else:
                    gobCopy[indexCol][indexLin][1] = cria_pedra_preta()

    return gobCopy


def obtem_ultima_intersecao(gob):
    """Devolve a interseção do canto superior direito do goban

    Recebe um goban e vai devolver a última interseção do goban recebido,
    ou seja, a interseção do canto superior direito.

    :argum gob (goban): representação interna de goban
    :return (intersecao): representação interna da últina interseção
    """
    return gob[-1][-1][0] #gob[indexCol][indexLin] = [interseção, pedra]


def obtem_pedra(gob, intersec):
    """Devolve a pedra associada à interseção no goban

    Recebe um goban e uma interseção e vai devolver a pedra associada à
    interseção no goban. A pedra pode ser neutra ou de um dos jogadores.

    :argum goban (goban): representação interna de goban
    :argum intersec (intersecao): representação interna de uma interseção
    :return (pedra): representação interna da pedra associada à interseção
    """
    indexCol, indexLin = indices_goban_aux(intersec)
    return gob[indexCol][indexLin][1] #gob[indexCol][indexLin]=[inters., pedra]


def obtem_cadeia(gob, intersec):
    """Devolve a cadeia de pedras a que a interseção pertence no goban

    Ao receber um goban e interseção, determina a pedra da interseção e devolve
    a cadeia de interseções ligadas entre si no goban e com o mesmo tipo de
    pedra num tuplo ordenado de interseções.

    :param gob (goban): representação interna de goban
    :param intersec (intersecao): representação interna de interseção
    :return (tuple): cadeia de interseções ordenadas
    """
    def adiciona_na_cadeia_aux(chain, intersec):
        """Função aux. que adiciona à cadeia as suas interseções

        Recebe uma cadeia e uma interseção, onde a vai adicionar à cadeia e ver
        as inters. adjacentes à inters. recebida caso contenham a mesma pedra e
        não pertenção ainda à cadeia vai adicioná-las.

        :param chain (list): representação da cadeia incompleta/completa
        :param intersec (intersecao): representação interna de interseção
        """
        chain += [intersec]
        for availInters in obtem_intersecoes_adjacentes(intersec, lastInters):
            if obtem_pedra(gob, availInters) == stone and\
                availInters not in chain:

                adiciona_na_cadeia_aux(chain, availInters) #até complet. a cad.


    lastInters = obtem_ultima_intersecao(gob)
    stone = obtem_pedra(gob, intersec)
    chain = []
    adiciona_na_cadeia_aux(chain, intersec) #Vai adi. todas as inters. da cadeia
    chain = ordena_intersecoes(tuple(chain)) # Argumento tem que ser tuplo
    return chain


def coloca_pedra(gob, intersec, stone):
    """Coloca a pedra recebina na interseção do goban

    Receve um goban, uma interseção e uma pedra, e modifica destrutivamente o
    goban colocando a pedra do jogador na interseção e devolve o goban alterado.

    :param gob (goban): representação interna de goban
    :param intersec (intersecao): representação interna de interseção
    :param stone (pedra): representação interna de pedra
    :return (goban): repres. interna do goban modificado com a pedra na inters.
    """
    indexCol, indexLin = indices_goban_aux(intersec)
    gob[indexCol][indexLin][1] = stone #gob[indexCol][indexLin]=[inters., pedra]
    return gob


def remove_pedra(gob, intersec):
    """Remove a pedra da interseção do goban

    Receve um goban e uma interseção, e modifica destrutivamente o goban
    removendo a pedra do jogador na interseção e devolve o goban alterado.

    :param gob (goban): representação interna de goban
    :param intersec (intersecao): representação interna de interseção
    :return (goban): repres. interna do goban modificado sem a pedra na inters.
    """
    indexCol, indexLin = indices_goban_aux(intersec)
    #gob[indexCol][indexLin]=[inters., pedra]
    gob[indexCol][indexLin][1] = cria_pedra_neutra()
    return gob


def remove_cadeia(gob, interTuple):
    """Remove as pedras da cadeia do goban

    Recebe um goban e uma cadeia (tuplo de interseções) e modifica
    destrutivamente o goban removendo a pedra do jogador nas interseções da
    cadeia e devolve o goban alterado.

    :param gob (goban): representação interna de goban
    :param interTuple (tuple): representação da cadeia (tuplo de interseções)
    :return (goban): goban modificado sem as pedras nas interseções da cadeia
    """
    for intersec in interTuple:
        gob = remove_pedra(gob, intersec) #Coloca no lugar uma pedra neutra
    return gob


def eh_goban(gob):
    """Verifica se o argumento é um goban

    O argumento é um goban se for uma lista de listas(colunas) n x n e se
    cada elemento das colunas for uma lista com a interseção na primeira posição
    e o tipo de pedra na segunda.

    :param gob (universal): representação interna de possível goban
    :return (bool): True se for goban e False caso contrário
    """
    #gob = [ [ [inteseção, pedra], ...], ...]

    if not type(gob) == list or len(gob) not in {9,13,19}: #len(gob)=n gob é nxn
        return False

    lenGob = len(gob) #quantidade de colunas
    for indexCol in range(lenGob):
        if not type(gob[indexCol]) == list and len(gob[indexCol]) != lenGob:
            #Se quantidade de colunas != linhas
            return False

        for indexLin in range(lenGob): #porque quantidade de colunas = linhas
            interStone = gob[indexCol][indexLin]
            # interStone deve de ser = [interseção, pedra]
            if not type(interStone) == list or len(interStone) != 2 or\
                not eh_intersecao(interStone[0]) or not eh_pedra(interStone[1]):

                return False
            #Para confirmar que as interseções estão nas posições corretas
            intersIndCol, intersIndLin = indices_goban_aux(interStone[0])
            if intersIndCol != indexCol or intersIndLin != indexLin:
                return False

    return True


def eh_intersecao_valida(gob, intersec):
    """Verifica se a interseção pertence ao goban (se é válida)

    Verifica se a interação está dentro do goban comparando os elementos da
    interseção com os elementos da última interseção do goban, sendo que os
    valores da interseção têm de ser menores ou iguais à última interseção.

    :param gob (goban): representação interna de goban
    :param intersec (intersecao): representação interna de interseção
    :return (bool): True se for interceção do goban e False caso contrário
    """
    col, lin = obtem_col(intersec), obtem_lin(intersec)
    lastInters = obtem_ultima_intersecao(gob)
    lastCol, lastLin = obtem_col(lastInters), obtem_lin(lastInters)
    return col <= lastCol and lin <= lastLin #têm que ser ambas menores ou igua.


def gobans_iguais(gobOne, gobTwo):
    """Avalia se ambos os gobans recebidos são válidos e se são iguais

    Recebe dois gobans e se estas forem válidas e se ambos forem a representação
    interna do mesmo goban vai devolver True e False caso contrário.

    :param gobOne (universal): representação interna de um goban
    :param gobTwo (universal): representação interna de outro goban
    :return (bool): True se forem iguais e False caso contrário
    """
    if eh_goban(gobOne) and eh_goban(gobTwo):
        sizeN = len(gobOne)
        if sizeN == len(gobTwo):
            for indexCol in range(sizeN):
                for indexLIn in range(sizeN):
                    #gob[indexCol][indexLin]=[inters., pedra]
                    if not pedras_iguais(gobOne[indexCol][indexLIn][1],\
                        gobTwo[indexCol][indexLIn][1]):

                        return False

            return True

    return False


def goban_para_str(gob):
    """Recebe um goban e devolve a string que o representa

    Recebe um goban e vai representá-lo na forma de uma cadeia de caracteres
    de maneira a ser possível depois a visualização do mesmo através de uma
    "tabela", ou seja, na representação externa.

    :param gob (goban): representação interna de goban
    :return (str): cadeia de caracteres que representa o goban (repr. externa)
    """
    def adiciona_letras_aux(strGob):
        """Função aux. que introduz as letras à string do goban

        Ao receber a cadeia de caracteres do goban vai adicionar as letras que
        representam cada coluna desde 'A' até à letra da última interseção do
        goban (última coluna do goban).

        :param strGob (str): representação da cadeia de caracteres do goban
        :return (str): cadeia de caracteres intermédia que representa o goban
        """
        strElem = "A"
        strGob += "  "
        #adiciona-se 2 espaços para que as letras fiquem bem posicionadas
        while strElem <= lastCol: #'A' até última letra do território
            strGob += f" {strElem}"
            strElem = chr(ord(strElem) + 1)

        return strGob

    def adiciona_numeros_inters_aux(strGob):
        """Função aux. que introduz os números e as pedras à string do Goban

        Ao receber a cadeia de caracteres do goban vai adicionar os números do
        maior para o menor onde cada um é uma linha do goban e as pedras das
        interseções que se encontram nessa linha.

        :param strGonb (str): representação da cadeia de caracteres do goban
        :return (str): cadeia de caracteres intermédia que representa o goban
        """
        strElem = lastLin # começa do maior para o menor

        for indexLin in range(lastLin): #número de linhas
            if strElem < 10: #para que continue enquadrada
                strGob += f"\n {strElem}"
            else:
                strGob += f"\n{strElem}"

            #quantidade de linhas = quantidade de colunas
            for indexCol in range(lastLin):
                stone = gob[indexCol][-indexLin -1][1] #começa na maior linha
                strGob += f" {pedra_para_str(stone)}"

            if strElem < 10: #para que continue enquadrada
                strGob += f"  {strElem}"
            else:
                strGob += f" {strElem}"

            strElem -= 1 # Número da linha que decrementa

        strGob += "\n"
        return strGob


    lastCol = obtem_col(obtem_ultima_intersecao(gob))# limite das interseções
    lastLin = obtem_lin(obtem_ultima_intersecao(gob))
    strGob = ""
    strGob = adiciona_letras_aux(strGob)
    strGob = adiciona_numeros_inters_aux(strGob)
    strGob = adiciona_letras_aux(strGob)

    return strGob


def obtem_territorios(gob):
    """Devolve um tuplo de tuplos com as inters. dos territ. do goban ordenados

    Ao receber um goban vai procurar as interseções livres (pedra neutra) e
    devolver um tuplo ordenado com as cadeias ordenadas de todos os
    territórios do goban.

    :param gob (goban): representação interna de goban
    :return (tuple): conjunto ordenado dos territórios do goban
    """
    seenIntersec = set() #set para ser mais eficiente a procura
    allTerrit = ()
    sizeN = obtem_lin(obtem_ultima_intersecao(gob)) # n x n -> n = num de linhas

    for indexLin in range(sizeN): #Primeiro vê linha inteira da menor à maior
        for indexCol in range(sizeN): #Territ. a adicion. já vão estar por ordem

            intersec = cria_intersecao(chr(65 + indexCol), 1 + indexLin)
            if intersec not in seenIntersec: #para não reavaliar interseções
                chain = obtem_cadeia(gob, intersec)

                if not eh_pedra_jogador(obtem_pedra(gob, intersec)):
                    allTerrit += (chain,) # tem que ser cadeias de pedra neutra

                for intersec in chain: # adiciona todas as inters da cadeia
                    seenIntersec.add(intersec)

    return allTerrit


def obtem_adjacentes_diferentes(gob, interTuple):
    """Devolve um tuplo com as inters. adjacentes e dif. às inters. recebidas

    Ao receber um tuplo de interseções e um goban, vai procurar as interseções
    adjacentes a cada uma delas e se tiverem pedra de jogador devolve as
    adjacentes ordenadas com pedra neutra e vice versa.

    :param gob (goban): representação interna de goban
    :param interTuple (tuple): representação de conjunto de interseções (cadeia)
    :return (tuple): conjunto ordenado de interseções adjacentes e diferentes
    """

    def adiciona_adjacentes_diferentes_aux(interTuple, adjaDifInter):
        """Função aux. que adic. as inters. adjac. e dif. ao conjunto das mesmas

        Recebe um tuplo de inters. e um set de inters. adjac. e dif. e caso as
        inter. adjac. das inter. do tuplo sejam diferet. e ainda não estejam no
        set adiciona-as e devolve no fim o tuplo ord. das inter. adjac. e dif.

        :param interTuple (tuple): repr. de conjunto de interseções (cadeia)
        :param adjaDifInter (set): repr. de conj. ordenado de inter. adj. e dif.
        :param return (tuple): conj. ordenado de inters. adjacentes e diferentes
        """
        if interTuple == (): #caso base
            return ordena_intersecoes(tuple(adjaDifInter))

        for intersec in obtem_intersecoes_adjacentes(interTuple[0], lastInters):

            if not eh_pedra_jogador(stone) ==\
                eh_pedra_jogador(obtem_pedra(gob, intersec)) and\
                    intersec not in adjaDifInter:
            #se pedra é neutra as adj têm que ser de jogadores e vice versa
                adjaDifInter.add(intersec)

        return adiciona_adjacentes_diferentes_aux(interTuple[1:], adjaDifInter)


    lastInters = obtem_ultima_intersecao(gob) #para as interseções adjacentes
    stone = obtem_pedra(gob, interTuple[0]) #para comparar com as nas adjacentes
    return adiciona_adjacentes_diferentes_aux(interTuple, set())


def jogada(gob, intersec, stone):
    """Coloca a pedra na inter. do goban e retira cadeia caso perca liberdade

    Recebe um goban, uma inter. e uma pedra e modifica destrutivamente o goban
    colocando a pedra do jogador na inter. e remove todas as pedras do jogador
    contrário pertencentes a cadeias adjacentes sem liberdade e devolve o goban

    :param gob (goban): representação interna de goban
    :param intersec (intersecao): representação interna de interseção
    :param stone (pedra): representação interna de pedra
    :return (goban): repr. interna de goban modificado com a pedra na interseção
    """

    gob = coloca_pedra(gob, intersec, stone)
    adjaInter = obtem_intersecoes_adjacentes(intersec,\
        obtem_ultima_intersecao(gob))

    for inter in adjaInter:
        adjIntStone = obtem_pedra(gob, inter)
        if eh_pedra_jogador(adjIntStone): #para excluir as que têm pedra neutra
            #vê as pedras do outro jogador para ver se perderam liberdade
            if not pedras_iguais(adjIntStone, stone):
                chain = obtem_cadeia(gob, inter)

                if not obtem_adjacentes_diferentes(gob, chain): #Sem liberdade
                    gob = remove_cadeia(gob, chain)

    return gob


def obtem_pedras_jogadores(gob):
    """Recebe um goban e devolve a quantidade de pedras de cada jogador

    Ao receber um goban vai contar a quantidade de pedras de cada jogador,
    o jogador branco e o jogador preto, e vai devolver um tuplo com a quantidade
    pedras do jogador branco e do jogador preto respetivamente.

    :param gob (goban): representação interna de goban
    :return (tuple): número de pedras do jogador branco e preto respetivamente
    """
    countWhite = countBlack = 0
    sizeN = obtem_lin(obtem_ultima_intersecao(gob)) #n x n -> n = num de linhas
    for indexCol in range(sizeN):
        for indexLin in range(sizeN):
            # ord('A') = 65
            intersec = cria_intersecao(chr(65 + indexCol), 1 + indexLin)
            stone = obtem_pedra(gob, intersec) #pedra de cada interseção

            if eh_pedra_jogador(stone): #para não contar com as pedras neutras
                if eh_pedra_preta(stone):
                    countBlack += 1
                else:
                    countWhite += 1

    return (countWhite, countBlack)


def calcula_pontos(gob):
    """Função auxiliar que calcula a pontuação de cada jogador

    Ao receber um goban, vai calcular os pontos dos dois jogador e devolver
    a pontuação do jogador branco e do jogador preto respetivamente num tuplo de
    dois inteiros.

    :param gob (goban): representação interna de goban
    :return (tuple): pontuação do jogador branco e preto respetivamente
    """
    def calcula_territorio_aux(countWhite, countBlack, territory, allTerrit):
        """Func. aux. que calcula a pontuação de todos os territórios

        Recebe os territórios e as pontuações de cada jogador e vê a pontuação
        de cada territ., que pode nem existir se ambos os jogadores tiverem
        uma pedra adj. ao territ., e adiciona a pontuação ao respetivo jogador.

        :param countWhite (int): representação da pontuação do jogador branco
        :param countBlack (int): representação da pontuação do jogador preto
        :param territory (tuple): representação de um território
        :param allTerrit (tuple): representação de todos os territórios
        :return (tuple): pontuação dos territ. do jogador branco e preto respet.
        """
        def eh_pedras_todas_iguais_aux(stone, allStones):
            """Func. aux. que verifica se todas as pedras recebidas são iguais

            Ao receber uma pedra e um conjunto de pedras vai ver se todas as
            pedras são iguais e devolve True se todas forem iguais e False caso
            não o sejam.

            :param stone (pedra): representação interna de pedra
            :param allStones (tuple): conjunto de repr. internas de pedras
            :return(bool): True se forem todas pedras iguais, False caso contr.
            """
            if allStones == ():
                return True
            if not pedras_iguais(stone, allStones[0]):
                return False #Basta apenas uma pedra não ser igual
            return eh_pedras_todas_iguais_aux(allStones[0], allStones[1:])


        frontier = obtem_adjacentes_diferentes(gob, territory)
        #frontier = interseções que formam a fronteira de cada território
        allStones = tuple(map(lambda x: obtem_pedra(gob, x), frontier))
        #transforma cada interseção da fronteira na pedra colocada na mesma
        if eh_pedras_todas_iguais_aux(allStones[0], allStones[1:]):
            if eh_pedra_branca(allStones[0]): #adi. a pontuação no jogador certo
                countWhite += len(territory) #cada pedra neutra dá um ponto
            else:
                countBlack += len(territory)

        if allTerrit == (): #Está no final para poder avaliar o último territ.
            return (countWhite, countBlack)

        return calcula_territorio_aux(countWhite, countBlack,\
            allTerrit[0], allTerrit[1:])


    allTerrit = obtem_territorios(gob)
    countWhite, countBlack = obtem_pedras_jogadores(gob) #pontuação das pedras

    if not( countWhite == 0 and countBlack == 0): #caso o goban esteja vazio
        countWhite, countBlack = calcula_territorio_aux(countWhite, countBlack,\
            allTerrit[0], allTerrit[1:]) # pontuação total (pedras+territórios)

    return (countWhite, countBlack)


def eh_jogada_legal(gobOne, intersec, stone, gobTwo):
    """Func. aux. que que avalia se a jogada é legal ou não.

    Recebe um goban, uma interseção, uma pedra e outro goban (estado anterior),
    se a jogada a realizar for um suicídio, uma repetição do estado anterior ou
    se já lá existir uma pedra de um jogador devolve False e True caso contr.

    :param gobOne (goban): representação interna de goban
    :param intersec (interseção): repersentação interna de interseção
    :param stone (pedra): representação interna de pedra
    :param gobTwo (goban): representação interna de outro goban
    :return (bool): True se a jogada for legal e False se a jogada for ilegal
    """
    if not eh_intersecao(intersec) or not eh_pedra(stone) or\
        not eh_pedra_jogador(stone) or\
            not eh_intersecao_valida(gobOne, intersec) or\
                eh_pedra_jogador(obtem_pedra(gobOne, intersec)):
        #ver se a inter. e a pedra são válidos e ver se já lá há pedra na inter.
        return False

    copyGob = cria_copia_goban(gobOne) #para não alterar o goban e sim a copia
    copyGob = jogada(copyGob, intersec, stone)
    #Se os dois gobans são válidos e iguais ao realizar a jogada é repetição
    if gobans_iguais(copyGob, gobTwo) or\
        obtem_adjacentes_diferentes(copyGob,\
            obtem_cadeia(copyGob, intersec)) == ():
    #Se for uma jogada suícida, na cad. da inters. não vai existir liberdade
        return False

    return True


def turno_jogador(gobOne, stone, gobTwo):
    """Func. aux. que realiza o turno do joga., pode passar ou colocar uma pedra

    Recebe um goban, uma pedra de jogador e outro goban, pede ao jogador para
    passar ou escolher onde quer colocar a pedra e se ele escolher uma
    interseção existente ou válida realiza a jogada.

    :param gobOne (goban): representação interna de um goban
    :param stone (pedra): representação interna de pedra
    :param gobTwo (goban): representação interna de outro goban
    :return (bool): True se o jogador passar e False se ele realizar uma jogada
    """
    print("Escreva uma intersecao ou 'P' para passar ", end = "")
    strIntersec = input(f"[{pedra_para_str(stone)}]:")

    if strIntersec == "P": #Se o jogador passar o turno
        return False

    if eh_str_intercecao_valida_aux(strIntersec):
    #se for a repr. externa de uma interseção
        intersec = str_para_intersecao(strIntersec)

    else: # volta ao início
        return turno_jogador(gobOne, stone, gobTwo)

    if not eh_intersecao_valida(gobOne, intersec) or\
        not eh_jogada_legal(gobOne,intersec, stone, gobTwo):
        #Se não for uma inters do goban ou uma jogada legal volta ao início
        return turno_jogador(gobOne, stone, gobTwo)

    gobOne = jogada(gobOne, intersec, stone) #realização da jogada
    return True


def go(sizeN, interWhite, interBlack):
    """Func. principal que permite jogar o jogo completo Go de dois jogadores

    Recebe um n e dous tuplos de repr. exter. inters. que originam um goban
    (gera erro se os arg. estiverem errados) e realiza o jogo Go onde se o
    jogador branco ganhar devolve True e False se o jogador preto ganhar.

    :param sizeN (int): representação de dimensão do goban
    :param interWhite(tuple): repr. exter. de inters. ocupadas por ped. brancas
    :param interBlack(tuple): repr. exter. de inters. ocupadas por ped. pretas
    :raise (ValueError): se a dimensão do goban ou as inters. forem inválido
    :return (bool): True se as brancas ganharem e False se as pretas ganharem
    """
    def calcula_no_momento_aux():
        """Calcula os pontos no momento e mostra ao jogador a situação do jogo

        Não recebe argumentos. Calcula a pontuação de cada jogador no momento
        e mostra a pontuação e a representação externa do goban aos jogadores,
        devolvendo os pontos do jogador branco e preto respetivamente.

        :return (tuple): pontuação do jogador branco e preto respetivamente
        """
        countWhite, countBlack = calcula_pontos(gobOne) # pontuação dos jogad.
        print(f"Branco (O) tem {countWhite} pontos")
        print(f"Preto (X) tem {countBlack} pontos")
        print(goban_para_str(gobOne))
        return (countWhite, countBlack)


    if type(interBlack) != tuple or type(interWhite) != tuple:
        raise ValueError("go: argumentos invalidos")

    for strIntersec in interWhite + interBlack: #Vê logo os dois conjuntos
        if not eh_str_intercecao_valida_aux(strIntersec):
            raise ValueError("go: argumentos invalidos")

    interWhite = tuple(str_para_intersecao(elem) for elem in interWhite)
    interBlack = tuple(str_para_intersecao(elem) for elem in interBlack)
    try: #se os argumentos estiverem certos não dá erro
        gobOne = cria_goban(sizeN, interWhite, interBlack)
        gobTwo = cria_goban_vazio(sizeN)
    except ValueError:
        raise ValueError("go: argumentos invalidos")

    end = 0 #contador de vezes que se passa a jogada
    stone = cria_pedra_preta() #as pretas jogam primeiro
    while end != 2: #se passarem duas vezes acaba o jogo
        calcula_no_momento_aux() #para apresentantar os pontos em cada momento
        gobCopy = cria_copia_goban(gobOne) # copia para o próximo loop
        if not turno_jogador(gobOne, stone, gobTwo): # joga e diz se passou
            end += 1
        else: #Se não passar o contador de passes volta a 0
            end = 0
        gobTwo = cria_copia_goban(gobCopy)

        if pedras_iguais(stone, cria_pedra_preta()):# altera o turno do jogador
            stone = cria_pedra_branca()
        else:
            stone = cria_pedra_preta()
    #Mostra última pontuação, último goban e guarda os pontos
    countWhite, countBlack = calcula_no_momento_aux()

    if countWhite >= countBlack: # Em caso de empate as brancas ganham
        return True
    return False


def indices_goban_aux(intersec):
    """Func. aux., recebe uma inters. e vai devolver os índices desta num goban

    Ao receber uma interseção vai obter os valores das colunas e das linhas da
    mesma e vai converter esses valores em índices para facilitar a procura
    da interseção no goban do TAD deste projeto

    :param intersec (intersecao): representação interna de interseção
    :return (tuple): indice da coluna e indice da linha da interceção
    """
    indexCol = ord(obtem_col(intersec)) - 65 # odr("A") = 65
    indexLin = obtem_lin(intersec) - 1
    return (indexCol, indexLin)


def eh_str_intercecao_valida_aux(strIntersec):
    """Func. aux. que avalia a possível repr. externa de inters. recebida

    Ao receber uma possível repr. externa de interseção vai avaliar se esta
    representa uma intersec., se for devolve True e caso contrário devolve False

    :param strIntersec (universal): possível repr. externa de interseção
    :return (bool): True se representar uma interseção, False caso contrário
    """
    return type(strIntersec) == str and len(strIntersec) in {2,3} and \
        65 <= ord(strIntersec[0]) <= 83 and strIntersec[1:].isnumeric() and\
            1 <= int(strIntersec[1:]) <= 19 # odr("A") = 65 odr("S") = 83

go(9,(),())