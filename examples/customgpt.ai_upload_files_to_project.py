#!/usr/bin/env python3

import argparse
import os
from customgpt_client import CustomGPT
from customgpt_client.types import File

def upload_files(api_key, project_id, directory, debug):
    CustomGPT.api_key = api_key

    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    # List all files in the directory
    files_to_upload = [os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    
    if debug:
        print(f"Files to upload: {files_to_upload}")

    for file_path in files_to_upload:
        try:
            with open(file_path, "rb") as file:
                file_content = file.read()
                file_name = os.path.basename(file_path)
                if debug:
                    print(f"Uploading file: {file_name}")
                create_source = CustomGPT.Source.create(
                    project_id=project_id, 
                    file=File(payload=file_content, file_name=file_name)
                )
                if create_source.status_code == 201:
                    print(f"Successfully uploaded: {file_name}")
                else:
                    print(f"Failed to upload: {file_name}")
                    if debug:
                        print(f"Response: {create_source.content}")
        except Exception as e:
            print(f"Error uploading file '{file_path}': {e}")

def main():
    parser = argparse.ArgumentParser(description="Upload all files in a specified directory to a CustomGPT project")
    parser.add_argument("project_id", help="Project ID in CustomGPT")
    parser.add_argument("directory", help="Directory containing files to upload")
    parser.add_argument("--debug", action='store_true', help="Enable debug logging")
    
    args = parser.parse_args()
    
    api_key = os.getenv("CUSTOMGPTAI_API_KEY")
    if not api_key:
        print("Error: CUSTOMGPTAI_API_KEY environment variable not set.")
        return
    
    upload_files(api_key, args.project_id, args.directory, args.debug)

if __name__ == "__main__":
    main()

    
