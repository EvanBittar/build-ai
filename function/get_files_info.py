# import os

# def get_files_info(working_directory, directory="."):
#     try:
#         full_path = os.path.abspath(os.path.join(working_directory, directory))
#         path = os.path.abspath(working_directory)
        
#         if not full_path.startswith(path):
#             return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
#         if not os.path.isdir(full_path):
#             return f'Error: "{directory}" is not a directory'
        
#         lines= [f'Result for {directory if directory != "." else "current directory"}:']
        
#         for name in os.listdir(full_path):
#             item_path = os.path.join(full_path,name)
            
#             try:
#                 file_size = os.path.getsize(item_path)
#                 is_dir = os.path.isdir(item_path)
#                 lines.append(f'- {name}: file_size={file_size} bytes, is_dir={is_dir}')
            
#             except Exception as e:
#                 lines.append(f'- {name}: Error: {str(e)}')
        
#         return "\n".join(lines)
    
#     except Exception as outer_error:
#         return f'Error: {str(outer_error)}'
import os

def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, directory))
        working_directory_abs = os.path.abspath(working_directory)

        header = f'Result for {directory if directory != "." else "current directory"}:'

        if not full_path.startswith(working_directory_abs):
            return f'{header}\n    Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(full_path):
            return f'{header}\n    Error: "{directory}" is not a directory'

        lines = [header]
        for name in os.listdir(full_path):
            item_path = os.path.join(full_path, name)
            try:
                file_size = os.path.getsize(item_path)
                is_dir = os.path.isdir(item_path)
                lines.append(f' - {name}: file_size={file_size} bytes, is_dir={is_dir}')
            except Exception as e:
                lines.append(f' - {name}: Error: {str(e)}')

        return "\n".join(lines)

    except Exception as outer_error:
        return f'Result for {directory}:\n    Error: {str(outer_error)}'