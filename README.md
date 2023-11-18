# CITS3001 Mario Project

Alex Hawking (23354512) & Connor Grayden (23349066)


## Description
This project investigates the performance of Deep RL models on the game Super Mario Bros through the package gym-super-mario-bros. The two algorithms used were PPO and DDQN, so both options are available for training and testing.

## Installation and Usage
To install this project, follow these steps (each model will have its own directory holding code, these steps need to be executed within the directories):

## DDQN

Follow these steps to get up and running:

1. **Create a conda environment using mario.yml:**
    ```bash
    conda env create --name DDQN_Mario --file mario.yml
    ```

2. Activate the environment
    ```bash
    activate DDQN_Mario
    ```

3. **Ensure Correct Environment Setup**

    ├── DDQN
    │ ├── DDQN_Model.pt
    │ ├── DDQNtrain.pt
    │ ├── DDQNrun.py


4. **Run**\
    To train the model:
    ```bash
    python DDQNtrain.py
    ```

    To run the trained model:
    ```bash
    python DDQNrun.py
    ```

## PPO

Follow these steps to get up and running:

1. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    ```
    (Would highly recommend)

2. **Activate the virtual environment:**
    - **Linux/Mac:**
        ```bash
        source venv/bin/activate
        ```
    - **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run**
    ```bash
    python3 main.py
    ```
