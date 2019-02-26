# Knock Knock

## Installation

1. Download and install Python
    https://www.python.org/downloads/release/python-2715/
    Must be Python 2
    It will install pip(python package manager) as well.

2. Install Virtualenv    
    ```sh
    pip install virtualenv 
    ```

3. Activate Virtualenv
    ```sh
    virtualenv .env
    source .env/bin/activate (Linux)
    .\.env\Scripts\activate (Windows)
    ```

4. Install packages
    ```sh
    pip install -r requirements.txt
    ```

4. Run Api
    ```sh
    python api.py
    ```

5. Deploy to AWS Lambda
    ```sh
    zappa deploy prod
    ```

6. Current Cloud Apis
    https://wvf2ve2ha1.execute-api.ap-southeast-2.amazonaws.com/prod/api/

