# MindGameGUI

This repository contains the `MindGameGUI` applications written in Python using the PyQt6 framework. The applications feature a graphical user interface to simulate real-time data updates on progress bars, intended to reflect cognitive band powers or focus levels in a "Mind Game." 'MindGameBandPower' displays the average bandpowers collected over time from UDP transmission and 'MindGameFrequency' shows current frequency value, concentration level and associated band power. 'MindGameFrequency' currently uses simulated data because we do not have an algorithm to differentiate between specific frequecies.

## Overview

`MindGameGUI` utilizes PyQt6 to create a responsive and visually interactive interface. The main features include starting and stopping the update of progress bars that reflect percentage values mimicking neural feedback systems.

## Prerequisites

Before running the application, ensure you have the following installed:
- Python 3.8 or higher
- PyQt6

## Installation

First, clone the repository or download the source code. Navigate to the directory containing the project files, and install the required dependencies:

```bash
pip install PyQt6
