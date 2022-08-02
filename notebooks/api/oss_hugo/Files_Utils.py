
class Files_Utils:

    @staticmethod
    def all_files_recursive_with_extension(path, extension):
        import os
        files = []
        for r, d, f in os.walk(path):
            files.extend(os.path.join(r, file) for file in f if extension in file)
        return files
