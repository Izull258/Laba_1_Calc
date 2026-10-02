# Laba_1_Calc

Лабораторная №1 на Python. Калькулятор и конвертер работают через терминал.

Калькулятор считает выражения с +, -, *, /, учитывает приоритет операций и знаки чисел.
Конвертер переводит длину, массу и температуру. При неправильном вводе выводится ошибка.

Нужен Python 3.10+.

Linux и macOS. Открыть терминал в папке проекта:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install ".[test]"

python -m toolkit calc "2 + 3 * 4"
python -m toolkit convert 150 --from cm --to m
python -m toolkit --help
```

Проверить тесты:

```bash
python -m pytest
```
