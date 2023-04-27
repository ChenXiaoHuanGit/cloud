import os
import re

# 要删除的数字
to_delete = [71,
89,
112,
113,
130,
134,
135,
137,
141,
147,
148,
152,
161,
162,
181,
204,
219,
228,
231,
232,
245,
265,
270,
357,
456,
462,
465,
648,
674,
703,
780,
1026,
1079,
1162,
1168,
1169,
1170,
1171,
1172,
1191,
]

# 要删除的文件名正则表达式
regex = re.compile(r'^({})\.pdbqt$'.format('|'.join(str(num) for num in to_delete)))

# 要删除的目录
dir_path = r"H:\DESK2\smi-pdbqt\pdbqt"

# 遍历目录中的所有文件，如果文件名匹配正则表达式，则删除文件
with os.scandir(dir_path) as dir_entries:
    for entry in dir_entries:
        if entry.is_file() and regex.match(entry.name):
            os.remove(entry.path)
            print(f'Deleted file: {entry.path}')
