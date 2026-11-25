   " ""
    Renders the main page.
    """
   t: ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
    'Video': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h', '.php', '.rb', '.go', '.rs'],
    'Others': [] # Files not matching any other category will go here
}ur ren render_template('index.html')

@app.route('/organize', methods=['POST'])
def organize_files():
import tempfile
from flask import Flask, render_template, request, send_file, after_this_request

# Flask: A lightweight WSGI web application framework.
# Used here to handle HTTP requests, render templates, and manage file uploads/downloads.
app = Flask(__name__)

# CATEGORIES: Dictionary mapping folder names to list of file extensions.
# This logic defines how files will be sorted.
CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx', '.csv'],
    'Audio'

@app.route('/')
def index():
    Handles file uploads, organizes them, zips the result, and downloads it.
    """    """import os
import shutil
import zipfile

    if 'files' not in request.files:
        return "No file part", 400
    
    files = request.files.getlist('files')
    
    if not files or files[0].filename == '':
        return "No selected file", 400

    # tempfile: Generates unique temporary directories.
    # We use this to process files in isolation so multiple users don't conflict,
    # and to ensure cleanup happens automatically (though we do manual cleanup here for the zip).
    temp_dir = tempfile.mkdtemp()
    organize_dir = os.path.join(temp_dir, 'organized_files')
    os.makedirs(organize_dir)

    try:
        for file in files:
            filename = file.filename
            # os.path.splitext: Splits file path into (base, ext).
            _, ext = os.path.splitext(filename)
            ext = ext.lower()
            
            moved = False
            for category, extensions in CATEGORIES.items():
                if ext in extensions:
                    # os.path.join: Intelligently joins path components.
                    target_folder = os.path.join(organize_dir, category)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    
                    file.save(os.path.join(target_folder, filename))
                    moved = True
                    break
            
            if not moved:
                target_folder = os.path.join(organize_dir, 'Others')
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                file.save(os.path.join(target_folder, filename))

        # shutil.make_archive: Create a zip file from the directory.
        zip_path = shutil.make_archive(os.path.join(temp_dir, 'organized_files'), 'zip', organize_dir)

        # Clean ups after request is done
        @after_this_request
        def remove_temp_file(response):
            try:
                # shutil.rmtree: Recursively delete a directory tree.
                shutil.rmtree(temp_dir)
            except Exception as e:
                app.logger.error(f"Error removing temp dir: {e}")
            return response

        # send_file: Sends the content of a file to the client.
        return send_file(zip_path, as_attachment=True, download_name='organized_files.zip')

    except Exception as e:
        shutil.rmtree(temp_dir) # Clean up on error
        return str(e), 500

if __name__ == '__main__':
    # Running the app in debug mode allows for hot-reloading during development.
    app.run(debug=True, port=5000)
