import csv
with open('./book.csv') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',')
  i = 0
  find = False
  for row in spamreader:
    if find and len(row) == 4:
      pages = [int(s) for s in row[1].split() if s.isdigit()]
      print('#Page', pages[0], '\n>', row[3], '\n\n评论：\n')
    if len(row) > 0 and row[0].find('批注类型') != -1:
      find = True
