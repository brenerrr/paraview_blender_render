import os
import gdown

os.mkdir("sample_data")
url = "https://drive.google.com/uc?id=1m7bJzr0Ajxjn77HciDOKHoFUA1RpUOrA"
output = os.path.join("sample_data", "3DFlow.000001.plt")
gdown.download(url, output)

url = "https://drive.google.com/uc?id=1bR1dWyS9NzflhBdjJZHeKYduRTn5MoO6"
output = os.path.join("sample_data", "3DFlow.000002.plt")
gdown.download(url, output)
