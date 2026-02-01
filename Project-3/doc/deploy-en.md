## 6. Web Application Deployment

After completing the training process of the cat and dog image classification model, the team deployed the trained model as a web application to allow users to interact directly with the model through an intuitive user interface.
The development of the user interface (UI) and the deployment of the web application were implemented using the Gradio library. The entire source code, trained model, and user interface were packaged and executed within the Hugging Face Spaces ecosystem, enabling the application to be accessed online and used immediately without manual server configuration.

Web application link:
https://huggingface.co/spaces/oriontk24/animals-classification-demo

Figure 6.1: Web application interface for cat and dog image classification deployed on Hugging Face Spaces.

6.1. Project Architecture:

project/

- app.py : Gradio UI and inference logic
- final_model.keras : Trained CNN model
- requirements.txt : List of dependencies
- conq011-cats-vs-dogs-classification-using-cnn.ipynb : Model training notebook

  6.2. Inference Workflow:

The application workflow is described as follows:

1. The user uploads an input image (cat or dog) through the web interface
2. The uploaded image is resized to the standard input size (default: 128x128) and pixel values are normalized
3. After clicking the prediction button, the image is passed to the trained model for inference
4. The system returns prediction probabilities for each class: CAT and DOG
5. If the prediction confidence is below a predefined threshold, the image is labeled as Unknown / Not a Pet

Application demo video:
https://drive.google.com/file/d/1s9i0Z5QHi0cxrMzn3MoHzVdI-zEVvfCl/view
