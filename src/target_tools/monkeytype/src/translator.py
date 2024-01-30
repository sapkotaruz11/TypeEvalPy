import argparse
import json
import os
import re
from pathlib import Path


def list_json_files(folder_path):
    python_files = sorted(Path(folder_path).rglob("*.json"))
    return python_files


def translate_content(file_path):
    # with open(file_path) as f:
    #     data = json.load(f)

    with open(file_path, "r") as file:
        code_content = file.read()

    # Regular expression to find variable annotations
    pattern = r"\b(\w+)\s*:\s*(\w+)\b"

    # Find all matches in the code content
    matches = re.findall(pattern, code_content)

    # Dictionary to store variables and their types
    data = dict(matches)

    # Do translation
    return data


def main_translator(args):
    json_files = list_json_files(args.bechmark_path)
    error_count = 0
    for file in json_files:
        try:
            # Run the inference here and gather results in /tmp/results
            translated = translate_content(file)

        except Exception as e:
            print(f"Command returned non-zero exit status: {e} for file: {file}")
            error_count += 1

    print(f"Runner finished with errors:{error_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bechmark_path",
        help="Specify the benchmark path",
        default="/tmp/micro-benchmark",
    )

    args = parser.parse_args()
    main_translator(args)
