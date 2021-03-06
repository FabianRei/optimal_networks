# Optimal networks

## "A convolutional neural network reaches optimal sensitivity for detecting some but not all patterns".  
Reith and Wandell
IEEE Access, 2020
<p> Journal: 10.1109/ACCESS.2020.3040235
<p> [PDF](https://scarlet.stanford.edu/~brian/papers/ise/2020-IEEEACCESS-Optimal-Reith-Wandell.pdf)

### Abstract
We investigate the spatial contrast sensitivity of modern convolutional neural networks (CNNs) and a linear support vector machine (SVM). To measure performance, we compare the CNN contrast-sensitivity across a range of patterns with the contrast-sensitivity of a Bayesian ideal observer (IO) with the signal-known-exactly and noise-known statistically. A ResNet-18 reaches optimal performance for harmonic patterns, as well as several classes of real world signals including faces. For these stimuli the CNN substantially outperforms the SVM. We further analyze the case in which the signal might appear in one of multiple locations and found that CNN spatial sensitivity continues to match the IO. However, the CNN sensitivity is far below optimal at detecting certain complex texture patterns. These measurements show that CNNs contrast-sensitivity differs markedly between spatial patterns. The variation in spatial contrast sensitivity may be a significant factor, influencing the performance level of an imaging system designed to detect low contrast spatial patterns.
<hr>

The signal generation code is in Matlab and depends on ISETCam (https://github.com/iset/isetcam/wiki).  

The network training code is in Python and imports various libraries.

* The directory IsetCam_signal_generation contains the Matlab scripts that generate the stimuli.  The associated figures are in the name of the script (e.g., Fig2_*).
* The script (multi_gpu_cnn_svm_optimal_observer_training.py) includes multiple sections, labeled by Figure number, that perform the network training and evaluation.
* The performance data are output into a CSV that is read by calculate_contrast_sensitivty.py to compute the estimated contrast sensitivity value.

As an example, to reproduce Figure 2 one would run the script to generate the stimuli (e.g., Fig2_<>). Then edit the file multi_gpu_cnn_svm_optimal_observer_training.py, find the section for Figure 2 (nearly line 148), and run it.





