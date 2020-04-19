# Takes an Understand database file (.udb) as the first argument

import understand
import csv


def fileCleanText(file, str, result):
    # Open the file lexer with macros expanded and
    # inactive code removed
    for lexeme in file.lexer(False, 8, False, True):
        result[0] = lexeme.text()
        result[1] = lexeme.token()
        with open(str + ".csv", "a", encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(result)
        print("%s  %s", lexeme.text(), lexeme.token())


if __name__ == '__main__':
    # Open Database
    db = understand.open("avro.udb")
    # ***************************Code Body***********************
    file_name = open('filename2.csv', 'r')
    # 读取文件内容
    files_names = csv.reader(file_name)
    for files_name in files_names:
        with open(files_name[0] + ".csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Text', 'Token'])
        result = [0, 0]
        file = db.lookup(files_name[0], "file")[0]
        fileCleanText(file, files_name[0], result)

    # ***************************End Main Body ******************

