# EEG Game - PsychoPy Experiment

Welcome to the EEG Game repository! This document provides detailed instructions on how to run the `EEG_Game.psyexp` file using PsychoPy3. The EEG Game is designed to test cognitive responses through various visual stimuli in an interactive format simulating a game environment.

## Overview

`EEG_Game.psyexp` is a PsychoPy experiment file that integrates visual and auditory stimuli to interact with EEG data capture systems. This experiment is tailored to investigate cognitive functions under different sensory conditions using flickering targets, pattern recognition, and reaction times.

## Prerequisites

Before you begin, ensure that you have the following prerequisites installed on your system:

- **Python 3.6 or higher**: PsychoPy is compatible with Python versions 3.6 and up.
- **PsychoPy3**: The experiment file is built specifically for the PsychoPy3 platform.

## Installation

1. **Install PsychoPy**:
   PsychoPy can be installed via pip, which is Python's package installer. Execute the following command in your terminal or command prompt:

    ```bash
    pip install psychopy
    ```

    Alternatively, you can download the standalone PsychoPy application from [PsychoPy's official website](https://www.psychopy.org/download.html) if you prefer not to use Python scripts directly.

2. **Download the Experiment File**:
   Ensure that you have downloaded the `EEG_Game.psyexp` file and all associated resources (such as images, sound files, and additional scripts if any).

## Running the Experiment

To run the experiment using PsychoPy, follow these steps:

### Using PsychoPy Standalone (GUI):

1. **Open PsychoPy**:
   Launch the PsychoPy application from your start menu or desktop.

2. **Open the Experiment**:
   Click on `File` > `Open` from the menu bar and navigate to the location of your `EEG_Game.psyexp` file. Select the file and click `Open`.

3. **Run the Experiment**:
   Click on the green 'Run' button in the toolbar or press `CTRL + R` to start the experiment. Ensure no other software that might interfere with the experiment's performance (such as screen recording or heavy background applications) is running.

4. **Save the Data**:
   Before starting, the experiment will prompt you to enter participant information and other details necessary for data segmentation and storage. Provide the required information and specify where you want the experiment data to be saved.

### Using PsychoPy from Command Line:

If you have installed PsychoPy as a Python package and prefer to use a terminal:

1. **Navigate to your Experiment's Directory**:
   Open a command prompt or terminal window and change the directory to where your `EEG_Game.psyexp` file is located using the `cd` command.

    ```bash
    cd path/to/your/experiment
    ```

2. **Run the Experiment**:
   Use the following command to start PsychoPy and open your experiment file:

    ```bash
    psychopy -m psychopy.scripts.psyexpCompile EEG_Game.psyexp -o EEG_Game.py
    python EEG_Game.py
    ```

   This command first compiles the `.psyexp` file into a `.py` script and then runs it with Python.

## Customizing the Experiment

If you need to modify the experiment, such as changing stimuli, timings, or other parameters:

- **Open the `.psyexp` file** in PsychoPy's Builder view, where you can drag and drop components, set parameters, and configure the flow of the experiment.

## Troubleshooting

If you encounter issues:

- **Check PsychoPy's version compatibility** with your Python installation.
- **Ensure all resource files** (images, sounds) are in the correct path as specified in the `.psyexp` file.
- **Consult the PsychoPy forums** or documentation for detailed troubleshooting advice.

## License

This project is released under the MIT License. For more details, see the `LICENSE` file included with the project.

## Contributing

Contributions to improve the experiment are welcome. Please ensure to maintain code readability and provide appropriate comments where necessary.

Enhancements in This Version:
- Comprehensive Setup and Execution Instructions: Detailed instructions for both GUI and command line users.
- Troubleshooting Guide: Basic troubleshooting information to help users resolve common issues.
- License and Contributing: Clarification on how others can contribute to the project or use it within the     bounds of the license.

This ```README.md``` aims to make the execution process of the EEG_Game.psyexp file as clear and straightforward as possible, ensuring that users can successfully run and modify the experiment according to their needs. Adjust the paths and specific details to accurately reflect the actual content and setup of your project.