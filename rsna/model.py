import torch
import torch.nn as nn
import torchvision.models as models


class RSNADenseNet121(nn.Module):
    '''
    Custom DenseNet121 model for RSNA hemorrhage classification.
    INPUT:      - x (torch.Tensor): Input image tensor. 
                    Shape: [batch_size, 3, 512, 512].
    OUTPUT:     - logits (torch.Tensor): Raw output logits for each class wit
                    Shape: [batch_size, 6].
    '''

    def __init__(self):
        '''
        Initializes the RSNADenseNet121 model by modifying a pre-trained DenseNet121 architecture.
        The final classification layer is replaced with a new linear layer that outputs 6 classes.
        '''

        # 1: Call the parent class constructor
        super().__init__()

        # 2: Load the DenseNet121 architecture without pre-trained weights
        base = models.densenet121(weights=None)

        # 3: Use the feature extractor and replace the classifier with a new linear layer
        self.densenet121 = base.features
        self.mlp = nn.Linear(1024, 6)

    def forward(self, x):
        '''
        Performs a forward pass through the RSNADenseNet121 model.
        INPUT:      - x (torch.Tensor): Input image tensor.
                        Shape: [batch_size, 3, 512, 512]
        OUTPUT:     - logits (torch.Tensor): Raw output logits for each class.
                        Shape: [batch_size, 6]
        '''

        # 1: Pass the input through the DenseNet121 feature extractor
        features = self.densenet121(x)
        features = torch.relu(features)
        features = torch.nn.functional.adaptive_avg_pool2d(features, (1, 1))
        features = torch.flatten(features, 1)

        # 2: Pass the features through the final linear layer to get logits
        logits = self.mlp(features)

        return logits
