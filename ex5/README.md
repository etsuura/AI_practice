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

この際, ```class Graph```の```cost_memory```に各ノードの経路のコストの最大値、```route```に直前に通ったノードを辞書型で記録する.

実行結果より以下の文字列が得られる.
>りつうあさん
>
>最大コストは23です.

---

## 演習課題5-2
### 課題

- 課題1において最終的にメモリに格納された各ノードの最大コストFtと経路st*がどうなっているのか示せ.

### 解答

ソースコードを[ex5_1 and ex5_2.py](https://github.com/etsuura/AI_practice/blob/master/ex5/ex5_1%20and%20ex5_2.py)に示す.

出力された```class Graph```の```cost_memory```および```route```は下記のとおりである.
>Ft
>{'START': 0, 'A': 2, 'B': 5, 'C': 4, 'D': 8, 'E': 9, 'F': 8, 'G': 11, 'H': 8, 'I': 11, 'J': 15, 'K': 11, 'L': 15, 'GOAL': 23}
>
>st*
{'A': 'START', 'B': 'START', 'C': 'START', 'D': 'B', 'E': 'C', 'F': 'B', 'G': 'E', 'H': 'F', 'I': 'E', 'J': 'G', 'K': 'I', 'L': 'H', 'GOAL': 'L'}

st*の結果より最適な経路は

```GOAL → L → H → F → B → START```

であることがわかる.

---

## 演習課題5-3
### 課題
- 「りつめいかん」と「はつめいか」の編集距離を動的計画法を用いて求めよ.

### 解答

ソースコードを[ex5_3.py](https://github.com/etsuura/AI_practice/blob/master/ex5/ex5_3.py)に示す.

関数```levenshtein```において動的計画法によって2つの文字列の編集距離を求める.

実行結果は以下のとおりである.

>1  2  3  4  5  
>2  2  3  4  5  
>3  3  2  3  4  
>4  4  3  2  3  
>5  5  4  3  2  
>6  6  5  4  3  
>Levenshtein Distance is 3

これを表にまとめると下記の表になる.

![graph](https://github.com/etsuura/AI_practice/blob/master/ex5/table.jpg)

また, 出力結果および表から「はつめいか」と「りつめいかん」の編集距離は3であることがわかる.

---

## 演習課題6-1
### 課題
![graph](https://github.com/etsuura/AI_practice/blob/master/ex5/q6_1.jpg)
1. P(X1)
2. P(Y2|X2)
3. P(X1,Y2)
4. P(Y1)

### 解答

1. P(X1)
    - 2/3の確率で革の袋:X1が選ばれるので  
     P(X1) = 2/3

2. P(Y2|X2)
    - 条件付き確率であるためX2であるときのY2の条件付き確率は  
    P(Y2|X2) = 1/20 / 1/3 = 3 / 20
3. P(X1,Y2)
    - P(X1,Y2)は同時確率であり,乗法定理より  　
    ```P(X1,Y2) = P(X1|Y2)P(Y2)```  
    と書き直せる.  
    よって, P(X1,Y2)は  
    
    
4. P(Y1)