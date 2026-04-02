from main_flyfood import leitura_matriz
from lerBrasil58 import custoCaminho
import random
import time

def calc_distancia_manhatan(coordenada1, coordenada2):
    return abs(coordenada1[0] - coordenada2[0]) + abs(coordenada1[1] - coordenada2[1])


def criador_matriz(coordenadas):
    pontos = ['R'] + sorted([k for k in coordenadas.keys() if k != 'R'])
    total_pontos = len(pontos)
    matriz = [[0] * total_pontos for _ in range(total_pontos)]

    for i in range(total_pontos):
        for j in range(total_pontos):
            if i != j:
                cidade_I = pontos[i]
                cidade_J = pontos[j]
                coord_i = coordenadas[cidade_I]
                coord_j = coordenadas[cidade_J]
                distancia = calc_distancia_manhatan(coord_i, coord_j)
                matriz[i][j] = distancia

    return pontos, matriz


def conversor_upper_row(matriz):
    dimensao = len(matriz)
    linhas = []
    for k in range(dimensao - 1):
        linha_valores = []
        for j in range(k + 1, dimensao):
            linha_valores.append(str(matriz[k][j]))
        linhas.append(' '.join(linha_valores))
    return linhas


def gerar_tsplib(entradaTXT, saidaTSP):
    coordenadas = leitura_matriz(entradaTXT)
    pontos, matriz_distancia = criador_matriz(coordenadas)
    linhas_upper = conversor_upper_row(matriz_distancia)

    with open(saidaTSP, 'w') as f:
        f.write("NAME: flyfood\n")
        f.write("TYPE: TSP\n")
        f.write("COMMENT: Problema de entrega FlyFood\n")
        f.write(f"DIMENSION: {len(pontos)}\n")
        f.write("EDGE_WEIGHT_TYPE: EXPLICIT\n")
        f.write("EDGE_WEIGHT_FORMAT: UPPER_ROW\n")
        f.write("EDGE_WEIGHT_SECTION\n")
        for linha in linhas_upper:
            f.write(linha + '\n')
    return pontos, matriz_distancia


def ler_tsplib_upper_row(caminho_tsp):
    with open(caminho_tsp, "r") as f:
        linhas = f.readlines()

    N = None
    lendo = False
    upper_rows = []

    for linha in linhas:
        linha = linha.strip()

        if linha.upper().startswith("DIMENSION"):
            N = int(linha.split(":")[1].strip())

        if linha.upper().startswith("EDGE_WEIGHT_SECTION"):
            lendo = True
            continue

        if lendo:
            if linha.upper() == "EOF":
                break
            if linha != "":
                upper_rows.append([int(x) for x in linha.split()])

    matriz = [[0 for _ in range(N)] for _ in range(N)]

    for k in range(N - 1):
        for j, valor in enumerate(upper_rows[k]):
            matriz[k][k + 1 + j] = valor

    for i in range(N):
        for j in range(i + 1, N):
            matriz[j][i] = matriz[i][j]

    return matriz


def matriz_para_dicionario(matriz_lista):
    dicionario = {}
    for i, linha in enumerate(matriz_lista):
        for j, valor in enumerate(linha):
            if i != j:
                dicionario[(i+1, j+1)] = valor
    return dicionario


def custoCaminho(permutacao, dicDistancias):
    soma = 0
    for i in range(len(permutacao)-1):
        soma += dicDistancias[(permutacao[i], permutacao[i+1])]
    soma += dicDistancias[(permutacao[-1], permutacao[0])]
    return soma


def inicializaPopulacao(tamanho, qtdeCidades):
    lista = []
    for _ in range(tamanho):
        individuo = list(range(1, qtdeCidades+1))
        random.shuffle(individuo)
        lista.append(individuo)
    return lista


def calculaAptidao(populacao, dicDistancias):
    return [custoCaminho(ind, dicDistancias) for ind in populacao]



def torneio(pop, apt, k=3):
    selecionados = random.sample(list(zip(pop, apt)), k)
    selecionados.sort(key=lambda x: x[1])
    return selecionados[0][0]


def crossover_OX(pai1, pai2):
    n = len(pai1)
    filho = [None] * n

    a = random.randint(0, n-2)
    b = random.randint(a+1, n-1)

    for i in range(a, b+1):
        filho[i] = pai1[i]

    pos = (b + 1) % n

    for j in range(n):
        gene = pai2[(b+1+j) % n]
        if gene not in filho:
            filho[pos] = gene
            pos = (pos + 1) % n

    return filho


def mutacao_reverse(individuo, prob=0.05):
    if random.random() < prob:
        a = random.randint(0, len(individuo)-2)
        b = random.randint(a+1, len(individuo)-1)
        individuo[a:b+1] = reversed(individuo[a:b+1])
    return individuo


def AG_TSP(dicDistancias, qtdeCidades, geracoes=500, tamPop=100,
           probMut=0.05, torneioK=3):

    populacao = inicializaPopulacao(tamPop, qtdeCidades)
    apt = calculaAptidao(populacao, dicDistancias)

    melhor_global = populacao[apt.index(min(apt))]
    melhor_custo = min(apt)


    for g in range(geracoes):
        nova_pop = []
        nova_pop.append(melhor_global[:])

        while len(nova_pop) < tamPop:
            pai1 = torneio(populacao, apt, torneioK)
            pai2 = torneio(populacao, apt, torneioK)
            filho = crossover_OX(pai1, pai2)
            filho = mutacao_reverse(filho, probMut)
            nova_pop.append(filho)

        populacao = nova_pop
        apt = calculaAptidao(populacao, dicDistancias)

        melhor_atual = populacao[apt.index(min(apt))]
        melhor_atual_custo = min(apt)

        if melhor_atual_custo < melhor_custo:
            melhor_custo = melhor_atual_custo
            melhor_global = melhor_atual[:]


        print(f"Geração {g+1}: melhor custo = {melhor_custo}")

    return melhor_global, melhor_custo



def traducaoRota(rota_numerica, mapa_pontos):
    rota_letras = []
    for id_cidade in rota_numerica:
        # Subtrai 1 porque o AG usa 1..N e a lista Python é 0..N-1
        indice = id_cidade - 1 
        letra = mapa_pontos[indice]
        rota_letras.append(letra)
    return rota_letras


if __name__ == "__main__":
    print("\n Gerando arquivo FlyFood")
    start_flyAG = time.time()
    gerar_tsplib("matriz.txt", "flyfood.tsp")

    print("\n Iniciando o AG FlyFood")
    matriz_fly = ler_tsplib_upper_row("flyfood.tsp")
    dic_fly = matriz_para_dicionario(matriz_fly)

    melhor_rota, melhor_custo = AG_TSP(dic_fly, len(matriz_fly), geracoes=150, tamPop=200)
    coordenadas = leitura_matriz("matriz.txt")
    chaves_ordenadas = sorted([k for k in coordenadas.keys() if k != 'R'])
    lista_pontos = ['R'] + chaves_ordenadas

    print("\n Melhor rota FlyFood:", melhor_rota)
    print("Custo:", melhor_custo)
    tempo_fly_AG = time.time() - start_flyAG
    print(f'Tempo de execução do FlyFood no AG (em segundos): {tempo_fly_AG}')
    rota_final_letras = traducaoRota(melhor_rota, lista_pontos)
    print("Rota Traduzida:", " -> ".join(rota_final_letras))


    # break de 3 segundos pra ler os resultados do flyfood
    print("\n Iniciando o AG Brasil58...")
    time.sleep(3)
    start_brasil = time.time()
    matriz_brasil = ler_tsplib_upper_row("brazil58.tsp")
    dic_brasil = matriz_para_dicionario(matriz_brasil)

    melhor_rota_b, melhor_custo_b = AG_TSP(dic_brasil, len(matriz_brasil),
                                           geracoes=500, tamPop=350)

    print("\n Melhor rota Brasil58:", melhor_rota_b)
    print("Custo:", melhor_custo_b)
    print("Gap para o ótimo (25395):", ((melhor_custo_b - 25395) / 25395) * 100, "%")
    tempo_AG = time.time() - start_brasil
    print(f'Tempo de execução do AG (em segundos): {tempo_AG}')
