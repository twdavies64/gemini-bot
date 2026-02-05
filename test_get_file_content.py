from functions.get_file_content import get_file_content

tests = {
    ("calculator", "lorem.txt"),
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat"), # this should return an error string
    ("calculator", "pkg/does_not_exist.py") # this should return an error string
}

for test in tests:
    content = get_file_content(test[0], test[1])
    print(content)


