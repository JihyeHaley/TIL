Init signature:
nn.Conv2d(
    in_channels: int,
    out_channels: int,
    kernel_size: Union[int, Tuple[int, int]],
    stride: Union[int, Tuple[int, int]] = 1,
    padding: Union[int, Tuple[int, int]] = 0,
    dilation: Union[int, Tuple[int, int]] = 1,
    groups: int = 1,
    bias: bool = True,
    padding_mode: str = 'zeros',
)
Docstring:     
Applies a 2D convolution over an input signal composed of several input
planes.

In the simplest case, the output value of the layer with input size
:math:`(N, C_{\text{in}}, H, W)` and output :math:`(N, C_{\text{out}}, H_{\text{out}}, W_{\text{out}})`
can be precisely described as:

.. math::
    \text{out}(N_i, C_{\text{out}_j}) = \text{bias}(C_{\text{out}_j}) +
    \sum_{k = 0}^{C_{\text{in}} - 1} \text{weight}(C_{\text{out}_j}, k) \star \text{input}(N_i, k)


where :math:`\star` is the valid 2D `cross-correlation`_ operator,
:math:`N` is a batch size, :math:`C` denotes a number of channels,
:math:`H` is a height of input planes in pixels, and :math:`W` is
width in pixels.


This module supports :ref:`TensorFloat32<tf32_on_ampere>`.

* :attr:`stride` controls the stride for the cross-correlation, a single
  number or a tuple.

* :attr:`padding` controls the amount of implicit padding on both
  sides for :attr:`padding` number of points for each dimension.

* :attr:`dilation` controls the spacing between the kernel points; also
  known as the à trous algorithm. It is harder to describe, but this `link`_
  has a nice visualization of what :attr:`dilation` does.

* :attr:`groups` controls the connections between inputs and outputs.
  :attr:`in_channels` and :attr:`out_channels` must both be divisible by
  :attr:`groups`. For example,

    * At groups=1, all inputs are convolved to all outputs.
    * At groups=2, the operation becomes equivalent to having two conv
      layers side by side, each seeing half the input channels
      and producing half the output channels, and both subsequently
      concatenated.
    * At groups= :attr:`in_channels`, each input channel is convolved with
      its own set of filters (of size
      :math:`\frac{\text{out\_channels}}{\text{in\_channels}}`).

The parameters :attr:`kernel_size`, :attr:`stride`, :attr:`padding`, :attr:`dilation` can either be:

    - a single ``int`` -- in which case the same value is used for the height and width dimension
    - a ``tuple`` of two ints -- in which case, the first `int` is used for the height dimension,
      and the second `int` for the width dimension

Note:
    When `groups == in_channels` and `out_channels == K * in_channels`,
    where `K` is a positive integer, this operation is also known as a "depthwise convolution".

    In other words, for an input of size :math:`(N, C_{in}, L_{in})`,
    a depthwise convolution with a depthwise multiplier `K` can be performed with the arguments
    :math:`(C_\text{in}=C_\text{in}, C_\text{out}=C_\text{in} \times \text{K}, ..., \text{groups}=C_\text{in})`.

Note:
    In some circumstances when given tensors on a CUDA device and using CuDNN, this operator may select a nondeterministic algorithm to increase performance. If this is undesirable, you can try to make the operation deterministic (potentially at a performance cost) by setting ``torch.backends.cudnn.deterministic = True``. See :doc:`/notes/randomness` for more information.

Args:
    in_channels (int): Number of channels in the input image
    out_channels (int): Number of channels produced by the convolution
    kernel_size (int or tuple): Size of the convolving kernel
    stride (int or tuple, optional): Stride of the convolution. Default: 1
    padding (int or tuple, optional): Zero-padding added to both sides of
        the input. Default: 0
    padding_mode (string, optional): ``'zeros'``, ``'reflect'``,
        ``'replicate'`` or ``'circular'``. Default: ``'zeros'``
    dilation (int or tuple, optional): Spacing between kernel elements. Default: 1
    groups (int, optional): Number of blocked connections from input
        channels to output channels. Default: 1
    bias (bool, optional): If ``True``, adds a learnable bias to the
        output. Default: ``True``


Shape:
    - Input: :math:`(N, C_{in}, H_{in}, W_{in})`
    - Output: :math:`(N, C_{out}, H_{out}, W_{out})` where

      .. math::
          H_{out} = \left\lfloor\frac{H_{in}  + 2 \times \text{padding}[0] - \text{dilation}[0]
                    \times (\text{kernel\_size}[0] - 1) - 1}{\text{stride}[0]} + 1\right\rfloor

      .. math::
          W_{out} = \left\lfloor\frac{W_{in}  + 2 \times \text{padding}[1] - \text{dilation}[1]
                    \times (\text{kernel\_size}[1] - 1) - 1}{\text{stride}[1]} + 1\right\rfloor

Attributes:
    weight (Tensor): the learnable weights of the module of shape
        :math:`(\text{out\_channels}, \frac{\text{in\_channels}}{\text{groups}},`
        :math:`\text{kernel\_size[0]}, \text{kernel\_size[1]})`.
        The values of these weights are sampled from
        :math:`\mathcal{U}(-\sqrt{k}, \sqrt{k})` where
        :math:`k = \frac{groups}{C_\text{in} * \prod_{i=0}^{1}\text{kernel\_size}[i]}`
    bias (Tensor):   the learnable bias of the module of shape
        (out_channels). If :attr:`bias` is ``True``,
        then the values of these weights are
        sampled from :math:`\mathcal{U}(-\sqrt{k}, \sqrt{k})` where
        :math:`k = \frac{groups}{C_\text{in} * \prod_{i=0}^{1}\text{kernel\_size}[i]}`

Examples:

    >>> # With square kernels and equal stride
    >>> m = nn.Conv2d(16, 33, 3, stride=2)
    >>> # non-square kernels and unequal stride and with padding
    >>> m = nn.Conv2d(16, 33, (3, 5), stride=(2, 1), padding=(4, 2))
    >>> # non-square kernels and unequal stride and with padding and dilation
    >>> m = nn.Conv2d(16, 33, (3, 5), stride=(2, 1), padding=(4, 2), dilation=(3, 1))
    >>> input = torch.randn(20, 16, 50, 100)
    >>> output = m(input)

.. _cross-correlation:
    https://en.wikipedia.org/wiki/Cross-correlation

.. _link:
    https://github.com/vdumoulin/conv_arithmetic/blob/master/README.md
Init docstring: Initializes internal Module state, shared by both nn.Module and ScriptModule.
File:           /usr/local/anaconda3/lib/python3.8/site-packages/torch/nn/modules/conv.py
Type:           type
Subclasses:     LazyConv2d, Conv2d, ConvBn2d
