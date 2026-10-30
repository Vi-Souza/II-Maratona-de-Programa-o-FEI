# 2ª Maratona de Programação FEI 2026 🏆

Repositório contendo as soluções em **Python 3** desenvolvidas durante e após a **2ª Maratona de Programação do Centro Universitário FEI**, realizada no Campus São Bernardo do Campo no dia 29 de outubro de 2026.

Este projeto funciona tanto como registro oficial do desempenho obtido na competição quanto como um ambiente de **treino contínuo**, onde os problemas restantes do caderno estão sendo ativamente implementados e documentados.

---

## 📌 Sumário Executivo & Resultados Oficiais

* **Instituição:** Centro Universitário FEI — Campus São Bernardo do Campo (SP)
* **Local e Data:** Sala K409 — 29 de outubro de 2026 (14h00 às 16h00)
* **Duração da Prova:** 2 horas
* **Ambiente de Prova:** **100% Offline** (sem internet, sem consultas externas, sem IA)
* **Linguagem Utilizada:** Python 3
* **Desempenho no Ranking Oficial:**
  * 🏆 **4º Lugar** na Categoria **Novatos** (alunos dos períodos iniciais de Computação)
  * 🚀 **9º Lugar** na Classificação **Geral** (competindo contra veteranos de semestres avançados)
  * 🎯 **5 Problemas Resolvidos na Competição** (de 14 propostos): Exercícios **A**, **C**, **D**, **E** e **H**

---

## 📋 Caderno de Exercícios & Status de Resolução

O caderno oficial contou com 14 problemas de complexidades variadas. A tabela abaixo acompanha tanto as soluções aceitas durante o evento quanto o progresso de resolução pós-maratona:

| Letra | Problema | Página | Status da Maratona | Status Atual | Tópico Principal / Conceito |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **A** | **Idade em Dias** | 7 | ✅ **Aceito** | Concluído | Matemática básica / Divisão inteira e resto |
| **B** | **Os Dois Últimos Dígitos** | 8 | ⏳ *Pós-prova* | 🛠️ *Treino* | Teoria dos números / Aritmética modular |
| **C** | **Múltiplos** | 9 | ✅ **Aceito** | Concluído | Lógica condicional / Operador de módulo |
| **D** | **Coordenadas de um Ponto** | 10 | ✅ **Aceito** | Concluído | Geometria analítica / Quadrantes no plano cartesiano |
| **E** | **Triângulo de Asteriscos** | 11 | ✅ **Aceito** | Concluído | Estruturas de repetição / Formatação de saída |
| **F** | **Fibonacci Fácil** | 12 | ⏳ *Pós-prova* | 🛠️ *Treino* | Sequências numéricas / Iteração linear |
| **G** | **Menor Par** | 13 | ⏳ *Pós-prova* | 🛠️ *Treino* | Vetores / Otimização linear $O(N)$ |
| **H** | **Matriz** | 14 | ✅ **Aceito** | Concluído | Matrizes bidimensionais / Diagonais e valor absoluto |
| **I** | **Vetor Palíndromo** | 15 | ⏳ *Pós-prova* | 🛠️ *Treino* | Arrays / Técnica de dois ponteiros (*Two Pointers*) |
| **J** | **Conversão** | 16 | ⏳ *Pós-prova* | 🛠️ *Treino* | Manipulação de strings / Alternância de caixa (*swapcase*) |
| **K** | **Soma dos Dígitos** | 17 | ⏳ *Pós-prova* | 🛠️ *Treino* | Decomposição numérica / Aritmética de strings grandes |
| **L** | **Doces para as Crianças** | 18 | ⏳ *Pós-prova* | 🛠️ *Treino* | Filas / Simulação circular de atendimento |
| **M** | **Sequência Boa** | 19 | ⏳ *Pós-prova* | 🛠️ *Treino* | Tabelas hash / Frequência de elementos |
| **N** | **Números Distintos** | 20 | ⏳ *Pós-prova* | 🛠️ *Treino* | Conjuntos (*Hash Sets*) / Eliminação de duplicatas |

---

## 🎯 Continuidade do Projeto & Treino Pós-Maratona

Como parte da minha preparação contínua para futuras maratonas de programação e competições da SBC/ICPC, este repositório é mantido ativo para resolver e documentar todos os exercícios restantes:

- [x] **Problema A** — Idade em Dias *(Resolvido na Maratona)*
- [ ] **Problema B** — Os Dois Últimos Dígitos
- [x] **Problema C** — Múltiplos *(Resolvido na Maratona)*
- [x] **Problema D** — Coordenadas de um Ponto *(Resolvido na Maratona)*
- [x] **Problema E** — Triângulo de Asteriscos *(Resolvido na Maratona)*
- [ ] **Problema F** — Fibonacci Fácil
- [ ] **Problema G** — Menor Par
- [x] **Problema H** — Matriz *(Resolvido na Maratona)*
- [ ] **Problema I** — Vetor Palíndromo
- [ ] **Problema J** — Conversão
- [ ] **Problema K** — Soma dos Dígitos
- [ ] **Problema L** — Doces para as Crianças
- [ ] **Problema M** — Sequência Boa
- [ ] **Problema N** — Números Distintos

---

## 💡 Detalhamento dos Problemas Resolvidos

### 1. Problema A — Idade em Dias
* **Proposta:** Converter um valor inteiro correspondente à idade de uma pessoa em dias para o formato expresso em anos, meses e dias (considerando o ano padrão de 365 dias e meses de 30 dias).
* **Conceito Aplicado:** Operadores de divisão inteira (`//`) e módulo (`%`) em cascata para extração sequencial das grandezas de tempo sem erros de arredondamento.

### 2. Problema C — Múltiplos
* **Proposta:** Ler dois números inteiros $A$ e $B$ e determinar se eles são múltiplos entre si, independentemente da ordem informada.
* **Conceito Aplicado:** Condicional com operador de resto (`A % B == 0 or B % A == 0`) garantindo tratamento simétrico para qualquer entrada.

### 3. Problema D — Coordenadas de um Ponto
* **Proposta:** Ler as coordenadas de ponto $(X, Y)$ com precisão de ponto flutuante e determinar a sua localização exata: quadrante específico (`Q1`, `Q2`, `Q3`, `Q4`), sobre o `Eixo X`, sobre o `Eixo Y` ou na `Origem`.
* **Conceito Aplicado:** Cadeia de ramificações condicionais (`if/elif/else`) priorizando os casos de borda na origem e nos eixos coordenados.

### 4. Problema E — Triângulo de Asteriscos
* **Proposta:** Dado um número $N$ ($1 \le N \le 99$), imprimir um triângulo retângulo invertido composto por $N$ linhas, onde a primeira linha possui $N$ asteriscos, a segunda possui $N - 1$, até a última linha com apenas um asterisco, sem espaços em branco após o último asterisco.
* **Conceito Aplicado:** Laço de repetição decrementando de $N$ até 1, aproveitando o operador de multiplicação de strings do Python (`'*' * i`) com rigor estrito de quebras de linha para evitar *Presentation Error*.

### 5. Problema H — Matriz
* **Proposta:** Dada uma matriz quadrada $N \times N$, calcular a diferença absoluta entre a soma dos elementos da diagonal principal e da diagonal secundária. Se $N$ for ímpar, o elemento central pertence a ambas as diagonais.
* **Conceito Aplicado:** Indexação bidimensional eficiente percorrendo a matriz em um único laço $O(N)$, acumulando `matriz[i][i]` (diagonal principal) e `matriz[i][N - 1 - i]` (diagonal secundária) e aplicando a função `abs()` no resultado final.

---

## ⚙️ Regras Oficiais e Sistema de Julgamento

1. **Entrada e Saída Estritas:** Leitura exclusiva via entrada padrão (`sys.stdin` / `input()`) e impressão via saída padrão (`print()`), sem arquivos intermediários.
2. **Formatação Rígida:** Qualquer espaço excedente ao final da linha ou quebra de linha ausente acarretava penalidade por *Presentation Error*.
3. **Penalidades de Tempo:** Cada submissão rejeitada pelo juiz adicionava **10 minutos de penalidade**, computados apenas para os problemas que fossem eventualmente aceitos.
4. **Congelamento do Placar (*Scoreboard Freeze*):** O placar público foi congelado nos últimos 30 minutos de competição para preservar a emoção da classificação final.

---

## 📂 Estrutura do Repositório

├── README.md
├── src/
│   ├── A_idade_em_dias.py
│   ├── C_multiplos.py
│   ├── D_coordenadas_de_um_ponto.py
│   ├── E_triangulo_asteriscos.py
│   ├── H_matriz.py
└── inputs/
    ├── in_A.txt
    ├── in_C.txt
    ├── in_D.txt
    ├── in_E.txt
    └── in_H.txt
```

---

## 🚀 Como Executar Localmente

Para rodar qualquer uma das soluções com dados via terminal ou arquivo de teste:

# Execução direta com entrada manual
python3 src/A_idade_em_dias.py

# Execução com redirecionamento de arquivo de teste
python3 src/E_triangulo_asteriscos.py < inputs/in_E.txt

---

## 👨‍💻 Autor

**Vitor Souza**  
Estudante de Ciência da Computação — Centro Universitário FEI  
1º Secretário do Diretório Acadêmico de Ciência da Computação (DACC) & Líder de E-Sports  
São Bernardo do Campo, SP