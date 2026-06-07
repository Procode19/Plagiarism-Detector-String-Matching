# src/file_handler.py

def read_file(file_path):
    """
    Reads text from a file
    """

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        return content

    except FileNotFoundError:
        print(f"Error: File not found -> {file_path}")
        return ""

    except Exception as e:
        print(f"Error reading file: {e}")
        return ""