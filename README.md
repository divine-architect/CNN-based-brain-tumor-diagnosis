# CNN-based-brain-tumor-diagnosis
Website and machine learning model to diagnose different types of tumors from MRI images

My submission to Skynet Hacks

## Run locally

```sh
git clone https://github.com/divine-architect/CNN-based-brain-tumor-diagnosis.git
cd CNN-based-brain-tumor-diagnosis
python server.py
```

## About
This website utilizes a custom-trained model to diagnose MRI scans of human brains and recognize brain tumors. It serves as a tool to aid in the early detection of brain tumors, which can help prevent complications and save lives. However, please note that this tool should not be considered as actual medical advice. The model is capable of identifying various types of brain tumors, including Gioma, Pituitary, and Meningioma.

## How it Works
The model was trained using ImageAI, a Python library, on a dataset consisting of over 3000 images of brains with different types of brain tumors, as well as images without tumors. The dense-net 121 CNN deep-learning framework was employed for training. The training process was performed on a dedicated hardware setup instead of a Jupyter notebook. The model was trained for 100 epochs with a batch size of 32. The ImageAI library, with a PyTorch backend, made the training process straightforward. You can train the model yourself using the `trainer.py` file from the GitHub repository, or you can download the pre-trained model directly from the webserver using the provided link.

## Why
This project was developed as a submission to Skynet Hacks, with a focus on the theme of "Social Good." Early diagnosis of brain tumors can significantly contribute to saving lives, making it a fitting contribution to the theme.

## Technical Details for Nerds 🤓
For this project, a CNN-based architecture was chosen due to its effectiveness in feature extraction from images. The architecture includes multiple convolutional layers, pooling layers, and fully connected layers. By learning hierarchical representations of brain MRI scans, the model becomes capable of detecting intricate patterns and features associated with tumors. The training process involves supervised learning and backpropagation, optimizing the network's weights and biases to differentiate between tumor and non-tumor images. The loss function, typically cross-entropy, is minimized to improve prediction accuracy. Techniques such as dropout and early stopping are employed to address overfitting, while cross-validation is utilized to assess performance and determine optimal hyperparameters. Training iterations continue until the model achieves satisfactory performance on both the training and validation datasets.

## Real-World Applications
The trained brain tumor detection model can be deployed in real-world healthcare settings to assist medical professionals in the early detection of brain tumors. By analyzing brain MRI scans, the model can quickly and accurately identify suspicious regions that require further examination. This helps reduce the time and effort required for manual review, allowing medical practitioners to prioritize and focus on critical cases. Furthermore, the model can be integrated into medical imaging systems to provide real-time feedback during the scanning process, thereby enhancing the efficiency and accuracy of brain tumor detection.

For more information, please refer to the website.

## Links
https://imageai.readthedocs.io/en/latest/ --> Image AI \
https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri --> Dataset used
