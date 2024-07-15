#!/usr/bin/env python3

import argparse
import os
import pprint
from customgpt_client import CustomGPT

def delete_all_files(api_key, project_id, debug):
    CustomGPT.api_key = api_key
    
    # List sources in the project
    try:
        list_sources = CustomGPT.Source.list(project_id=project_id)
        data = list_sources.parsed.data
        if debug:
            print("List sources response data:")
            pprint.pprint(data)
    except Exception as e:
        print(f"Failed to list sources for project {project_id}: {e}")
        return
    
    # Handle the single upload object correctly
    if hasattr(data, 'uploads') and data.uploads:
        upload_source_id = data.uploads.id
        if debug:
            print(f"Upload source ID: {upload_source_id}")
    else:
        print("No file uploads found.")
        return

    if debug:
        print(f"Attempting to delete upload source with ID: {upload_source_id}")
    try:
        delete_source = CustomGPT.Source.delete(project_id=project_id, source_id=upload_source_id)
        if delete_source.status_code == 200:
            print(f"Deleted upload source with ID: {upload_source_id}")
        else:
            print(f"Failed to delete upload source with ID: {upload_source_id}")
            if debug:
                print(f"Response: {delete_source.content}")
    except Exception as e:
        print(f"Error deleting upload source with ID {upload_source_id}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Delete all file sources in a specified customgpt project")
    parser.add_argument("project_id", help="Project ID in CustomGPT")
    parser.add_argument("--debug", action='store_true', help="Enable debug logging")
    
    args = parser.parse_args()
    
    api_key = os.getenv("CUSTOMGPTAI_API_KEY")
    if not api_key:
        print("Error: CUSTOMGPTAI_API_KEY environment variable not set.")
        return
    
    delete_all_files(api_key, args.project_id, args.debug)

if __name__ == "__main__":
    main()

    
