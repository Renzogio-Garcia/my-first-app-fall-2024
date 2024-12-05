# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template
import requests

drinks_routes = Blueprint("drinks_routes", __name__)

@drinks_routes.route("/drinks")

def drinks():
    print("DRINKS...")
    
    cocktail_url = 'https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Non_Alcoholic'

    d = requests.get(cocktail_url)
    drinks = d.json()

    drinks = drinks['drinks']
    drinks = drinks[:20]

    return render_template("drinks.html", drinks=drinks)