'''
Tensors
준비 운동: NumPy
PyTorch를 소개하기 전에, 먼저 NumPy를 사용하여 신경망을 구성해보겠습니다.

NumPy는 N차원 배열 객체와 함께 이러한 배열들을 조작하기 위한 다양한 함수들을 제공합니다. 
NumPy는 과학적 분야의 연산을 위한 포괄적인 프레임워크 (Framework)입니다; 
NumPy는 연산 그래프(computation graph)나 딥러닝, 변화도(gradient)에 대해서는 알지 못합니다. 

하지만 NumPy 연산을 사용하여 순전파 단계와 역전파 단계를 직접 구현함으로써, 
2계층(two-layer)을 갖는 신경망이 무작위의 데이터를 맞추도록 할 수 있습니다:

'''
import numpy as np

N, D_in, H, D_out = 64, 1000, 100, 10

# 입력과 출력 데이터를 무작위로 생성
x = np.random.randn(N, D_in)
y = np.random.randn(H, D_out)


# 가중치 무작위로 초기화
w1 = np.random.randn(D_in, H)
w2 = np.random.randn(H, D_out)

learning_rate = 1e-6
for t in range(500):
    # 예측값  y를 계산
    h = x.dot(w1)
    h_relu = np.maximum(h, 0)
    y_pred = h_relu.dot(w2)

    # loss를 계산, 출력
    loss = np.squre(y_pred - y).sum()
    print(t, loss)

    # 손실에 따른 w1, w2의 변화도를 계산하고 역전파합니다.
    grad_y_pred = 2.0*(y_pred - y)
    grad_w2 = h_relu.T.dot(grad_y_pred)
    grad_h_relu = grad_y_pred.dot(w2.T)
    grad_h = grad_h_relu.copy()
    grad_h[h < 0] = 0
    grad_w1 = x.T.dot(grad_h)
    
    # 가중치 갱신
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2
    




