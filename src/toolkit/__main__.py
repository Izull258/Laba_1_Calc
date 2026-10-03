import argparse
import sys

from toolkit.calculator import evaluate
from toolkit.converter import convert_units

parser = argparse.ArgumentParser(
    description="Калькулятор и конвертер величин"
)

commands = parser.add_subparsers(dest="command", required=True)

calc_parser = commands.add_parser("calc")
calc_parser.add_argument("expression")

convert_parser = commands.add_parser("convert")
convert_parser.add_argument("value", type=float)
convert_parser.add_argument("--from", dest="from_unit", required=True)
convert_parser.add_argument("--to", dest="to_unit", required=True)

args = parser.parse_args()

try:
    if args.command == "calc":
        result = evaluate(args.expression)
    else:
        result = convert_units(
            args.value,
            args.from_unit,
            args.to_unit,
        )

    print(result)

except ValueError as error:
    print("Ошибка:", error, file=sys.stderr)
    sys.exit(2)