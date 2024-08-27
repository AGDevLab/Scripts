# FocusChatBox_LogiAIWindow

![Python](https://img.shields.io/badge/language-Python-blue.svg) ![Windows](https://img.shields.io/badge/platform-Windows-blue.svg)

This repository contains the script `FocusChatBox_LogiAIWindow.py` and its compiled executable version `FocusChatBox_LogiAIWindow.exe`. The script automates the task of focusing on a specific text box inside a Flutter-based Logi AI Prompt Builder application window. It leverages Microsoft Active Accessibility (MSAA) to interact with elements that are otherwise inaccessible using standard UI Automation tools.

## Project Structure

- **FocusChatBox_LogiAIWindow.py**: The Python script that automates the focusing of the ChatGPT text box inside the Logi AI Prompt Builder window.
- **FocusChatBox_LogiAIWindow.exe**: The compiled executable version of the Python script for direct use on Windows without requiring a Python interpreter.
- **README.md**: This file, which contains detailed information about the project, including how to build and use the script.

## Python Script Explanation

The script is designed to:

1. **Launch the Logi AI Prompt Builder application** using a specific command.
2. **Utilize MSAA** (Microsoft Active Accessibility) to locate and interact with the internal elements of the `FLUTTERVIEW` window.
3. **Focus on the ChatGPT text box** inside the Flutter-based application window by drilling down through the window's internal components.

### Key Components

- **os**: Used to run system-level commands to launch the application.
- **time** and **asyncio**: Handle asynchronous delays and task scheduling.
- **pywinauto**: The primary library used for automating the interaction with Windows UI elements.
- **logging**: To track the script's actions and output results to a log file.

### Code Usage

To run the script manually:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd Scripts/Python/
    ```

2. **Ensure all dependencies are installed**:
    ```bash
    pip install pywinauto
    ```

3. **Run the script**:
    ```bash
    python FocusChatBox_LogiAIWindow.py
    ```

### Building the Executable

To build the executable from the Python script using PyInstaller:

1. **Install PyInstaller**:
    ```bash
    pip install pyinstaller
    ```

2. **Generate the executable**:
    ```bash
    pyinstaller --onefile --noconsole FocusChatBox_LogiAIWindow.py
    ```

3. The executable will be available in the `dist/` directory.

### Compiled Executable

The compiled executable `FocusChatBox_LogiAIWindow.exe` can be run directly on Windows without needing Python installed:

1. **Run the executable**:
    - Double-click the `FocusChatBox_LogiAIWindow.exe` file.
    - The script will automatically focus on the ChatGPT text box inside the Logi AI Prompt Builder window.

### Requirements

- **Python 3.x**: Required to run the Python script.
- **Windows OS**: The script and compiled executable are designed to run on Windows.

### Icons and Badges

- ![Python](https://img.shields.io/badge/language-Python-blue.svg)
- ![Windows](https://img.shields.io/badge/platform-Windows-blue.svg)

### Issues and Contributions

Feel free to open an issue if you encounter any problems, or contribute to the project by submitting a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

### Contact

For more information or inquiries, please contact [Your Name] at [Your Email].

