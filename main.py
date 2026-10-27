import argparse
from pathlib import Path
from utils.log import log,log_content

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("filename",type = Path, help="this is the positional argument for file")
    arg = parser.parse_args()
    filename = arg.filename

    try:
        if filename.is_dir():
            for file in filename.rglob("*"):
                if file.is_file():
                    log(file)
                    log_content(file)
        elif filename.is_file():
            log(filename)
            log_content(filename)
        else:
            print("it is not in this folder")

    except FileNotFoundError:
        print("file is not in this directory")

    except PermissionError:
        print("file is not permitted")

if __name__ == "__main__":
    main()