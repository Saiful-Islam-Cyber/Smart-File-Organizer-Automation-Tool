import os
from organizer import FileOrganizer

def main():
    print("=============================================")
    print("   Smart File Organizer & Automation Tool    ")
    print("=============================================\n")

    # 1. Accept targeted input route directory path
    folder_path = input("Enter the absolute path of the folder to organize: ").strip()
    
    if not os.path.isdir(folder_path):
        print("Invalid directory path! Please make sure it exists on your drive setup.")
        return

    # Initialize the instance Object mapping
    organizer = FileOrganizer(folder_path)

    # 2. Offer modular selection flow option for Preview Mode bonus
    mode = input("Run in Preview Mode first? (y/n): ").strip().lower()
    
    if mode == 'y':
        print("\n--- RUNNING IN PREVIEW MODE (No files will be altered) ---")
        organizer.process_files(preview_mode=True)
        
        proceed = input("\nWould you like to execute the actual file movement now? (y/n): ").strip().lower()
        if proceed == 'y':
            organizer.process_files(preview_mode=False)
        else:
            print("Operation canceled cleanly without modifications.")
    else:
        print("\n--- RUNNING IN LIVE EXECUTION MODE ---")
        organizer.process_files(preview_mode=False)

if __name__ == "__main__":
    main()
