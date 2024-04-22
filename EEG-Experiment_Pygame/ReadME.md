# EEG-Experiment_Pygame

Welcome to the EEG-Experiment_Pygame repository! This repository contains a Python application that simulates an EEG-based experimental setup using Pygame. The application displays targets that flicker at different frequencies and records the responses, simulating a basic neurofeedback system.

## Overview

`EEG-Experiment_Pygame` utilizes Pygame to create a dynamic and interactive environment for EEG experiments. It is designed to test various aspects of visual and cognitive responses through controlled experiments involving flickering targets.

## Prerequisites

Before running the application, ensure you have the following installed:
- Python 3.6 or higher
- Pygame
- CSV module (typically included with Python)

## Installation

First, clone the repository or download the source code. Navigate to the directory containing the project files, and install the required dependencies:

```bash
pip install pygame
```

Structure
Here's what each file and component does within the project:

main.py: This is the main Python script that you run to launch the experiment. It includes backend logic for initializing the Pygame display, handling state changes, and managing target display and interactions.
target.py: Contains the Target class that encapsulates the properties and methods of the flickering targets used in the experiments.
Usage
To run the application, execute the following command in the terminal or command prompt:
python main.py

Key Functionalities
Dynamic Target Display:
Displays targets that flicker at different frequencies to simulate various experimental conditions.
Supports configurations for multiple targets across different screen positions.
Interaction Logging:
Logs interactions with targets including response times and target indices.
Saves the collected data to a CSV file for further analysis.
State Management:
Manages different states of the experiment, from initialization through multiple test conditions to completion.
Provides visual and auditory feedback based on user interactions and experimental requirements.
Customizing
To customize the experiment or adjust the target configurations:

Modify the target_arrange function in main.py to change how targets are displayed or add new configurations.
Adjust the target properties and behaviors by modifying the Target class in target.py.
Contributing
Contributions to enhance the application or extend its capabilities are welcome. Please ensure to maintain code readability and add appropriate comments where necessary.

License
This project is released under the MIT License. For more details, see the LICENSE file included with the project.


### Enhancements in This Version:
- **Visual Elements**: Utilizes markdown formatting to organize information cleanly and highlight sections clearly.
- **Prerequisites and Installation Instructions**: Detailed setup instructions to help users get started without prior knowledge of the dependencies.
- **Expanded Description of Functionalities**: Clear breakdown of what the application does and how it can be interacted with, which is essential for end-users.

This README is designed to be both informative and easy to navigate, enhancing the user's understanding and ability to use or contribute to the project effectively. Adjust the paths and specific script details to ensure they accurately reflect the actual content and setup of your project.
