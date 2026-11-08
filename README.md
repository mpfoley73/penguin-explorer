# penguin-explorer
Learning project following DevOps for Data Science by Alex K. Gold.

This repository holds the connected Penguin project as it develops through the
book. `../ds_lab` holds separate experiments and reference notes; it is not a
runtime dependency of this project.

## Chapter 1: Environments as Code

We are following the [Chapter 1 lab](https://do4ds.com/chapters/sec1/1-1-env-as-code.html)
in small increments:

1. Create and render the minimal Quarto website. **Complete.**
2. Initialize a project-local R library with `renv`, create `eda.qmd`, render
   it, and record its packages with `renv::snapshot()`. **Complete.**
3. Create a Python virtual environment, build `model.qmd`, render it, and
   capture installed packages in `requirements.txt`. **Complete.**

The goal is to isolate this project's packages and record their versions so
the environment can be restored later. The package records belong in Git;
the installed libraries and generated website do not. The Python environment
uses Python 3.13.7; `requirements.txt` records package versions but not the
Python interpreter version.

### Preview the site

From this repository's root, run:

```powershell
quarto preview
```

To render without starting a preview server:

```powershell
quarto render
```

The R exploratory analysis and Python model now render successfully using their
project-specific environments.

## Chapter 2: Deploying a Model

The Chapter 2 lab is **complete**. The project now:

1. Wraps the fitted penguin model and its input prototype in a Vetiver model.
2. Stores and versions the model on a local Pins board.
3. Reloads the saved model and checks that it can make a prediction.
4. Defines a local Vetiver prediction API in `app.py`.

This separates the trained model from the analysis document so it can be loaded
and served independently. The model artifact remains outside the repository;
the code and Python package record needed to reproduce the workflow belong in
Git.

## Chapter 3: Databases and Data APIs

The Chapter 3 lab is **complete**. The project now:

1. Stores all 344 penguins in `my-db.duckdb`, created by `prepare_data.R`.
2. Reads that shared database from the R EDA and Python model reports.
3. Retains 333 penguins for modeling, excluding 11 with missing model inputs.
4. Calls the prediction API from a Shiny for Python interface in
   `penguin_ui/app.py`, using bill length, species, and sex.

The interface sends a JSON request to the API when Predict is clicked and
displays the predicted body mass in grams. The API loads the saved Pins model;
the interface does not load the model or query DuckDB directly.

R dependencies are recorded in `renv.lock`; Python dependencies are recorded in
`requirements.txt`.

### Run the prediction explorer

From the project root, start the API in a PowerShell terminal:

```powershell
.\.venv\Scripts\python.exe app.py
```

The API requires the saved model on the local Pins board configured in `app.py`.
Its documentation is at <http://127.0.0.1:8080/docs>.

In a second PowerShell terminal, also at the project root, start the interface:

```powershell
.\.venv\Scripts\python.exe -m shiny run --reload penguin_ui/app.py
```

Open <http://127.0.0.1:8000>, choose the inputs, and click **Predict body mass**.
Keep both terminals running while using the app. Press Ctrl+C in each terminal
to stop its server.

### Recreate the data and model

Run `prepare_data.R` from the project root in the project's R environment to
create the database. Run it once: it will error if the `penguins` table already
exists, protecting the existing table from replacement.

Render the reports from the project root:

```powershell
quarto render eda.qmd
quarto render model.qmd
```

Rendering `model.qmd` also fits and saves the model to the local Pins board.
