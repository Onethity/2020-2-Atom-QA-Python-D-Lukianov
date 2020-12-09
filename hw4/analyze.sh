#!/bin/bash
#
# Скрипт для анализа access логов nginx

if [ $# -eq 0 ]; then
  echo "Ошибка: вы должны передать путь к лог-файлу или к папке с логами"
  echo "Для получения справки введите $0 -h"
  exit 0
fi

if [ "$1" == "-h" ]; then
  echo "Использование: $0 (<file>|<dir>...)"
  echo "Если передан путь к лог-файлу, то выполняется анализ этого файла"
  echo "Если передан путь к папке, то скрипт выбирает все лог-файлы из папки и анализирует их"
  echo ""
  echo "Примеры:"
  echo "$0 access.log"
  echo "$0 /var/log/nginx"
  exit 0
fi

FILES=" " # Переменная для хранения путей к файлам логов
for file in "$@"; do # Перебираем аргументы
  if [ -d "$file" ]; then # Если аргумент это папка
    FILES="$FILES $file/*.log" # то добавляем все log файлы из папки
  elif [ -f "$file" ]; then # Если аргумент это файл
    FILES="$FILES $file" # то добавляем его в список всех файлов
  else
    echo "Неверный путь: $file"
    exit 1
  fi
done

LOGS=$(cat $FILES)
CURRENT_DATE=$(date +'%d/%m/%Y %H:%M')

{
  echo ""
  echo "========== Новый анализ $* $CURRENT_DATE =========="

  echo -n "Total count: "
  echo "$LOGS" | wc -l
  echo "-------------------"

  echo "Requests by type:"
  echo "$LOGS" | awk '$6 ~ /"[A-Z]+/ {print($6)}' | cut -d '"' -f2 | sort -nr | uniq -c | sort -nr
  echo "-------------------"

  echo "Top 10 biggest requests:"
  echo "$LOGS" | awk '{print($7, $10)}' | sort -k2,2 -nr | uniq -c | head -n 10
  echo "-------------------"

  echo "Top 10 client errors:"
  echo "$LOGS" | awk '{print($7, $9, $1)}' | grep '\s4[0-9][0-9]\s' | sort | uniq -c | sort -nr | head -n 10
  echo "-------------------"

  echo "Top 10 server errors:"
  echo "$LOGS" | awk '{print($7, $9, $1)}' | grep '\s5[0-9][0-9]\s' | sort | uniq -c | sort -nr | head -n 10
  echo "-------------------"
} >> output.txt

echo "Анализ успешно завершен. Результаты добавлены в output.txt"
