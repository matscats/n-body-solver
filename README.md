# Gravitational Simulations in Python

This project aims to perform gravitational simulations between bodies using classical gravitational theory.

## Project Structure
- `library/`: Contains a collection of .json files that can be used for simulations.
- `projects/`: This folder should contain the .json file in which you want to perform simulations. The file must necessarily be named "params.json".
- `src/`: Source code directory.

## Prerequisites
You need to create a Python virtual environment and install the prerequisites. To do this, navigate to the project's root folder and execute the following commands:

```bash
$ python -m venv venv
$ . venv/bin/activate
$ python -m pip install -r requirements.txt
```

Now, you have a Python environment ready to run the program.

## How to Simulate?
To perform a simulation, you need to create an appropriate .json model. The file's format can be based on the .json files contained in the `library/` folder. After creating the model, rename it to "params.json" and place it in the `projects/` folder.

Once you've completed this step, you're ready to run the simulation. To do so, navigate to the project's root folder and execute the following command:

```bash
$ python src/main.py
```

Upon completion, a graph of the trajectories will be displayed.

## Extras

### How to Choose a Time Interval for the Simulation?
You can adjust the simulation time by editing the `config.py` file located in `src/` and changing the value of the `tf` variable (final time). Additionally, you can increase or decrease the simulation's precision by altering the value of the `h` variable, also found in `config.py`. It's not recommended to use an `h` value smaller than 1e-4.

### How Can I Obtain More Information About the Simulation?
The `utils.py` file contains useful tools for obtaining additional information about the simulation. You can use them to modify the code and retrieve extra data.

## Units Used
- Time is in years.
- Distance is represented in astronomical units.
- Mass is given in solar masses.