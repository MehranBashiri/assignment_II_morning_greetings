# Neural Radiance Field (NeRF) for 3D Scene Reconstruction

## Overview
**Neural Radiance Field (NeRF)** is a framework for synthesizing novel views of 3D scenes by representing them as continuous volumetric functions. This project implements a streamlined version of NeRF using PyTorch3D to simplify computational requirements while maintaining high-quality rendering capabilities. The models and experiments are provided in a Jupyter Notebook and can be run online or locally.

## Running the Code

The project is implemented in a Jupyter Notebook (`notebook.ipynb`), which can be executed in:

### Google Colab
1. Upload the `notebook.ipynb` to [Google Colab](https://colab.research.google.com/).
2. Follow the prompts in the notebook to install required dependencies.
3. Execute the cells sequentially to train and evaluate the models.

### Local Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/repository-name.git
    ```
2. Navigate to the project directory:
    ```bash
    cd repository-name
    ```
3. Open the Jupyter Notebook locally:
    ```bash
    jupyter notebook notebook.ipynb
    ```
4. Install required dependencies as specified in the notebook's initial cells.

## Dataset

### Clean Cow Dataset
The clean cow dataset includes rendered views of a 3D cow model with simple, uncluttered backgrounds and binary silhouettes. It provides an idealized baseline for testing Neural Radiance Fields (NeRF) models.

### Complex Noisy Cow Dataset
To evaluate the robustness of the models, the complex noisy cow dataset introduces challenges such as:
- Gaussian noise and salt-and-pepper noise.
- Visual complexities like motion blur, background changes, and color jittering.

These datasets are automatically downloaded and prepared during notebook execution.

## Models

The project includes six models evaluated on both the clean and complex noisy cow datasets. Each model's results are detailed in the Jupyter Notebook.

### Baseline NeRF
The basic implementation of NeRF with no additional optimizations or extensions. It serves as the starting point for evaluating the effectiveness of enhancements.

### Baseline NeRF + Mixed Precision Training (MPT)
Incorporates mixed precision training to optimize memory usage and improve training efficiency.

### Baseline NeRF + MPT + Early Ray Termination (ERT)
Adds Early Ray Termination (ERT), which dynamically halts ray sampling for regions that meet density thresholds, reducing computation.

### Baseline NeRF + MPT + ERT + Denoising Autoencoder (DAE)
Introduces a Denoising Autoencoder (DAE) to mitigate noise and improve robustness, especially for complex noisy datasets.

### Baseline NeRF + MPT + Multi-View Consistency (MVC)
Ensures coherence across multiple views of the same scene by enforcing consistency constraints during training.

### Baseline NeRF + MPT + DAE
Combines Mixed Precision Training and Denoising Autoencoder without ERT or MVC for robust rendering in noisy conditions.

## Results
The performance of the models is evaluated using the following metrics:
- **PSNR (Peak Signal-to-Noise Ratio):** Measures pixel-level fidelity.
- **SSIM (Structural Similarity Index):** Evaluates structural and perceptual similarity.
- **LPIPS (Learned Perceptual Image Patch Similarity):** Assesses perceptual similarity using learned features.

The results, including comparisons of the six models across both datasets, are presented quantitatively and qualitatively in the Jupyter Notebook and project report.

