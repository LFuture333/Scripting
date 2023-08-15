import torch
import torch.nn as nn


#Data Preparation

#Input Layer |Hidden Layer | Output Layer| Optimizer object |
n_input,       n_hidden,        n_out,       batch_size,       learning_rate = 10, 15, 1, 100, 0.01