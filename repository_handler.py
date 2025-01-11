import os

def get_code_from_file(file_path):
    """
    Reads the content of a Python file and returns it.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {e}"

def check_code_in_repository(query):
    """
    Looks for code files in the repository and returns relevant code snippets based on user query.
    """
    repository_path = 'repository'  # Path to the directory where your code files are stored
    code_snippets = []

    for root, dirs, files in os.walk(repository_path):
        for file in files:
            if file.endswith('.py'):  # Or check for specific extensions you want to analyze
                file_path = os.path.join(root, file)
                code_content = get_code_from_file(file_path)
                # You can add logic to filter relevant parts of the code based on the query
                if query.lower() in code_content.lower():
                    code_snippets.append({'file': file_path, 'code': code_content})
    
    return code_snippets

