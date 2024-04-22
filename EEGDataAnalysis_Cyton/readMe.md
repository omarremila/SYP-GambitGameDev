# EEG Game - PsychoPy Experiment

Welcome to the EEG Game repository! This document provides detailed instructions on how to run the `EEG_Game.psyexp` file and the `collecting_bands.py` Python script using PsychoPy3. These components integrate to form a comprehensive system for conducting cognitive response experiments with visual stimuli.

## Overview

`EEG_Game.psyexp` orchestrates the visual stimuli and participant interaction, while `collecting_bands.py` handles real-time EEG data collection via a UDP connection. This setup is designed to test cognitive functions under various sensory conditions using flickering targets, pattern recognition, and reaction times.

## Prerequisites

Before you begin, ensure that you have the following prerequisites installed on your system:

- **Python 3.6 or higher**: Needed for both PsychoPy and the data collection script.
- **PsychoPy3**: Essential for running the `.psyexp` file.
- **NumPy**: Required for numerical operations in `collecting_bands.py`.
- **Socket and Threading**: Standard libraries in Python used in `collecting_bands.py` for handling UDP connections and concurrent execution.

## Installation

1. **Install PsychoPy**:
   PsychoPy can be installed via pip, which is Python's package installer. Execute the following command in your terminal or command prompt:

    ```bash
    pip install psychopy numpy
    ```

    Alternatively, you can download the standalone PsychoPy application from [PsychoPy's official website](https://www.psychopy.org/download.html) if you prefer not to use Python scripts directly.

2. **Download the Experiment Files**:
   Ensure that you have downloaded both the `EEG_Game.psyexp` and `collecting_bands.py` files, along with any associated resources (such as images, sound files, and additional scripts).

## Running the Experiment

### Using PsychoPy Standalone (GUI):

1. **Open PsychoPy**:
   Launch the PsychoPy application from your start menu or desktop.

2. **Open and Run the Experiment**:
   - Open `EEG_Game.psyexp` by clicking on `File` > `Open` and navigating to the file's location.
   - Run the experiment by clicking the green 'Run' button or pressing `CTRL + R`.

3. **Run the Data Collection Script**:
   Open a command prompt or terminal, navigate to the script's directory, and run:

    ```bash
    python collecting_bands.py
    ```

   Make sure to run this script simultaneously with the PsychoPy experiment to collect EEG data in real-time.

### Using Command Line:

1. **Navigate to the Experiment's Directory**:
   Change the directory to where your files are located:

    ```bash
    cd path/to/your/experiment
    ```

2. **Run the PsychoPy Experiment**:
    First, convert the `.psyexp` file to a `.py` script and then execute it:

    ```bash
    psychopy -m psychopy.scripts.psyexpCompile EEG_Game.psyexp -o EEG_Game.py
    python EEG_Game.py
    ```

3. **Simultaneously, Run the Data Collection Script**:

    ```bash
    python collecting_bands.py
    ```

## Customizing the Experiment

Edit the parameters in `EEG_Game.psyexp` using PsychoPy's Builder view for visual changes or stimulus adjustments. For `collecting_bands.py`, you can modify connection settings or processing logic directly in the Python script.

## Troubleshooting

- **Compatibility Issues**: Ensure PsychoPy and Python versions are compatible.
- **Resource Paths**: Verify that all external resources are correctly referenced in your experiment files.
- **UDP Connection Issues**: Ensure no firewall or network settings block the UDP ports used by `collecting_bands.py`.

## License

This project is released under the MIT License. For more details, see the `LICENSE` file included with the project.

## Contributing

Contributions to enhance the experiment or extend its capabilities are welcome. Please ensure to maintain code readability and provide appropriate comments where necessary.

- Enhancements in This Version:
Integration of collecting_bands.py: Details about running the Python script alongside the PsychoPy experiment are now included.
- Expanded Setup Instructions: Additional installation steps for required libraries like NumPy.
- Simultaneous Script Execution: Instructions for running the data collection script at the same time as the PsychoPy experiment to ensure synchronized data collection.

This updated README.md now provides a complete guide to running both the PsychoPy experiment and the accompanying Python script for EEG data collection, ensuring users can effectively utilize and modify the experiment setup. Adjust paths and specific details to reflect the actual content and setup of your project accurately.