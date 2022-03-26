import numpy as np

S0 = 100    # 초기의 주가지수
K = 105     # 행사가
T = 1.0     # 잔존만기
r = 0.05    # 무위험 이자율
vol = 0.2   # 변동성

I = 100000  # 시뮬레이션 횟수

# 가격결정 알고리즘
z = np.random.standard_normal(I)    # 의사 난수

ST = S0 * np.exp((r-0.5*vol**2)*T+vol*np.sqrt(T)*z)
# 만기시의 주가지수
hT = np.maximum(ST-K,0) # 만기시의 내재가치
C0 = np.exp(-r*T) * np.sum(hT) / I  # 몬테카를로 추정식

print(f"Value of the European Call Option {C0}")

