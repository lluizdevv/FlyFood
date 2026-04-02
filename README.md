# 🚀 FlyFood

O **FlyFood** é um projeto acadêmico desenvolvido no curso de Sistemas de Informação da UFRPE, com foco na **otimização de rotas de entrega por drones** em ambientes urbanos.

O problema é modelado como uma variação do **Problema do Caixeiro Viajante (TSP)**, utilizando a **distância de Manhattan** para representar deslocamentos em uma malha urbana (sem movimentos diagonais).

---

## 📌 Motivação

O crescimento das entregas urbanas exige soluções mais eficientes. Nesse contexto:

- O trânsito urbano dificulta entregas rápidas  
- Drones surgem como alternativa promissora  
- A limitação de bateria exige **otimização de rotas**

O FlyFood propõe resolver esse problema utilizando algoritmos computacionais.

---

## 🎯 Objetivo

Desenvolver soluções para encontrar a **rota de menor custo** para um drone que:

1. Parte de um ponto inicial (R)  
2. Visita todos os pontos de entrega  
3. Retorna ao ponto inicial  
4. Minimiza a distância total percorrida  

---

## 🧠 Modelagem do Problema

- Representação: matriz (grid urbano)
- Pontos:
  - `R` → origem
  - `A, B, C...` → entregas
- Distância: Manhattan
  - D(u,v) = |x1 - x2| + |y1 - y2

---

## 📂 Estrutura do Projeto
FlyFood/
│
├── 1-AV/ # Solução com força bruta (exata)
├── 2-AV/ # Evolução com algoritmo genético
└── README.md

---

## ⚙️ Abordagens Utilizadas

### 🔹 1ª Avaliação (1-AV)
- Algoritmo: **Força Bruta**
- Gera todas as permutações possíveis
- Garante solução ótima
- Complexidade: **O(n!)**

---

### 🔹 2ª Avaliação (2-AV)
- Algoritmo: **Algoritmo Genético (GA)**
- Estratégia heurística
- Escalável para grandes entradas
- Trabalha com:
  - Seleção por torneio
  - Crossover (OX)
  - Mutação por inversão

---

## 📊 Comparação das Abordagens

| Método           | Vantagem              | Desvantagem              |
|-----------------|----------------------|--------------------------|
| Força Bruta     | Solução ótima        | Inviável para muitos pontos |
| Alg. Genético   | Escalável e rápido   | Aproximação (não exata)  |

---

## 🚀 Como Executar

```bash
git clone https://github.com/lluizdevv/FlyFood.git
cd FlyFood
▶️ 1-AV
python main_flyfood.py
▶️ 2-AV
python flyfood_main.py
```

## 📌 Conceitos Utilizados
Problema do Caixeiro Viajante (TSP)
Distância de Manhattan
Complexidade NP-difícil
Heurísticas e Meta-heurísticas
Algoritmos Genéticos

## 👨‍💻 Autores

Projeto desenvolvido por estudantes de Sistemas de Informação - UFRPE:

Luiz Vinicius de Lima Santos
Clara Helena Souza da Silva
Danielly Mendonça Nunes
Lucas Gabriel Ferreira de Santana

## 📚 Licença

Projeto acadêmico para fins educacionais.

