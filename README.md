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

[Obtain an API Key](https://sendgrid.com/en-us/2?adobe_mc_sdid=SDID%3D14497B71DE8F5F8B-3F810B9ED0886A80%7CMCORGID%3D32523BB96217F7B60A495CB6%40AdobeOrg%7CTS%3D1731112951&adobe_mc_ref=https%3A%2F%2Fwww.google.com%2F) from Sendgrid

Create a ".env" file and add contents like the following (using your own AlphaVantage API Key, Sendgrid API Key, and Sendgrid Sender Address):

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

## Testing

Run tests:

```sh
pytest
```