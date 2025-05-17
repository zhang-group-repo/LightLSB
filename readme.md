# LightLSB: A lightweight secure transmission mechanism for large-scale biometric images
<!-- -------------------------------------------------------- -->
This is a repository for the paper of "LightLSB". 

## Overview
![LightLSB](./images/LightLSB.png)
<!-- -------------------------------------------------------- -->
In recent years, face recognition and other biometric recognition technologies have been increasingly appearing in social life. The interconnection of intelligent terminals in the Internet of things (IoT) has made it possible to collect biometrics on a large scale anytime and anywhere, which has also brought new challenges to the privacy protection of massive data. Compared with general computing devices, IoT terminal equipment has been becoming smaller and lighter, making it difficult to support the complex operations required by standard cryptography. The widespread use of biometric recognition has intensified social concerns about personal privacy disclosure. To address these problems, a lightweight secure transmission mechanism for large-scale biometric images (LightLSB) was proposed. The existing visual cryptography algorithm was reused, and the quality of decrypted images was gradually improved during preprocessing and post-processing. By dividing sensitive biometric images into multiple shares unrelated to the original image, the secure transmission of large-scale biometric images was realized in untrusted networks. Experiments were carried out on three typical biometric datasets, and the results showed that the proposed framework could achieve the same recognition performance on encrypted datasets as on ordinary datasets.

`InvHT_Bilateral_Filters.py` is the implementation of ours decryption improvement scheme.