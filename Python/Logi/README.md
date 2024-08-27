# FocusChatBox_LogiAIWindow

![Python](https://img.shields.io/badge/language-Python-blue.svg) ![Windows](https://img.shields.io/badge/platform-Windows-blue.svg)

<img src="https://img.icons8.com/color/48/000000/python.png" alt="Python Logo" style="width: 48px;"/> <img src="https://img.icons8.com/color/48/000000/windows-logo.png" alt="Windows Logo" style="width: 48px;"/>

## Goal

**Replace the native AI Actions**: "Open ChatGPT" with an executable that focuses on the application chat box after launching the app.

## Method

To achieve the goal, the following steps are implemented in the script:

1. **Launching the Application**:
   - The script first launches the Logi AI Prompt Builder application using the command line. This is done using Python's `os.system` function.

2. **Switching to MSAA**:
   - Instead of relying on UI Automation (UIA), the script uses Microsoft Active Accessibility (MSAA) to interact with the internal elements of the `FLUTTERVIEW` window. MSAA is better suited for interacting with older or non-standard applications that encapsulate their UI components.

3. **Locating the Chat Box**:
   - The script drills down through the `FLUTTERVIEW` window's internal components to find the text box element. This is achieved by targeting the `"" text` element, which is the first child in the hierarchy inside the encapsulated window.

4. **Focusing the Text Box**:
   - Once the text box is identified, the script focuses on it, allowing the user to start typing directly into ChatGPT without needing to manually click inside the box.

## Project Structure

- **FocusChatBox_LogiAIWindow.py**: The Python script that automates the focusing of the ChatGPT text box inside the Logi AI Prompt Builder window.
- **FocusChatBox_LogiAIWindow.exe**: The compiled executable version of the Python script for direct use on Windows without requiring a Python interpreter.
- **README.md**: This file, which contains detailed information about the project, including how to build and use the script.
- **FocusChatBox_LogiAIWindow.spec**: The PyInstaller spec file used to build the executable. It includes configurations for hidden imports and suppressing the console window.

## Python Script Explanation

The script automates the process of focusing on the ChatGPT text box within a Flutter-based application window by using MSAA for better accessibility and control.

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

## Building the Executable

To build the executable from the Python script using PyInstaller and a custom spec file:

1. **Install PyInstaller**:
    ```bash
    pip install pyinstaller
    ```

2. **Edit the Spec File**:
    - Open the `FocusChatBox_LogiAIWindow.spec` file and ensure it includes hidden imports and configurations as shown below:

    ```python
    # -*- mode: python ; coding: utf-8 -*-

    block_cipher = None

    a = Analysis(
        ['FocusChatBox_LogiAIWindow.py'],
        pathex=['.'],
        binaries=[
            ('path_to_comtypes_stream.py', 'comtypes.stream'), 
            ('path_to_comtypes_gen.py', 'comtypes.gen')
        ],
        datas=[],
        hiddenimports=['comtypes.stream', 'comtypes.gen'],
        hookspath=[],
        runtime_hooks=[],
        excludes=[],
        win_no_prefer_redirects=False,
        win_private_assemblies=False,
        cipher=block_cipher,
        noarchive=False,
    )

    pyz = PYZ(
        a.pure, 
        a.zipped_data, 
        cipher=block_cipher
    )

    exe = EXE(
        pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name='FocusChatBox_LogiAIWindow',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        upx_exclude=[],
        runtime_tmpdir=None,
        console=False,
    )

    coll = COLLECT(
        exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=[],
        name='FocusChatBox_LogiAIWindow'
    )
    ```

3. **Generate the Executable**:
    - Use the spec file to create the `.exe`:
    ```bash
    pyinstaller FocusChatBox_LogiAIWindow.spec
    ```

4. **Run the Executable**:
    - After the build process, the `.exe` file will be located in the `dist/` directory and can be run directly.

## Creating a Logitech Smart Action

To integrate the compiled executable into Logitech’s Smart Actions:

1. **Open Logitech Options+**.
2. **Navigate to the device settings** where you want to assign the action.
3. **Create a new Smart Action**:
   - Add a new action and select "Run Application."
   - Browse and select the `FocusChatBox_LogiAIWindow.exe` file.
4. **Assign the Smart Action** to a specific button on your Logitech device.

This setup will allow you to trigger the ChatGPT focus action directly from your Logitech device.

---

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
