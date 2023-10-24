
# *Human Stress Detection in and through Sleep* 

## Problem Description

The project addresses the issue of detecting stress in humans during the sleep period. It is based on a Kaggle dataset with the primary goal of predicting an individual's stress level. This challenge stems from the necessity to understand and tackle the impact of stress on health, particularly during rest hours.

### Context 

The project benefits from the data collected within the research project [SaYoPillow](https://www.researchgate.net/publication/332819364_Smart-Pillow_An_IoT_Based_Device_for_Stress_Detection_Considering_Sleeping_Habits), an IoT-based device designed for stress detection, taking into account sleeping habits.

The context provides a solid foundation for our approach as we leverage the advancements and expertise accumulated by SaYoPillow. We use the parameters collected by this project as a starting point to develop a broader and more applicable stress prediction model.

### Significance

The significance of this project lies in its contribution to understanding and addressing stress in the context of human sleep. The aim is to advance the ability to predict and manage stress during sleep. This work not only has implications for improving sleep quality but also for the overall management of stress, positively impacting the health and well-being of individuals.


## Data

The data used in this project is from [Human Stress Detection in and thorough Sleep](https://www.kaggle.com/datasets/laavanya/human-stress-detection-in-and-through-sleep?select=SaYoPillow.csv) dataset, which can be found in [Kaggle](https://www.kaggle.com/).

Take a thorough look at the characteristics presented in the dataset, including their descriptions and the unit of measurement, if relevant.

| Feature Name | Feature Description |
| :----------: | :-----------------: |
| snoring rate   | Represents intensity of snoring |
| respiration rate | Indicates frequency of breathing while sleeping. |
| body temperature | Refers to the body temperature |
| limb movement | Measures the frequency of limb movements during sleep. |
| blood oxygen | Represents the levels of oxygen in the blood during sleep |
| eye movement | Indicates ocular activity during sleep |
| sleeping hours | Represents the total number of sleep hours recorded |
| heart rate | Indicates the heart rate during sleep |
| stress level | Reflects the detected level of stress during the sleep period (0- low/normal, 1 – medium low, 2- medium, 3-medium high, 4 -high) |

## Getting Started

This is a set of instructions on setting up this project locally. To get a local copy up and running follow these simple example steps.

Prerequisites This is an example of how to list things you need to use this software.

- Python
- Pipenv
- Docker 

### Installing Dependencies

You can install the dependencies with pipenv, as they are specified in the `Pipfile` and `Pipfile.lock`, by running the following commands:

```
pipenv install
pipenv shell
```

### Building the model

You have the option to execute either the `train.py` file  to carry out all the necessary steps for training the final model used in this project.

To initiate the model training, you can use the following command:

```
python train.py
```

### Serving the model (Locally)

To serve the model with Docker:

1. **First install docker:**

    - *Download Docker Desktop:*
        - Visit the official Docker website: [Docker Desktop](https://www.docker.com/products/docker-desktop).
        - Click on the "Get Docker Desktop for Windows" button.
        - You will be redirected to the download page. Download the installation file here.

    - *Install Docker Desktop:*
        - Run the installation file you just downloaded.
        - Follow the installer instructions to complete the installation.

    - *Launch Docker Desktop:*
        - Once installed, look for Docker Desktop in your start menu and run it.
    
    - *Verify the Installation:*
        - Open a terminal and run the following command to verify that Docker is installed correctly:
        
            ```bash
            docker --version
            ```
        - You can also run:
            ```bash
            docker run hello-world
            ```
        - This will download a small image, run it, and you should see a message indicating that Docker is working correctly.
    
    And that's it! Now you should have Docker installed and ready to use on your Windows system.

2. **Click and initialize the DOCKER DESKTOP app after installing it:**

    - Maybe it asks you to update wsl. Open your terminal and run the following command:
        ```bash
        wsl --update
        ```

3. **Build the Docker image and run it:**

    - *Build the Docker image*
        - Open a new terminal, enter the 'Midterm_Project' folder and run the following command:
            ```
            docker build -t zoomcamp-midterm-project .
            ```
        
        - REMEMBER THE DOT (.) IN THE LAST COMMAND!!!This command builds a Docker image from the provided files.

    - *Run the previous image*
        ```
        docker run -it --rm -p 9696:9696 zoomcamp-midterm-project
        ```
        - This command runs a container based on the previously built image. Maps port 9696 on the host system to port 9696 on the container. This is important if the application inside the container is listening on port 9696.

### Testing the model

Finally, you can test the model. Serving the model locally, open another terminal, and:

```
python predict_test.py
```

## Citation

1. L. Rachakonda, A. K. Bapatla, S. P. Mohanty, and E. Kougianos, “SaYoPillow: Blockchain-Integrated Privacy-Assured IoMT Framework for Stress Management Considering Sleeping Habits”, IEEE Transactions on Consumer Electronics (TCE), Vol. 67, No. 1, Feb 2021, pp. 20-29.

2. L. Rachakonda, S. P. Mohanty, E. Kougianos, K. Karunakaran, and M. Ganapathiraju, “Smart-Pillow: An IoT based Device for Stress Detection Considering Sleeping Habits”, in Proceedings of the 4th IEEE International Symposium on Smart Electronic Systems (iSES), 2018, pp. 161--166.
