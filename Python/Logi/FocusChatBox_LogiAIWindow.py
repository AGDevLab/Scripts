import os
import logging
import asyncio
from pywinauto import Application, Desktop
from pywinauto.findwindows import ElementNotFoundError, ElementAmbiguousError

# Set up logging
log_file = "focus_chat_box_no_delay.log"
logging.basicConfig(filename=log_file, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for retries
MAX_RETRIES = 3

async def run_command():
    try:
        logging.info("Starting LogiAiPromptBuilder.exe with nexus route...")
        os.system('start "" "C:\\Program Files\\LogiOptionsPlus\\logi_ai_prompt_builder\\LogiAiPromptBuilder.exe" nexus://route/chat_gpt')
        logging.info("Command executed successfully.")
    except Exception as e:
        logging.error(f"Failed to start LogiAiPromptBuilder.exe: {e}")
        raise

async def focus_using_msaa():
    retries = 0
    while retries < MAX_RETRIES:
        try:
            logging.info(f"Attempt {retries + 1}: Connecting to the Logi AI Prompt Builder window...")
            app = Application(backend="uia").connect(title="Logi AI Prompt Builder")
            window = app.window(class_name="FLUTTERVIEW")

            logging.info("Attempting to focus on the first text child element...")
            text_element = window.child_window(control_type="Text", found_index=0)

            if text_element.exists():
                logging.info("First text child element found. Attempting to focus...")
                text_element.set_focus()
                logging.info("Element focused successfully.")
                break
            else:
                logging.warning("First text child element not found. Trying to focus on the WebView element...")

                # Attempting to focus on the WebView2 content using the hwnd from Inspect
                webview_element = Desktop(backend="uia").window(handle=0x312EE)

                if webview_element.exists():
                    webview_element.set_focus()
                    logging.info("WebView element focused successfully.")
                    break
                else:
                    logging.error("Failed to find or focus the WebView element.")
        except (ElementNotFoundError, ElementAmbiguousError) as e:
            logging.error(f"Attempt {retries + 1} failed: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred on attempt {retries + 1}: {e}")

        retries += 1

    if retries == MAX_RETRIES:
        logging.error("Max retries reached. Script failed to focus on the target element.")

async def main():
    try:
        await run_command()
        await focus_using_msaa()
        logging.info("Script completed successfully.")
    except Exception as e:
        logging.error(f"Script terminated due to an error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
