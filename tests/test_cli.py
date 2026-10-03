import subprocess
import sys
from pathlib import Path


def run_cli(arguments):
    source_folder = Path(__file__).resolve().parent.parent / "src"
    command = [sys.executable, "-m", "toolkit"] + arguments
    # Запускаем из src, чтобы Python нашёл текущую версию toolkit.
    return subprocess.run(
        command,
        cwd=source_folder,
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )


def test_cli_calculator():
    process = run_cli(["calc", "2 + 3 * 4"])
    assert process.returncode == 0
    assert process.stdout.strip() == "14.0"
    assert process.stderr == ""


def test_cli_negative_expression():
    process = run_cli(["calc", "--", "-5 + 2 * -3"])
    assert process.returncode == 0
    assert process.stdout.strip() == "-11.0"
    assert process.stderr == ""


def test_cli_converter():
    process = run_cli(["convert", "150", "--from", "cm", "--to", "m"])
    assert process.returncode == 0
    assert process.stdout.strip() == "1.5"
    assert process.stderr == ""


def test_cli_help():
    process = run_cli(["--help"])
    assert process.returncode == 0
    assert "calc" in process.stdout
    assert "convert" in process.stdout
    assert process.stderr == ""


def test_cli_division_by_zero():
    process = run_cli(["calc", "10 / 0"])
    assert process.returncode == 2
    assert process.stdout == ""
    assert "Деление на ноль" in process.stderr
    assert "Traceback" not in process.stderr


def test_cli_invalid_number():
    process = run_cli(["convert", "abc", "--from", "cm", "--to", "m"])
    assert process.returncode == 2
    assert process.stdout == ""
    assert process.stderr
    assert "Traceback" not in process.stderr


def test_cli_missing_unit():
    process = run_cli(["convert", "150", "--from", "cm"])
    assert process.returncode == 2
    assert process.stdout == ""
    assert "--to" in process.stderr


def test_cli_invalid_temperature():
    process = run_cli(["convert", "-1", "--from", "k", "--to", "c"])
    assert process.returncode == 2
    assert process.stdout == ""
    assert "ниже абсолютного нуля" in process.stderr
    assert "Traceback" not in process.stderr
