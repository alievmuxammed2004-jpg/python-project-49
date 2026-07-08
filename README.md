### Hexlet tests and linter status:
[![Actions Status](https://github.com/alievmuxammed2004-jpg/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/alievmuxammed2004-jpg/python-project-49/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=alievmuxammed2004-jpg_python-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=alievmuxammed2004-jpg_python-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=alievmuxammed2004-jpg_python-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=alievmuxammed2004-jpg_python-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=alievmuxammed2004-jpg_python-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=alievmuxammed2004-jpg_python-project-49)

# Brain Games

Набор обучающих текстовых игр на Python для тренировки ума: НОД, проверка на чётность, калькулятор, прогрессии и др.

Каждая игра — это отдельный модуль, который запускается как CLI-команда. Проект построен по модульному принципу и легко расширяется новыми играми.

## Игры в проекте

- `brain-gcd` — вычисление наибольшего общего делителя.
- `brain-prime` — определение, является ли число простым.
- `brain-progression` — угадывание пропущенного числа в арифметической прогрессии.
- `brain-calc` — простые арифметические выражения.
- `brain-even` — проверка числа на чётность.

## Требования

- Python 3.12+
- `uv` (рекомендуется) или `pip`
- `make` (для удобных команд в Makefile)

## Установка

### Вариант 1: через `uv` (рекомендуемый)

```bash
uv sync
uv run pip install .

agg https://asciinema.org/a/x9mpmZXQLr7OYqqg demo.gif
agg demo.cast demo.gif