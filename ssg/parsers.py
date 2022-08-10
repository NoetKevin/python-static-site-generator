from typing import List
from pathlib import Path
import shutil

class Parser:
    """docstring for Parser."""

    @List[str]
    extensions = []

    def __init__(self, arg):
        pass


    def valid_extension(self, extension):
        return if extension in self.extensions

    def parse(self, path, source, dest):
        raise NotImplementedError

    def read(self, path):
        with open(path, 'r') as lines:
            return lines.read()

    def write(self, path, dest, content, ext='.html'):
        full_path = self.dest / path.with_suffix(ext)
        with open(full_path, 'w') as file:
            file.write(content)

    def copy(path, source, dest):
        shutil.copy2(path, self.dest / path.relative_to(self.source))


class ResourceParser(Parser):

    def __init__(self):
        self.extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path, source, dest):
        self.copy(path, source, dest)
