#-*- coding: utf-8 -*-
import os
import shutil
import subprocess
import sys
import time
import traceback
import csv

import file_changes_watcher
import resave 

WATCH_DIRECTORIES = ['Dropbox/d16-calculus/Results']

PUPILS_NAMES=[\
"Ашихмин Иван",\
"Байкабулов Тимур",\
"Безель Елизавета",\
"Гехт Артём",\
"Гунченко Любовь",\
"Журавлёв Андрей",\
"Забазарных Варвара",\
"Заболотских Александр",\
"Злобин Александр",\
"Крылов Дмитрий",\
"Кудрявцев Еремей",\
"Кудрявцева Полина",\
"Машкова Ольга",\
"Мурашко Матвей",\
"Павловский Михаил",\
"Рыжков Кирилл",\
"Суханов Григорий",\
"Фесюк Марина",\
"Хумонен Иннокентий",\
"Шуваева Елизавета",\
]

BY_LIST_RESULTS_DIR = 'Dropbox/d16-calculus/Results/ByListResults/'
PIVOT_DIR = 'Dropbox/d16-calculus/Results/PivotTables/'

PIVOT_TABLES = {\
"Common": PUPILS_NAMES\
,\
"Asya": [\
"Байкабулов Тимур",\
"Гехт Артём",\
"Заболотских Александр",\
], \
"Dima": [\
"Забазарных Варвара",\
"Кудрявцев Еремей",\
"Машкова Ольга",\
], \
"Grisha": [\
"Злобин Александр",\
"Крылов Дмитрий",\
"Фесюк Марина",\
], \
"Kirill": [\
"Кудрявцева Полина",\
"Мурашко Матвей",\
"Рыжков Кирилл",\
], \
"Lesha": [\
"Гунченко Любовь",\
"Журавлёв Андрей",\
"Павловский Михаил",\
"Шуваева Елизавета",\
], \
"Lida": [\
"Ашихмин Иван",\
"Безель Елизавета",\
"Хумонен Иннокентий",\
], \
}

PERSONAL_DIR='Dropbox/d16-calculus/Results/PersonalResults/'

FILE_START=\
"\
%%THIS FILE IS AUTO GENERATED\n\
%%ALL CHANGES WILL BE IGNORED\n\
\n\
\\documentclass[a4paper,landscape,12pt]{article}\n\
\\usepackage{newlistok}\n\
\\usepackage{wrapfig}\n\
\\usepackage{tikz}\n\
\\usepackage{graphicx}\n\
\\usepackage{placeins}\n\
\\usetikzlibrary{calc}\n\
\\textheight=180truemm\n\
\\textwidth=260truemm\n\
\\begin{document}\n\
"

FILE_END=\
"\
\\end{document}\n\
"



NOT_TASKS = ["name", "surname"]

MAX_COL_COUNT = 25


def split_to_task_and_subtask(name):
	if name.lower() in NOT_TASKS:
		return name, ''
	task = ""
	subtask = ""
	for c in name:
		if c.isdigit():
			task += c
		else:
			subtask += c
	return task, subtask

def split_to_subtasks(task_names):
	tasks = dict()
	keys = []
	for name in task_names:
		number, string = split_to_task_and_subtask(name)
		if not number in tasks:
			tasks[number] = []
			keys.append(number)
		tasks[number].append(string)
	return keys, tasks

def escape_characters(s):
	return s.replace('_', '\_')

class generate_tex_table_string:
	def __init__(self, col_names, name=""):
		self.__col_count = len(col_names)

		self.__str = "\\begin{table}[!tbph]\n"
		self.__str += name + '\n\n'
		self.__str += "\\begin{tabular}{|" + '|'.join(['c'] * (len(col_names)) )  + "|}\n"
		self.__str += "\\hline\n"

		numbers, tasks = split_to_subtasks(col_names)
		number_strings = []
		for n in numbers:
			number_strings.append("\multicolumn{%d}{ |c| }{%s}" % (len(tasks[n]),n))
		self.__str += "&".join(number_strings) + "\\\\\n"

		self.__str += "\\hline\n"

		subtask_stings = []
		for n in numbers:
			subtask_stings += tasks[n]
		self.__str += "&".join(subtask_stings) + "\\\\\n"

		self.__str += "\\hline\n"


	def add_row(self, value_list):
		values = value_list + [''] * (self.__col_count - len(value_list))
		values = [escape_characters(v) for v in values]
		self.__str += "&".join(values) + "\\\\\n"
		self.__str += "\\hline\n"

	def get_table_string(self):
		return self.__str + "\\end{tabular}\n\\end{table}\n\\FloatBarrier\n"

def read_csv(file_path):
	table = csv.reader(open(file_path, 'r'), delimiter='\t')

	#unite name and surname
	new_rows = []
	for row in table:
		if len(row) < 2:
			print(row, file_path)
		new_row = [row[0] + ' ' + row[1]] + row[2:]
		new_rows.append(new_row)

	return new_rows

def get_needed_rows(table, needed_rows):
	for i in range(len(table)):
		row = list(table[i])
		if i == 0 or row[0] in needed_rows:
			yield row

def table_to_tex(table, name):
	table = list(table)
	col_names = table[0]
	table_string_generator = generate_tex_table_string(col_names, name)
	for row in table[1:]:
		table_string_generator.add_row(row)

	return table_string_generator.get_table_string()

def wide_table_to_tables(table):
	table = list(table)
	tasks_count = len(table[0]) - 1
	subtables_count = tasks_count // MAX_COL_COUNT + 1
	subtables = []
	for i in range(subtables_count):
		subtables.append([])
	for row in table:
		pupil_name = row[:1]
		for i in range(subtables_count):
			begin = 1 + (tasks_count * i // subtables_count)
			end = 1 + (tasks_count * (i + 1) // subtables_count)
			new_row = pupil_name + row[begin:end]
			subtables[i].append(new_row)

	return subtables

def tables_to_string_with_tex(tables, names, tables_on_different_pages=False):
	s = FILE_START
	for t, name in zip(tables, names):
		t = list(t)
		subtables = wide_table_to_tables(t)
		for i in range(len(subtables)):
			if len(subtables) > 1:
				suffix = str(i + 1)
			else:
				suffix = ""
			sub = subtables[i]
			s += table_to_tex(sub, name + suffix)
			s += "\n"
			if tables_on_different_pages:
				s += "\\clearpage\n"
	s += FILE_END
	return s

def save_to_file(str, file_path):
	f = open(file_path, 'w')
	f.write(str)
	f.close()

def get_table_name(path):
	return path.split('/')[-1][:-4]

def generate_tex_files(all_files, root):
	tables = []
	names = []

	for path in all_files:
		TRY_COUNTS = 2
		for i in range(TRY_COUNTS):
			try:
				tables.append(read_csv(path))
				names.append(get_table_name(path))

				pivot_sheet = get_needed_rows(tables[-1], PUPILS_NAMES)
				s = tables_to_string_with_tex([pivot_sheet], [names[-1]])
				save_to_file(s, root + '/' + BY_LIST_RESULTS_DIR + names[-1] + '.tex')

				break
			except:
				print(traceback.format_exc())
				print("problem with file " + path + ". Trying to resave")
				resave.resave(path)

	for table_name, needed_rows in PIVOT_TABLES.items():
		pivot_sheets = [get_needed_rows(t, needed_rows) for t in tables]
		s = tables_to_string_with_tex(pivot_sheets, names, table_name=="Common")
		save_to_file(s, root + '/' + PIVOT_DIR + table_name + '.tex')

	for pupil in PUPILS_NAMES:
		pivot_sheets = [get_needed_rows(t, [pupil]) for t in tables]
		s = tables_to_string_with_tex(pivot_sheets, names)
		save_to_file(s, root + '/' + PERSONAL_DIR + pupil + '/' + pupil + '.tex')

def parse_args():
    parser = argparse.ArgumentParser(description='Finds csv files and generates tex pivot tables for them')
    parser.add_argument('-r', '--root', type=str, default="/home/sav/", help = "root dir for file searching")
    parser.add_argument('-d', '--debug', action='store_true', help = "debug mode. Stops working if error occurs")
    return parser.parse_args()

def main():
	parser=parse_args()
	watch_dirs = [os.path.join(parser.root, d) for d in WATCH_DIRECTORIES]
	watcher = file_changes_watcher.file_changes_watcher(watch_dirs, ".tex", stopwords=STOPWORDS)
	while True:
		try:
			if watcher.is_smth_changed():
				generate_tex_files(sorted(watcher.get_all_files()), root)
		except Exception as e:
			print(traceback.format_exc())
			if parser.debug:
				raise e
		time.sleep(1)


if __name__ == "__main__":
    main()
