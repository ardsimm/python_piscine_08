import os
import site
import sys


def is_in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def not_in_venv(executable: str) -> None:
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current python: {executable}")
    print("Virtual Environment: None detected")
    print("")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")
    print("")
    print("Then run this program again.")


def in_venv(executable: str) -> None:
    print("MATRIX STATUS: Welcome to the construct")
    print("")
    print(f"Current Python: {executable}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {os.environ['VIRTUAL_ENV']}")
    print("")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("")
    print("Package installation path:")
    print(site.getsitepackages()[0])


def main() -> None:
    if is_in_venv():
        in_venv(sys.executable)
    else:
        not_in_venv(sys.executable)


if __name__ == "__main__":
    main()
