# LearnGithubActions

This project was made to learn how the following work and how to build them:

1. YAMLs
2. CI/CD pipelines
3. Unit Tests
4. Exception Handling
5. Pipeline Alerting, specifically on failure
6. Pre-commit hooks
7. Linters

Running this project required making changes to the 2 files within the repo, pushing up the changes, allowing the pipeline to run, and monitor the outcome.
On failure this project will send an alert to my discord channel alerting that the build is broken and requires a fix. 

## **RUNNING THE PROJECT**

Before running the project you will need to install pre-commit by:
```
  pip install pre-commit
  pre-commit install
 ```

mycalculator.py is a terminal based calculator app that does simple mathematics operations based on user input. It contains a menu that directs to the operation selected and the ability to exit if the user intends to do so.

calc_unit_test.py tests that the code, specifically the math functions perform as expected. 

To get this code on your own machine you can clone the repo using git and HTTPS or SSH. 

Recommended to use vscode, and the following optional extensions: python, python debugger, and python environment. 

Running both the calculator and unittests can be done via:
```
  python mycalculator.py
  python calc_unit_test.py
```
