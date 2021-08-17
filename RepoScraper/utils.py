import os
from sklearn.impute import kkkk


def get_repo_packages():
    """
    Get all repository packages and list them into files as pip freeze
    """
    imports = []
    for root, subdirs, files in os.walk("."):

        paths = []
        for file in [f for f in files if ".py" in f[-3:]]:
            py_path = os.path.join(root, file)
            paths.append(py_path)

        for file_path in paths:
            with open(file_path, "r") as f:
                for line in f:
                    line_tokens = line.split()
                    if "import" in line_tokens:
                        imports.append(line[:-1])

    imports_and_versions = []
    for import_string in imports:
        if "from" in import_string.split():
            import_string = re.sub("import.*", "", import_string)
        import_string = import_string.split(".")[0]
        import_string = re.sub("(import|from)", "", import_string).replace(" ", "")
        exec(f"import {import_string}")
        try:
            name = eval(f"{import_string}.__name__")
            vers = eval(f"{import_string}.__version__")
            imports_and_versions.append(f"{name}=={vers}")
        except AttributeError as e:
            pass

    with open("repo_modules.txt", "w") as f:
        for case in imports_and_versions:
            f.write(case + "\n")

    return 0
