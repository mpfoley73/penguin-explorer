from pins import board_folder
from vetiver import VetiverModel
from vetiver import VetiverAPI

# Load the model created in `model.qmd`.
model_folder = "C:/Users/mpfol/OneDrive/Documents/penguin-artifacts/model"
model_board = board_folder(model_folder, allow_pickle_read=True)
loaded_v = VetiverModel.from_pin(model_board, "penguin_model")

# Create the API. `check_prototype=True` enables input checking against the 
# saved prototype.
api = VetiverAPI(loaded_v, check_prototype=True)

# Python automatically creates the variable `__name__` when executing code.
# - Running `python app.py` sets `__name__` to "__main__".
# - Importing it with `import app` sets `__name__` to "app".
# This guard lets another program import the objects in `app.py` without 
# triggering a running server.
if __name__ == "__main__":
    api.run(host="127.0.0.1", port=8080)
