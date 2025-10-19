# from function.get_files_info import get_files_info

# result = get_files_info("calculator", ".")
# print(result + "\n")
# # Result for current directory:
# #  - main.py: file_size=719 bytes, is_dir=False
# #  - tests.py: file_size=1331 bytes, is_dir=False
# #  - pkg: file_size=44 bytes, is_dir=True

# result = get_files_info("calculator", "pkg")
# print(result + "\n")
# # Result for 'pkg' directory:
# #  - calculator.py: file_size=1721 bytes, is_dir=False
# #  - render.py: file_size=376 bytes, is_dir=False

# result = get_files_info("calculator", "/bin")
# print(result + "\n")
# # Result for '/bin' directory:
# #     Error: Cannot list "/bin" as it is outside the permitted working directory

# result = get_files_info("calculator", "../")
# print(result + "\n")
# # Result for '../' directory:
# #     Error: Cannot list "../" as it is outside the permitted working directory


# result = get_file_content("calculator","main.py")
# print(result)

# result = get_file_content("calculator", "pkg/calculator.py")
# print(result)

# result = get_file_content("calculator", "/bin/cat")
# print(result)

# result = get_file_content("calculator", "pkg/does_not_exist.py")
# print(result)


# result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
# print(result)

# result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
# print(result)

# result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
# print(result)

from function.run_python_file import run_python_file

result = run_python_file("calculator", "main.py")
print(result)

result = run_python_file("calculator", "main.py", ["3 + 5"])
print(result)

result = run_python_file("calculator", "tests.py")
print(result)

result = run_python_file("calculator", "../main.py")
print(result)

result = run_python_file("calculator", "nonexistent.py")
print(result)

result = run_python_file("calculator", "lorem.txt")
print(result)