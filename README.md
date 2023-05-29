# Проект парсинга pep
Парсер позволяет скачать актуальную документацию Python, получить все версии Python и получить все статусы PEP.
# Установка
```bash
git clone git@github.com:PavelHomov/bs4_parser_pep.git
```
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```
# Режимы работы
- whats-new
- latest-versions
- download
- pep

# Команды парсера 
- -c, --clear-cache (Очистка кеша перед парсингом)
- -o, --output (Формат вывода)
- -h (Вызов справки)

# Стэк
- Python 
- bs4

## Примеры команд
```bash
python3 main.py whats-new -с
```
```bash
python3 main.py latest-versions -o pretty
```
```bash
python3 main.py latest-versions -o file
```