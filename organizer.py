import os
import shutil
import logging
from datetime import datetime

class FileOrganizer:
    # Category rules mapping extensions to target folders
    CATEGORIES = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Python Files': ['.py']
    }

    def __init__(self, target_folder):
        self.target_folder = os.path.abspath(target_folder)
        self.counts = {cat: 0 for cat in self.CATEGORIES}
        self.counts['Others'] = 0
        
        # Configure local logging framework
        logging.basicConfig(
            filename='file_management.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def get_category(self, filename):
        """Determine file category folder string based on its file extension."""
        _, ext = os.path.splitext(filename.lower())
        for category, extensions in self.CATEGORIES.items():
            if ext in extensions:
                return category
        return 'Others'

    def get_unique_path(self, destination_dir, filename):
        """Handles duplicate naming conflicts by safely appending an indexed counter suffix."""
        base, ext = os.path.splitext(filename)
        counter = 1
        unique_path = os.path.join(destination_dir, filename)
        
        while os.path.exists(unique_path):
            unique_filename = f"{base}_{counter}{ext}"
            unique_path = os.path.join(destination_dir, unique_filename)
            counter += 1
            
        return unique_path

    def process_files(self, preview_mode=False):
        """Scans the directory structure using the os module to sort files."""
        if not os.path.exists(self.target_folder):
            print(f"Error: Target path '{self.target_folder}' does not exist.")
            return False

        # Reset dictionary metrics counters before a new run execution
        self.counts = {cat: 0 for cat in self.counts}
        
        try:
            items = os.listdir(self.target_folder)
        except Exception as e:
            print(f"Failed to access or read directory contents: {str(e)}")
            return False

        files = [f for f in items if os.path.isfile(os.path.join(self.target_folder, f))]

        if not files:
            print("No loose files found inside the target directory to organize.")
            return False

        print("\n--- Processing Files ---")
        for filename in files:
            # Protect workspace runtime logic dependencies from accidental moving
            if filename in ['app.py', 'organizer.py', 'file_management.log', 'summary_report.txt']:
                continue

            source_path = os.path.join(self.target_folder, filename)
            category = self.get_category(filename)
            destination_dir = os.path.join(self.target_folder, category)

            if preview_mode:
                print(f"[PREVIEW] File '{filename}' would be moved to folder: {category}")
                self.counts[category] += 1
            else:
                # Dynamically construct missing directories
                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)

                dest_path = self.get_unique_path(destination_dir, filename)
                final_name = os.path.basename(dest_path)

                try:
                    shutil.move(source_path, dest_path)
                    log_msg = f"Moved: '{filename}' -> '{category}/{final_name}'"
                    print(log_msg)
                    logging.info(log_msg)
                    self.counts[category] += 1
                except Exception as e:
                    err_msg = f"Failed to relocate file '{filename}': {str(e)}"
                    print(err_msg)
                    logging.error(err_msg)

        if not preview_mode:
            self.generate_report()
            
        return True

    def generate_report(self):
        """Generates a tracking metrics file summarizing runtime categories processed."""
        report_path = 'summary_report.txt'
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"File Organizer Summary Report\n")
            f.write(f"Executed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Target Directory: {self.target_folder}\n")
            f.write(f"{'='*40}\n")
            for category, count in self.counts.items():
                f.write(f"{category}: {count} files processed\n")
            f.write(f"{'='*40}\n")
        print(f"\nSummary configuration report written cleanly to: '{report_path}'")
