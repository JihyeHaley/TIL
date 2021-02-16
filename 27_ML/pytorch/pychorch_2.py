'''
PyTorch: Tensors
NumPy는 훌륭한 프레임워크지만, GPU를 사용하여 수치 연산을 가속화할 수는 없습니다. 
현대의 심층 신경망에서 GPU는 종종 50배 또는 그 이상 의 속도 향상을 제공하기 때문에, 
안타깝게도 NumPy는 현대의 딥러닝에는 충분치 않습니다.

이번에는 PyTorch의 기본적인 개념인 Tensor 에 대해서 알아보겠습니다. 
PyTorch Tensor는 개념적으로 NumPy 배열과 동일합니다: Tensor는 N차원 배열이며, 

PyTorch는 Tensor 연산을 위한 다양한 함수들을 제공합니다. 
umPy 배열처럼 PyTorch Tensor는 딥러닝이나 연산 그래프, 
변화도는 알지 못하며, 과학적 분야의 연산을 위한 포괄적인 도구입니다.

그러나 NumPy와는 달리, PyTorch Tensor는 GPU를 활용하여 수치 연산을 가속화할 수 있습니다. 
GPU에서 PyTorch Tensor를 실행하기 위해서는 단지 새로운 자료형으로 변환(Cast)해주기만 하면 됩니다.

여기에서는 PyTorch Tensor를 사용하여 2계층의 신경망이 무작위 데이터를 맞추도록 할 것입니다. 
위의 NumPy 예제에서와 같이 신경망의 순전파 단계와 역전파 단계는 직접 구현하겠습니다.
'''

import torch

dtype = torch.float
device = torch.device('cpu')
# device = torch.device('cuda:0)  # gpu에서 실행하려면 이 주석을 제거해야한다.

# N은 배치 크기이며, D_in은 입력의 차원이다.
# H는 은닉의 차원이며, D_out은 출력 차원이다.
N, D_in, H, D_out =  64, 1000, 100, 10

# 무작위의 입력과 출력 데이터를 생성합니다.
x = torch.randn(N, D_in, device=device, dtype=dtype)
y = torch.randn(N, D_out, device=device, dtype=dtype)

# 무작위로 가중치를 초기화한다.
w1 = torch.randn(D_in, H, device=device, dtype=dtype)
w2 = torch.randn(H, D_out, device=device, dtype=dtype)

learning_rate = 1e-6
for t in range(500):
    # 순전파 단계: 예측값 y를 계산합니다.
    h = x.mm(w1)
    h_relu = h.clamp(min=0)
    y_pred = h_relu.mm(w2)


    # 손실(loss)을 계산하고 출력합니다.
    loss = (y_pred - y).pow(2).sum().item()
    if t % 100 == 99:
        print(t, loss)


    # 손실에 따른 w1, w2의 변화도를 계산하고 역전파합니다.
    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_relu.t().mm(grad_y_pred)
    grad_h_relu = grad_y_pred.mm(w2.t())
    grad_h = grad_h_relu.clone()
    grad_h[h < 0] = 0
    grad_w1 = x.t().mm(grad_h)

    # 경사하강법(gradient descent)를 사용하여 가중치를 갱신합니다.
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2