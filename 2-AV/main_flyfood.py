from itertools import permutations
import time

def leitura_matriz(txt):
    coordenadas = {}
    with open(txt, 'r') as matrixTxt:
        linhas = matrixTxt.readlines()
        matriz = [linha.strip().split() for linha in linhas]
        for y, subLista in enumerate(matriz):
            for x, valor in enumerate(subLista):
                if not valor.isdigit():
                    coordenadas[valor] = (x + 1, y)
    return coordenadas

def calc_distancia_dois_pontos(dicionario):
    livro_coords = {}
    for key, value in dicionario.items():
        for chave, valor in dicionario.items():
            if key != chave:
                livro_coords[key + chave] = abs(value[0] - valor[0]) + abs(value[1] - valor[1])
    return livro_coords

def encontrar_melhor_rota(coordenadas, livro_coords):
    pontos_entrega = [key for key in coordenadas if key != 'R']
    rotas_de_entrega = permutations(pontos_entrega)
    menor_distancia = float('inf')
    melhor_rota = None

    for p in rotas_de_entrega:
        rota_completa = ('R',) + p + ('R',)
        distancia_atual = 0
        for i in range(len(rota_completa) - 1):
            ponto_a = rota_completa[i]
            ponto_b = rota_completa[i+1]
            chave = ponto_a + ponto_b if ponto_a + ponto_b in livro_coords else ponto_b + ponto_a
            distancia_atual += livro_coords[chave]


        if distancia_atual < menor_distancia:
            menor_distancia = distancia_atual
            melhor_rota = p  
    return melhor_rota, menor_distancia    

    
def main():
    coordenadas = leitura_matriz("matriz.txt")
    livro_coords = calc_distancia_dois_pontos(coordenadas)
    melhor_rota, menor_distancia = encontrar_melhor_rota(coordenadas, livro_coords)

    print("Melhor rota:", ' '.join(melhor_rota))
    print("Distância total:", menor_distancia)
        
if __name__ == "__main__":
    start_fly = time.time()
    main()
    tempo_forcaBruta = time.time() - start_fly
    print(f'Tempo de execução da FB (em segundos): {tempo_forcaBruta}') 