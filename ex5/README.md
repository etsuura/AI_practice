# 人工知能入門 演習5, 6
## 演習課題5-1
### 課題

- 文字bi-gramによる単語生成

- 文字のつながりの利得がリンク上に示してある.

- **得点が最も高くなる経路を見つけよ.**
![graph](https://github.com/etsuura/AI_practice/blob/master/ex5/graph.jpg)

### 解答

ソースコードを[ex5_1 and ex5_2.py](https://github.com/etsuura/AI_practice/blob/master/ex5/ex5_1%20and%20ex5_2.py)に示す.

```class Graph```において各ノードのリンクやコスト、それに対応する文字を辞書型を用いて表す.

関数```DynamicProgrammi```において動的計画法によって多段階決定問題の経路の最大値を求める.

この際, ```class Graph```の```cost_memory```に各ノードの経路の最大値、```route```に直前に通ったノードを辞書型で記録する.

実行結果より以下の文字列が得られる.
>りつうあさん
>
>最大コストは23です.

---

## 演習課題5-2
### 課題

- 最終的にメモリに格納された最大コストと経路がどうなっているのか示せ.

### 解答

ソースコードを[ex5_1 and ex5_2.py](https://github.com/etsuura/AI_practice/blob/master/ex5/ex5_1%20and%20ex5_2.py)に示す.

出力された```class Graph```の```cost_memory```および```route```は下記のとおりである.
>Ft
>{'START': 0, 'A': 2, 'B': 5, 'C': 4, 'D': 8, 'E': 9, 'F': 8, 'G': 11, 'H': 8, 'I': 11, 'J': 15, 'K': 11, 'L': 15, 'GOAL': 23}

>st*
{'A': 'START', 'B': 'START', 'C': 'START', 'D': 'B', 'E': 'C', 'F': 'B', 'G': 'E', 'H': 'F', 'I': 'E', 'J': 'G', 'K': 'I', 'L': 'H', 'GOAL': 'L'}


---

## 演習課題5-3
### 課題
- 「りつめいかん」と「はつめいか」の編集距離を動的計画法を用いて求めよ.

### 解答

