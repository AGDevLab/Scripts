# FocusChatBox_LogiAIWindow

![Python](https://img.shields.io/badge/language-Python-blue.svg) ![Windows](https://img.shields.io/badge/platform-Windows-blue.svg)

<p align="center">
  <img src="https://img.icons8.com/color/144/000000/python.png" width="100" alt="Python Logo"/>
  <img src="https://img.icons8.com/color/144/000000/windows-11.png" width="100" alt="Windows Logo"/>
</p>

This repository contains the script `FocusChatBox_LogiAIWindow.py` and its compiled executable version `FocusChatBox_LogiAIWindow.exe`. The script automates the task of focusing on a specific text box inside a Flutter-based Logi AI Prompt Builder application window. It leverages Microsoft Active Accessibility (MSAA) to interact with elements that are otherwise inaccessible using standard UI Automation tools.

## Goal
Replace the native AI Action: "Open ChatGPT" with an executable that focuses on the application chat box after launching the app.

## Project Structure

- **FocusChatBox_LogiAIWindow.py**: The Python script that automates the focusing of the ChatGPT text box inside the Logi AI Prompt Builder window.
- **FocusChatBox_LogiAIWindow.exe**: The compiled executable version of the Python script for direct use on Windows without requiring a Python interpreter.
- **README.md**: This file, which contains detailed information about the project, including how to build and use the script.

## Method

The method involves several key steps:

1. **Launch the Logi AI Prompt Builder Application**: 
   - The script begins by launching the Logi AI Prompt Builder application using a specific command.
  
2. **Utilize MSAA (Microsoft Active Accessibility)**:
   - The script bypasses traditional UI Automation (UIA) methods, which struggled to access the internal elements of the `FLUTTERVIEW` window, a component of the Flutter framework.
   - MSAA is used to locate and interact with these internal elements, specifically targeting the text box where user input is accepted.

3. **Focus on the ChatGPT Text Box**:
   - The script drills down through the window's internal components using MSAA, eventually setting focus on the ChatGPT text box within the application.

### Key Components

- **os**: Used to run system-level commands to launch the application.
- **time** and **asyncio**: Handle asynchronous delays and task scheduling.
- **pywinauto**: The primary library used for automating the interaction with Windows UI elements.
- **logging**: To track the script's actions and output results to a log file.

<p align="center">
  <img src="https://img.icons8.com/external-justicon-lineal-color-justicon/144/000000/external-keyboard-coding-and-development-justicon-lineal-color-justicon.png" width="100" alt="Keyboard Icon"/>
</p>

## Code Usage

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

## Building the Executable

### Step 1: Create a Spec File

Generate a spec file for your script:
```bash
pyinstaller --onefile --specpath . FocusChatBox_LogiAIWindow.py
