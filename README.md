# File Organizer Website

This is a Python-based web application that automatically organizes uploaded files into categories (Images, Documents, Audio, etc.) and provides a zipped download of the organized structure.

## Features
- **Drag & Drop Interface**: Modern, clean UI built with TailwindCSS.
- **Auto-Sorting**: Classifies files based on extensions.
- **Privacy Focused**: Files are processed locally and temp files are cleaned up immediately.

## Libraries Used

Here is an explanation of the key Python libraries used in this project:

1.  **`flask`**:
    *   **Purpose**: The web framework used to build the application.
    *   **Usage**: Handles routing (URLs), processing incoming requests (file uploads), and rendering the HTML templates.

2.  **`os`**:
    *   **Purpose**: Provides functions for interacting with the operating system.
    *   **Usage**: Used for creating directories (`os.makedirs`), joining paths cross-platform (`os.path.join`), and splitting filenames (`os.path.splitext`).

3.  **`shutil`**:
    *   **Purpose**: Offers high-level file operations.
    *   **Usage**: Used to create the ZIP archive (`shutil.make_archive`) and to safely delete the temporary directories (`shutil.rmtree`) after processing.

4.  **`zipfile`**:
    *   **Purpose**:  Tools for creating, reading, writing, appending, and listing a ZIP file.
    *   **Usage**: In this app, `shutil.make_archive` uses this under the hood, but it's a core library for handling archives.

5.  **`tempfile`**:
    *   **Purpose**: Generates unique temporary files and directories.
    *   **Usage**: Creates a safe, isolated sandbox for each request where files are organized before being zipped, ensuring no conflicts between users.

## How to Run

1.  **Install Flask**:
    ```bash
    pip install flask
    ```

2.  **Run the App**:
    ```bash
    python app.py
    ```

3.  **Usage**:
    *   Open `http://127.0.0.1:5000` in your browser.
    *   Drag and drop files to organize them.
