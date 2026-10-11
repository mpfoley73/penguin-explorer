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
project-specific environments. The next step is to verify that the recorded
environment files can restore the project reproducibly.
