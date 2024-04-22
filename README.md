# Project Repository Overview

This repository is structured to support the development and analysis of a game or experiment involving EEG (electroencephalogram) data. It is divided into several key directories, each with a specific focus. Below is an overview of these directories and their contents.

## Data_Analysis

This directory is dedicated to the analysis of EEG data collected during gameplay. It includes Python scripts that serve various analytical functions:

- `BrainVoltageCalc.py`: Calculates brain voltage.
- `TimeDomainPlt.py`: Plots time domain data.
- `Welch_modified_periodogram.py`: Generates a modified Welch periodogram.
- `Gambit.py`: Handles the game's data analysis aspect.

Additionally, this directory contains a subdirectory (`DataCH4`) and sample data for script testing purposes.


## EEG-Experiment-psychopy

This directory focuses on the implementation of EEG experiments using PsychoPy, a powerful software package for creating psychology stimuli in Python. The provided script, created with PsychoPy3 Experiment Builder (v2023.2.3), outlines a structured approach to running an EEG experiment. It includes the initialization of experiment parameters, participant information gathering, and the setup for data collection and logging. This script represents a comprehensive framework for executing behavioral experiments with EEG data collection, showcasing the integration of PsychoPy's capabilities into the project's experimental design framework.

Overall, the repository is geared towards the development of an EEG-based game or experiment, with a significant focus on data analysis, experimental setup, and user interface design.
# EEG Experiments and Game Simulations - Capstone Project

Welcome to the Capstone Project repository by Electrical and Computer Engineering students at Dalhousie University. This repository contains a collection of projects and experiments developed by Omar Abdel Hameed, Evan Lowe, and Connor McLeod. Our project has been graciously sponsored by Dr. Hamidreza Maymandi at [Avisyna](https://avisyna.com/start).

## Project Overview

This repository is organized into several distinct folders, each containing different aspects of our EEG-related experiments and interactive game simulations designed to study cognitive responses under various conditions.

### Folders and Their Functions

- **EEG-Experiment_Pygame**
  - **Purpose**: Contains a Python script utilizing Pygame for conducting EEG experiments that involve visual stimuli displayed in a game-like environment.
  - **Usage**: Navigate into the folder and run the Python scripts provided. The scripts are set up to interact with EEG hardware to record responses based on the stimuli presented.

- **EEG-Game_Psychopy**
  - **Purpose**: This folder contains experiments crafted with PsychoPy, designed to simulate an alien invasion game that tests various cognitive functions.
  - **Usage**: The `.psyexp` files can be opened and run using PsychoPy's GUI or command-line interface. Detailed instructions are provided within the folder's README.

- **MindGameGUI**
  - **Purpose**: Features a graphical user interface developed in PyQt for a mind-focused game intended to measure focus and attention through interactive tasks.
  - **Usage**: Run the main Python script to start the GUI. The user will interact with the interface, which tracks and logs their performance on the tasks.

- **Collecting_Bands**
  - **Purpose**: Scripts in this folder are designed to collect EEG band powers from a UDP stream, process them, and output the data for further analysis.
  - **Usage**: Execute the Python scripts to start data collection while an EEG streaming device runs concurrently.

## Installation

To run the projects and scripts contained in this repository, you may need to install specific Python libraries and PsychoPy. Each folder's README contains detailed installation instructions for the required software.

## Technologies Used

- **Python**: The primary programming language used for script development.
- **PsychoPy**: Used for creating experiments that integrate real-time stimuli and response tracking.
- **Pygame**: Employed for developing interactive games that can be used in psychological testing.
- **PyQt**: A toolkit for creating graphical user interfaces.

## Contributing

Contributions to this project are welcome. To contribute, please fork the repository, make your changes, and submit a pull request. Ensure your code adheres to the clean code principles and is well-documented.

## Acknowledgments

- **Capstone Project Team**:
  - Omar Abdel Hameed
  - Evan Lowe
  - Connor McLeod
- **Sponsor**:
  - Dr. Hamidreza Maymandi at [Avisyna](https://avisyna.com/start)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

