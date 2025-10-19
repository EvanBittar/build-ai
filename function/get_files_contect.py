import os
from config import MAX_CHAR_LIMIT 

def get_file_content(working_directory, file_path):
    try:
        
        working_directory = os.path.abspath(working_directory)
        file_path = os.path.abspath(os.path.join(working_directory,file_path))
        
        if not file_path.startswith(working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if len(content) > MAX_CHAR_LIMIT:
            return content[:MAX_CHAR_LIMIT] + f'[...File "{file_path}" truncated at 10000 characters]'
        return content
    except Exception as e:
        return f'Error: Failed to read file "{file_path}" — {e}'
    
    
    
    # try:
    #     # Normalize paths
    #     working_directory = os.path.abspath(working_directory)
    #     file_path = os.path.abspath(file_path)
    # except Exception as e:
    #     return f'Error: Failed to resolve paths — {e}'

    # try:
    #     # Check if file_path is within working_directory
    #     if not file_path.startswith(working_directory):
    #         return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    # except Exception as e:
    #     return f'Error: Failed to validate path containment — {e}'

    # try:
    #     # Check if the file exists
    #     if not os.path.isfile(file_path):
    #         return f'Error: File "{file_path}" does not exist.'
    # except Exception as e:
    #     return f'Error: Failed to check if file exists — {e}'

    # try:
    #     # Read and return the file content
    #     with open(file_path, 'r', encoding='utf-8') as f:
    #         contect =  f.read()
    #     if len(contect) > MAX_CHAR_LIMIT:
    #         return contect[:MAX_CHAR_LIMIT] + f'[...File "{file_path}" truncated at 10000 characters].'
    #     return contect
    # except Exception as e:
    #     return f'Error: Failed to read file "{file_path}" — {e}'


