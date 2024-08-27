# FocusChatBox_LogiAIWindow

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Windows](https://img.shields.io/badge/Platform-Windows-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

**FocusChatBox_LogiAIWindow** is a Python script designed to automate the process of focusing on the ChatGPT text box inside the Logi AI Prompt Builder window. The script was created to interact with the Flutter-based Logi AI application, which encapsulates its UI in a `FLUTTERVIEW` window.

### Features

- Automatically focuses on the ChatGPT text box within the Logi AI Prompt Builder.
- Uses Microsoft Active Accessibility (MSAA) for reliable interaction with the Flutter application.
- Built with error-handling and retry logic to ensure robustness.

## Getting Started

### Prerequisites

- Python 3.8+
- `pywinauto` library
- `comtypes` library

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/yourrepo.git
   ```

2. Navigate to the `Scripts/Python/` directory:

   ```bash
   cd Scripts/Python/
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

You can run the script directly from the command line:

```bash
python FocusChatBox_LogiAIWindow.py
```
