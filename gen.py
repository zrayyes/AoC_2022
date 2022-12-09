import os
from pathlib import Path
import sys
from abc import ABC, abstractmethod
from typing import Optional

if len(sys.argv) < 3:
    print("Missing parameters")
    print("gen.py language day_number")
    exit(1)


class Builder(ABC):
    language: str
    day_number: int
    new_directory_path: str

    def __init__(self, language: str, day_number: int) -> None:
        self.language = language
        self.day_number = day_number
        self.new_directory_path = f"{language}/day{day_number}"

    @abstractmethod
    def create_directory(self):
        ...

    @abstractmethod
    def create_files(self):
        ...


class PythonBuilder(Builder):
    def create_directory(self):
        if not os.path.exists(self.new_directory_path):
            os.makedirs(self.new_directory_path)

    def create_files(self):
        files = [
            Path(f"{self.new_directory_path}/a.py"),
            Path(f"{self.new_directory_path}/input.txt"),
        ]
        [file.touch(exist_ok=True) for file in files]


def get_builder(language: str, day_number: int) -> Optional[Builder]:
    if language == "python":
        return PythonBuilder(language, day_number)


language = sys.argv[1]
day_number = int(sys.argv[2])

accepted_languages = ["python"]

if language not in accepted_languages:
    print("Not accepted language.")
    print("Accepted:", accepted_languages)
    exit(1)

builder = get_builder(language, day_number)
if builder:
    builder.create_directory()
    builder.create_files()