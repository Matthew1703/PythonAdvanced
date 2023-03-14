import os.path

path = os.path.abspath("output_file.txt")
def get_summary_rss(file: str):
    summ = 0
    with open(file, 'r') as file1:
        file1 = file1.readlines()[1:]
        for i in range(len(file1)):
            lst = file1[i].split()
            summ += int(lst[5])
    bits = summ
    kbits = summ / 1024
    mbits = kbits / 1024
    print(f"Объем потребляемой памяти: {bits} B, {round(kbits, 2)} KiB, {round(mbits, 2)} MiB")

if __name__ == "__main__":
    get_summary_rss(path)