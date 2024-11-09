# my-first-app-fall-2024

## Setup

Create and activate a virutal environment:

```sh
conda create -n reports-env-2024 python=3.10
```

Activate the environment:

```sh
conda activate reports-env-2024
```


Install packages:

```sh
pip install -r requirements.txt
```


[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Create a ".env" file and add contents like the following (using your own AlphaVantage API Key):

```sh
# this is the ".env" file:
ALPHAVANTAGE_API_KEY="..."

# optionally:
SENDGRID_API_KEY = ""
SENDGRID_SENDER_ADDRESS = ""
```

## Usage

Run the example script:

```sh
python app/my_script.py
```

Run the unemployment report:

```sh
ALPHAVANTAGE_API_KEY = "..." python app/unemployment.py
```

Run the stocks report:

```sh
python app/stocks.py
```


Run the RPS game:

```sh
python app/rps.py
```

Run the example email sending file:

```sh
python app/email_service.py
```