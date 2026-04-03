# 📦 FlyFood - 1ª Avaliação (Força Bruta)

Esta versão implementa uma solução **exata** para o problema de roteamento de drones utilizando **força bruta**.



## 🎯 Objetivo

Encontrar a rota de menor custo testando **todas as permutações possíveis** dos pontos de entrega.



## ⚙️ Como Funciona

1. Lê uma matriz representando o mapa
2. Identifica:
   - Ponto inicial (R)
   - Pontos de entrega
3. Gera todas as permutações (n!)
4. Calcula o custo de cada rota
5. Retorna a melhor solução



## 🧠 Modelo Matemático

Custo da rota: C(S) = D(R,s1) + Σ D(si, si+1) + D(sn, R)

## 📌 Distância Utilizada

Distância de Manhattan: D(u,v) = |xu - xv| + |yu - yv|

## 📂 Arquivos

- 1-AV
  - main_flyfood.py
  - matriz.txt

## ⚠️ Complexidade

- Tempo: **O(n!)**
- Crescimento fatorial
- Inviável para muitos pontos


## 📊 Quando usar?

✔ Pequenos conjuntos (até ~8 pontos)  
❌ Grandes conjuntos  


## 🚀 Execução

```bash
python main_flyfood.py
```
## 📌 Conclusão

A abordagem garante a solução ótima, porém possui alto custo computacional, motivando o uso de heurísticas na próxima etapa.
