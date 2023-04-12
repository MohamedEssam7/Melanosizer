# Melanosizer
Melanosizer is a deep learning-based melanoma detection embedded device that was developed as part of a year-long graduation project. This project was completed in July 2022, and it was graded with an excellent mark. The project involved developing a device that could detect melanoma, a type of skin cancer, using a monitor and camera embedded on a Raspberry Pi device.

## Technology Stack

The Melanosizer project uses a combination of technologies and frameworks to achieve its goals. The core technology stack used in this project includes:

- TensorFlow: TensorFlow is an open-source machine learning library that is used extensively for deep learning projects. It was used in the Melanosizer project to build and train the model for melanoma detection.
- Raspberry Pi: Raspberry Pi is a small, single-board computer that is widely used in DIY electronics projects. It was used in the Melanosizer project as the hardware platform for the embedded device.
- Flask: Flask is a lightweight web framework that is used for building web applications. It was used in the Melanosizer project to build an API for the model.
- Python Tkinter: Python Tkinter is a standard GUI (Graphical User Interface) package for Python. It was used in the Melanosizer project to create the graphical user interface for the Raspberry Pi device.
- Ngrok: Ngrok is a tool that creates a secure tunnel between a local and remote machine, allowing access to the local machine from the internet. It was used in the Melanosizer project to deploy the API.
## Model Architecture
The final model used in the Melanosizer project was built using the Resnet-50 architecture. This architecture was modified by adding some regularization techniques to improve the performance of the model. The model was fine-tuned to achieve a private score of 91.5 in the competition.
## API
An API was built for the Melanosizer model using Flask. The API allows users to upload images of skin lesions, and the model returns a prediction of whether the lesion is melanoma or not. The API was deployed using Ngrok, which creates a secure tunnel to allow remote access to the API.
## Contributors

The following people contributed to the development of the Melanosizer project:

- [Yussef AbdElrazik](https://github.com/Yussef-AbdElrazik)
- [Shimaa](https://github.com/ShimaaMustafaa)
- [Alaa Ahmed](https://github.com/Roo7ELfahham)
- [Hader Mostafa](https://github.com/hadersaif)
- [Mohamed Essam](https://github.com/MohamedEssam7)
