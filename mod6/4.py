import itertools
import json
import subprocess
from collections import Counter

with open("skillbox_json_messages.log", "r") as F:
    loggs = [json.loads(line) for line in F.readlines()]

print("1 task")
lst_levels_logs = ["DEBUG", "INFO", "WARNING", "ERROR"]
for level_log in lst_levels_logs:
    print(f"Amount logs level={level_log}:", end=' ')
    logs = subprocess.run(["grep", "-c", f'"level": "{level_log}"', "skillbox_json_messages.log"])

print("2 task")
def max_logs_by_hour(logs):
    logs_by_hour = {}
    for hour, log_group in itertools.groupby(
        logs, key=lambda j: j["time"].split(":")[0]
    ):
        logs_by_hour[hour] = len(list(log_group))
    print(f"Больше всего логов в {max(logs_by_hour, key=logs_by_hour.get)} час")
max_logs_by_hour(loggs)

print("3 task")
print("Количество логов уровня INFO с 03:18:00 до 03:20:00:", end=' ')
res3 = subprocess.run(["grep", "-c", f'"time": "03:1[8-9]:[0-5][0-9]", "level": "INFO"', "skillbox_json_messages.log"])

print("4 task")
print("Количество логов, содержащих слово пароль:", end=' ')
res4 = subprocess.run(["grep", "-c", '\w*\\b[пП]ароль\\b\w*', "skillbox_json_messages.log"])

print("5 task")
def most_frequent_word_in_warning(logs):
    warnings = [log["message"] for log in logs if log["level"] == "WARNING"]
    words = [word for word in (warning.split() for warning in warnings)]

    most_frequent, count = Counter(
        [item for sublist in words for item in sublist]
    ).most_common(1)[0]

    print(f"Самое частое слово: {most_frequent}, кол-во раз: {count}")
most_frequent_word_in_warning(loggs)