import logging
import requests
from shiny import App, reactive, render, ui

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.INFO,
)
logging.info("Penguin interface started")

app_ui = ui.page_fluid(
    ui.h2("Penguin mass explorer"),
    ui.input_numeric(
        "bill_length",
        "Bill length (mm)",
        value=39.1,
        min=30,
        max=65,
        step=0.1,
    ),
    ui.input_select(
        "species",
        "Species",
        choices=["Adelie", "Chinstrap", "Gentoo"],
    ),
    ui.input_select(
        "sex",
        "Sex",
        choices=["Male", "Female"],
    ),
    ui.input_action_button("predict", "Predict body mass"),
    ui.output_text("prediction"),
)


def server(input, output, session):
    @render.text
    @reactive.event(input.predict)
    def prediction():
        penguin = {
            "bill_length_mm": input.bill_length(),
            "species_Chinstrap": input.species() == "Chinstrap",
            "species_Gentoo": input.species() == "Gentoo",
            "sex_male": input.sex() == "Male",
        }

        logging.info("Requesting prediction")
        logging.debug("Prediction inputs: %s", penguin)

        try:
            response = requests.post("http://127.0.0.1:8080/predict", json=[penguin],)
            response.raise_for_status()
            mass = response.json()["predict"][0]
        except requests.exceptions.RequestException:
            logging.exception("Prediction request failed")
            return "Could not get a prediction. Please try again later."

        logging.debug("Predicted body mass: %s", mass)
        logging.info("Prediction received successfully")

        return f"Predicted body mass: {mass:,.0f} grams"


app = App(app_ui, server)
