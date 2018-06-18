import numpy as np
import matplotlib.pyplot as plt

#パラメータ設定
a = 0.3
b = 0.99
d = 0.25
At = 1.0
numer = eval("(1/b+d-1)") #分子
denom = eval("a*At") #分母
exp = eval("1/(a-1)") #指数

#Δk=0軌跡の式
K = np.arange(0, 4, 0.01)
def Ct(K):
    Ct = At * K**a - d * K
    return Ct

#Δc=0軌跡の式
Kt = (numer/denom)**exp

#消費と資本の軌跡グラフ作図
plt.plot(K,Ct(K)) #Δc=0軌跡のグラフ
plt.vlines([Kt], 0, 1.0, "blue", linestyle='solid') #Δk=0軌跡のグラフ
plt.ylim(0, 1)
plt.plot(Kt,Ct(Kt),"ro") #双方の軌跡の交点を赤く表示
plt.xlabel("Kt")
plt.ylabel("Ct", rotation=0)
plt.text(2.5, 0.8, "ΔK=0")
plt.text(1.5, 0.6, "ΔC=0")
plt.show()

#パラメータを追加
maxT = 30 #期間

#経路の計算
sC = np.empty(maxT)
sC[0] = 0.65 #消費の初期値
sK = np.empty(maxT)
sK[0] = Kt * 0.5 #資本の初期値 

for t in range(maxT-1):
    sC[t+1] = b*sC[t] * (a*(sK[t]**a - sC[t]+(1-d)*sK[t])**(a-1)+1-d)
    sK[t+1] = sK[t]**a - sC[t] + (1-d)*sK[t]

#資本と消費の経路グラフ作図
t = np.arange(0, 4, 1.0)
plt.plot(sK, sC)
plt.plot(K,Ct(K))
plt.vlines([Kt], 0, 1.5, "blue", linestyle='solid')
plt.plot(Kt,Ct(Kt),"ro")
plt.xlabel("Kt")
plt.ylabel("Ct", rotation=0)
plt.text(2.5, 0.8, "ΔK=0")
plt.text(1.4, 0.55, "ΔC=0")
plt.xlim(xmax=4)
plt.ylim(ymax=1.5)
plt.show()