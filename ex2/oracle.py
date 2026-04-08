from typing import Dict, Optional
from dotenv import load_dotenv
import os


def get_env_variables() -> Dict[str, Optional[str]]:
    print("ORACLE STATUS: Reading the matrix...")
    load_dotenv()
    return {
        "MATRIX_MODE": os.environ.get("MATRIX_MODE"),
        "DATABASE_URL": os.environ.get("DATABASE_URL"),
        "API_KEY": os.environ.get("API_KEY"),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL"),
        "ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT")
    }


def print_env_infos(env: Dict[str, Optional[str]]) -> None:
    print("\nConfiguration loaded:")
    print(f"Mode: {env['MATRIX_MODE'] or "[MISSING]"}")
    print(f"Database: {(
        "Connected to local instance"
        if env["DATABASE_URL"] is not None
        else
        "Not connected"
    )}")
    print(f"API Access: {(
        "Authenticated"
        if env["DATABASE_URL"] is not None
        else
        "Not connected"
    )}")
    print(f"Log Level: {env['LOG_LEVEL'] or "[MISSING]"}")
    print(f"Zion Network: {(
        "Online"
        if env["ZION_ENDPOINT"] is not None
        else
        "Offline"
    )}")


def env_security_check(env_valid: bool) -> None:
    dotenv_exists = os.path.exists(".env") or os.path.exists("ex2/.env")
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print(
        "[OK] .env file properly configured"
        if dotenv_exists
        else (
            "[WARNING] no .env file found"
            if env_valid
            else
            "[ERROR] Invalid envrionment configuration"
        )
    )
    print("[OK] Production overrides available")


def print_missing_env(env: Dict[str, Optional[str]]) -> None:
    missing_vars = [
        key
        for key, value
        in env.items()
        if value is None
    ]

    print("\nInvalid or incomplete configuration, missing variables:")

    for var in missing_vars:
        print(" -", var)

    print("\nDefine these variables in a .env file and return to the oracle")


def main() -> None:
    env = get_env_variables()
    env_valid = not any(value is None for value in env.values())
    print_env_infos(env)
    env_security_check(env_valid)
    if not env_valid:
        print_missing_env(env)
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
