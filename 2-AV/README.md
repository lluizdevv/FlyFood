# 🚀 FlyFood - 2ª Avaliação (Algoritmo Genético)

Esta versão evolui o projeto utilizando **Algoritmos Genéticos (GA)** para resolver o problema de forma eficiente e escalável.



## 🎯 Objetivo

Substituir a abordagem de força bruta por uma solução heurística capaz de:

- Reduzir tempo de execução
- Escalar para grandes instâncias
- Manter alta qualidade de solução



## 🧠 Ideia Principal

O problema é tratado como TSP e resolvido via:

- População de soluções (rotas)
- Evolução por gerações
- Seleção dos melhores indivíduos



## ⚙️ Componentes do Algoritmo

### 🧬 Representação
- Cromossomo = permutação dos pontos

Exemplo: [C, A, D, B]


### 🎯 Fitness
Minimizar custo da rota:

C(S) = soma das distâncias



### 🔁 Operadores

- **Seleção:** Torneio  
- **Crossover:** Order Crossover (OX)  
- **Mutação:** Inversão (Reverse)  
- **Elitismo:** preserva melhor solução  



## 📂 Estrutura
```
FlyFood/
│
├── brazil58.tsp
├── edgesbrasil58.tsp
├── flyfood.tsp
│
├── lerBrasil58.py
├── main_flyfood.py
├── projeto2.py
│
├── matriz.txt
│
└── README.md
```

## 📊 Vantagens

✔ Escalável  
✔ Tempo polinomial prático  
✔ Funciona para grandes instâncias  



## 📉 Resultados

- Força bruta inviável a partir de ~12 pontos  
- GA mantém desempenho eficiente  
- Gap pequeno em relação ao ótimo (~4%)  



## 🚀 Execução

```bash
python flyfood_main.py
```

## 🔥 Diferencial
- Uso de estrutura baseada em matriz de custos
- Compatível com TSPLib
- Aplicável a cenários reais

## 📌 Conclusão

O Algoritmo Genético se mostrou essencial para tornar o FlyFood viável em larga escala, sendo uma solução prática para problemas reais de logística.
