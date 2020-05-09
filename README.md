# L96RungeKutta
## 概要
Lorenz, E. (1996)に紹介されている簡易力学モデルL96をRungeKutta4thで解くプログラム

## 関数
* L96(X)

４０変数のXをもらい，次のステップのXを返す関数

* L96_Runge4_one(X, dt)

L96にRunge4thを１度する関数
引数はdt と初期値X
返し値はX+k

* spinup_L96_Runge4(tpoints, X, dt)

与えられた関数分スピンアップを回す関数．
引数は回す回数tpoints, 初期値X

* L96_Runge4(tpoints, startX, saveX, dt)

与えられたtpoints分L96をRungeKutta4thで解き，saveXに保存する関数．
引数回す回数tpoints, 初期値startX, 保存saveX, dt
