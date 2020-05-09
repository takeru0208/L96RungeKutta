import numpy as np
from numba import jit

K = 40
F = 8.0

#４０変数のXをもらい，次のステップのXを返す関数
@jit
def L96(X):
    nextX = np.empty(K)
    for j in range(K):
        if j == 0:
            nextX[j] = (X[j+1] - X[38])*X[39] - X[j] + F
        elif j == 1:
            nextX[j] = (X[j+1] - X[39])*X[j-1] - X[j] + F
        elif j == 39:
            nextX[j] = (X[0] - X[j-2])*X[j-1] - X[j] + F
        else:
            nextX[j] = (X[j+1] - X[j-2])*X[j-1] - X[j] + F
    return nextX

#L96にRunge4thを１度する関数
#引数はdt と初期値X
#返し値はX+k
def L96_Runge4_one(X, dt):
    k = np.empty(K)
    k1 = np.empty(K)
    k2 = np.empty(K)
    k3 = np.empty(K)
    k4 = np.empty(K)
    Xtmp1 = np.empty(K)
    Xtmp2 = np.empty(K)
    Xtmp3 = np.empty(K)
    
    k1 = dt*L96(X)
    Xtmp1 = X + k1*0.5
    k2 = dt*L96(Xtmp1)
    Xtmp2 = X + k2*0.5
    k3 = dt*L96(Xtmp2)
    Xtmp3 = X + k3
    k4 = dt*L96(Xtmp3)
    k = (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0
    return X + k
    

#与えられた関数分スピンアップを回す関数．
#引数は回す回数tpoints, 初期値X
def spinup_L96_Runge4(tpoints, X, dt):
    for t in tpoints:
        X = L96_Runge4_one(X, dt)
    return X
        
        
#与えられたtpoints分L96をRungeKutta4thで解き，saveXに保存する関数．
#引数回す回数tpoints, 初期値startX, 保存saveX, dt
def L96_Runge4(tpoints, startX, saveX, dt):
    X = np.empty(K)
    X = startX.copy()
    for i, t in enumerate(tpoints):
        saveX[i] = L96_Runge4_one(X, dt)
        X = saveX[i]
    
    
    
    
    
    
    
    
    
    
    
    