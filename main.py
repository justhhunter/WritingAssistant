"""
    main.py for lab report writer. This program 
    will transcript audio input to a docx file. Then give you
    the option of sending that file to a chat gpt API 
    to do editing and refinement using a specially 
    made prompt to get the most out of the process.



    Chat gpt api key
    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
"""

from dotenv import load_dotenv
import os
import sys

# load variables from .env file for api key
dotenv_path = '/home/hunter/programs/lab_report_writer/api_key.env'
load_dotenv(dotenv_path)

# assign api key
openai_api_key = os.getenv('OPENAI_API_KEY')

import speech_to_doc  
import edit_with_gpt

print(openai_api_key)


# document path/filename or just filename
doc_path = "test.docx"

def main():
    
    
    while True:
        print("\nSelect an option:")
        print("1. Edit an existing document using gpt-4")
        print("2. Speech to Text")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            edited_doc_path = edit_with_gpt.edit_document(doc_path, openai_api_key)
            print(f"Edited document saved to: {edited_doc_path}")
        elif choice == '2':
            # Start speech-to-text session
            try:
                speech_to_doc.transcribe_speech_to_docx(doc_path)  
                print(f"Document saved to: {doc_path}")
            except KeyboardInterrupt:
                # Handling Ctrl+C during speech to text
                print("\nSpeech to Text stopped.")
        elif choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

