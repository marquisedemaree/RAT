import numpy as np
import torch
import torch.nn.functional as F


def rsna_preprocess(dicom):
    '''
    Preprocesses a DICOM image for input into the RSNADenseNet121 model.
    INPUT:      - dicom (pydicom Dataset): The loaded DICOM image.
    OUTPUT:     - tensor (torch.Tensor): Preprocessed image tensor ready for model input.
                    Shape: [1, 3, 512, 512].
    '''

    # 1: Extract pixel array and apply rescaling using DICOM metadata  
    image = dicom.pixel_array.astype(np.float32)
    slope = getattr(dicom, "RescaleSlope", 1.0)
    intercept = getattr(dicom, "RescaleIntercept", 0.0)
    image = image * slope + intercept

    # 2: Clip to brain window and normalize to [0, 1]
    image = np.clip(image, 0, 80)
    image = image / 80.0

    # 3: Convert to PyTorch tensor and add batch/channel dimensions
    tensor = torch.from_numpy(image).float()
    # [H, W] -> [1, 1, H, W]
    tensor = tensor.unsqueeze(0).unsqueeze(0) 

    # 4: Resize to 512x512
    tensor = F.interpolate(
        tensor,
        size=(512, 512),
        mode="bilinear",
        align_corners=False
    )

    # 5: Repeat channel dimension to create 3-channel image
    tensor = tensor.repeat(1, 3, 1, 1)

    return tensor
