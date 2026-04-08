import importlib
import sys
from types import ModuleType
from typing import Any, Dict


def get_dependencies() -> Dict[str, ModuleType]:

    required_modules = [
        ("pandas", "pandas", "Data manipulation"),
        ("numpy", "numpy", "Numerical computation"),
        ("matplotlib", "matplotlib.pyplot", "Visualization"),
    ]

    imported_modules: Dict[str, ModuleType] = {}

    print("Checking dependencies:")

    for module in required_modules:
        try:
            imported_modules[module[1]] = importlib.import_module(module[1])
            print(
                f"[OK] {module[0]}",
                f"({(
                    importlib.import_module(module[0]).__version__
                    if module[0] != module[1]
                    else imported_modules[module[1]].__version__
                )})",
                f"- {module[2]} ready",
            )
        except ModuleNotFoundError:
            print(f"[MISSING] {module[0]} - {module[2]} missing")

    if any(value is None for value in imported_modules.values()) or len(
        imported_modules
    ) != len(required_modules):
        raise ModuleNotFoundError("\nMissing required module(s)")

    return imported_modules


def get_data(numpy: ModuleType) -> Any:
    # Generate data with numpy
    print("Analyzing Matrix data...")
    numpy.random.seed(42)
    return numpy.random.random(100)


def manipulate_data(panda: ModuleType, data: Any) -> Any:
    # Manipulate data with panda
    print(f"Processing {data.shape[0]} data points...")
    return panda.DataFrame(data, columns=["matrix_pings"])


def visualize_data(matplotlib: ModuleType, data: Any) -> None:
    # Visualize data with matplotlib
    print("Generating visualization...")
    matplotlib.figure(figsize=(20, 20))
    matplotlib.plot(data["matrix_pings"])
    matplotlib.title("Matrix pings")
    matplotlib.xlabel("Time")
    matplotlib.ylabel("Pings")
    matplotlib.savefig("matrix_analysis.png")
    matplotlib.close()


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    try:
        deps = get_dependencies()
        data = get_data(deps["numpy"])
        data = manipulate_data(deps["pandas"], data)
        try:
            visualize_data(deps["matplotlib.pyplot"], data)
        except Exception as err:
            print(
                "An exception occured during data visualization:",
                err, "Exiting...", sep="\n"
            )
            sys.exit(1)
        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")
    except ModuleNotFoundError:
        print(
            "Missing dependencies, please use pip install -r requirements.txt",
            "or poetry install and relaunch the program.",
        )


if __name__ == "__main__":
    main()
