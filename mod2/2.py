import sys

lines = sys.stdin.readlines()[1:]
def get_mean_size(lines):
    medium_size = 0
    count = 0
    if not lines:
        return "Файлов нет"
    for line in lines:
        line = line.split()
        medium_size += int(line[4])
        count += 1
    return medium_size / count

result = get_mean_size(lines)
print("Средний размер файла в байтах:", round(result, 2))
