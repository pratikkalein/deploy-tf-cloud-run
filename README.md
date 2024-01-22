<h3 align="center">MNIST Digit App</h3>

  <p align="center">
    An end to end project which shows how to deploy a Tensorflow model on Google Cloud
    <br />
    <a href="http://pratik.tech/tf-run-demo"><strong>View Demo »</strong></a>
    <br />
    <br />
</div>

## About The Project

![Screenshot](streamlit.png)
This project demonstrates how to train a ML model with TensorFlow and deploy the model to Google Cloud Run with the help of Cloud Build and Docker.

## Built With

![Python](https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask)
![Flask](https://img.shields.io/badge/Google%20Cloud-000000?style=for-the-badge&logo=googlecloud)
![Flask](https://img.shields.io/badge/streamlit-000000?style=for-the-badge&logo=streamlit)

## Getting Started

Set up the project locally.

### Prerequisites

1. Python
2. Pip
3. [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/pratikkalein/deploy-tf-cloud-run.git
   ```
2. Create and activate virtual environment

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install requirements.txt
   ```sh
   pip install -r requirements.txt
   ```

### Train the model

1. Open and run the 01-train.py file

   ```sh
   python3 01-train.py
   ```

   You can try playing with the batch size and epochs. Once the training is done a `.keras` file will be saved into the root directory.

2. Run the 02-load.py file to load and test the output of the model.
   ```sh
   python3 02-load.py
   ```

### Deploying the Flask app

1. Change your current working directory to `deploy`

   ```shell
   cd deploy
   ```

2. Make sure you are authenticated with gcloud CLI

   ```shell
   gcloud auth login
   ```

   Your default browser will open once you run this command. Choose your Google account.

3. Observe the 03-main.py file to understand how the flask API is working. Start the build using gcloud CLI.
   ```shell
   gcloud builds submit --tag gcr.io/<project_id>/<function_name>
   ```
   It usually takes 3-4 mins to build.
4. Once the build is done deploy to cloud run.
   ```shell
   gcloud run deploy --image gcr.io/<project_id>/<function_name> --platform managed
   ```
   It usually takes 3-4 mins to deploy.
5. Go to [Google Cloud Console](https://console.cloud.google.com/run) and open Cloud run. You can find the URL endpoint.

### Testing

1. Open the 04-st-app.py and add the URL you got from Cloud run and paste it at the location mentioned in the file.
2. Run the file.
   ```shell
   streamlit run 04-st-app.py
   ```
3. Upload the image and test the prediction output.

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact

Pratik Kale

Twitter - [@pratikkalein](https://twitter.com/pratikkalein) LinkedIn- [/in/pratikkalein]()

ppvkale@gmail.com

Project Link: [https://github.com/pratikkalein/deploy-tf-cloud-run](https://github.com/pratikkalein/deploy-tf-cloud-run)
Demo Link : [http://pratik.tech/tf-run-demo](http://pratik.tech/tf-run-demo)
