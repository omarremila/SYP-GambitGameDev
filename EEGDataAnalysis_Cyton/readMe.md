# EEG Data Processing and Visualization Toolkit

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

This toolkit comprises a collection of Python scripts designed to handle and analyze EEG data efficiently. The scripts utilize various libraries including pandas, numpy, matplotlib, MNE, and socket programming to provide a broad range of functionalities from data collection to processing and visualization.

## 📜 Scripts Overview

| Script                     | Description                                                   | Features                                                                                     |
|----------------------------|---------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| **brainwave_animation.py** | Animates brainwave data using a bar chart updated in real-time.| Matplotlib's animation API, dynamic updates                                                 |
| **brainwave_viewer.py**    | Displays the latest brainwave data on a bar chart using Tkinter GUI. | Interactive GUI, real-time data loading                                                      |
| **collecting_bands.py**    | Collects band power percentages from EEG data.                 | Data streaming and processing, CSV output                                                    |
| **data_analysis.py**       | Performs data analysis on EEG data.                            | Statistical analysis and visualization                                                       |
| **eeg_data_collector.py**  | Collects EEG data over a network using UDP protocol.           | Network data collection, automated file sorting                                              |
| **eeg_file_to_mne.py**     | Converts EEG data from a text file into an MNE-compatible format. | Integration with MNE library, data structuring                                               |
| **json_eeg_to_mne_plot.py**| Loads EEG data from a JSON-formatted binary file and plots it. | JSON parsing, data plotting with MNE                                                         |
| **json_to_csv_converter.py**| Converts JSON data into CSV format.                           | JSON to CSV conversion, file operations                                                      |
| **udp_data_collector.py**  | Collects data from multiple UDP sources and categorizes it.    | Multi-threaded UDP listening, data categorization                                            |

## 🛠 Installation and Requirements

- **Python Version**: 3.x
- **Required Libraries**: 
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `mne`
  - `socket`
  - `json`
  - `tkinter`
- **Installation of Libraries**:
```bash
pip install numpy pandas matplotlib mne
```
```🚀 Usage
Each script is standalone. Modify the parameters, paths, and configurations as described in the script's usage section above before running:
python <script_name>.py
```
```🤝 Contributing
Contributions to this toolkit are welcome. Please ensure to follow the coding standards and provide comments where necessary.
```
```📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
```
### Enhancements in This Version:
1. **Badges**: Added colorful badges for Python version and license type to immediately convey key information.
2. **Table Format**: Utilized a table to neatly organize scripts along with their descriptions and features, making it easier to digest at a glance.
3. **Section Icons**: Added emojis to section titles to draw attention and improve navigation.

This enhanced README aims to make the repository more accessible and attractive,
encouraging users to read through and understand the available tools more clearly.
Be sure to adjust the paths and any specific script details to match the actual content and usage accurately.
