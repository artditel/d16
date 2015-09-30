#-*- coding: utf-8 -*-
import argparse
import csv
import os
import shutil
import subprocess
import sys
import time
import traceback
import file_changes_watcher

WATCH_DIRECTORIES = ['/home/sav/Dropbox/d16-calculus', '/home/sav/Dropbox/d16-programming']
STOPWORDS = ['related']
WAIT_TIME = 10

from csv_to_tex_daemon import PUPILS_NAMES

class TaskInfo:
	ITEMS_NAMES = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
	def __init__(self, num, difficulty=0):
		self.num = num
		self.difficulty = difficulty
		self.items_difficulties = []
	def add_item(self, difficulty=0):
		self.items_difficulties.append(self.difficulty + difficulty)
	def get_items_strings(self):
		if len(self.items_difficulties) == 0:
			return [str(self.num) + '*' * self.difficulty]
		return ["{num}{item}{diff}".format(
			                                   num=self.num,
			                                   item=self.ITEMS_NAMES[i],
			                                   diff='*' * diff
		                                   ) for i, diff in enumerate(self.items_difficulties)]

def get_task_message_parts(task_message):
	parts = task_message.split('_')
	num = int(parts[1])
	difficulty = len(parts[2])
	return num, difficulty

def read_tasks(log_path):
	tasks = {}
	with open(log_path, encoding="cp1251") as log:
		words = log.read().split()
		for w in words:
			if w.startswith('TaskFound'):
				num, difficulty = get_task_message_parts(w)
				tasks[num] = TaskInfo(num, difficulty)
			elif w.startswith('TaskItemFound'):
				num, difficulty = get_task_message_parts(w)
				tasks[num].add_item(difficulty)
	return tasks

def save_tasks_to_csv(tasks, csv_path):
	header = ["", ""]
	for key in sorted(tasks.keys()):
		header += tasks[key].get_items_strings()

	with open(csv_path, 'w') as csv_out:
		writer = csv.writer(csv_out, delimiter='\t')
		writer.writerow(header)
		for p in PUPILS_NAMES:
			row = p.split() + [""]*(len(header) - 2)
			writer.writerow(row)

def gen_csv(log_path, csv_path):
	tasks = read_tasks(log_path)
	save_tasks_to_csv(tasks, csv_path)

def make_pdf(file_path):
	directory, file_name = os.path.split(file_path)
	log_name = file_name[:-4] + '.log'
	pdf_name = file_name[:-4] + '.pdf'
	log_path = file_path[:-4] + '.log'
	pdf_path = file_path[:-4] + '.pdf'
	csv_path = file_path[:-4] + '.csv'

	try:
		os.remove(pdf_name)
	except FileNotFoundError:
		pass

	subprocess.call('iconv -f utf-8 -t cp1251 ' + '"' + file_path + '" > "' + file_name + '"', shell=True)
	p = subprocess.Popen(['pdflatex', '-shell-escape', '-halt-on-error', '"' + file_name + '"'])
	try:
		p.wait(WAIT_TIME)
	except subprocess.TimeoutExpired:
		pass

	if os.path.exists(pdf_name):
		print("success")
		try:
			os.remove(log_path)
		except FileNotFoundError:
			pass
		shutil.move(pdf_name, pdf_path)
		gen_csv(log_name, csv_path)
	else:
		print("error")
		shutil.move(log_name, log_path)

def parse_args():
    parser = argparse.ArgumentParser(description='Finds new tex-files and pdflatexs them')
    parser.add_argument('-r', '--root', type=str, default="/home/sav/", help = "root dir for file searching")
    parser.add_argument('-d', '--debug', action='store_true', help = "debug mode. Stops working if error occurs")
    return parser.parse_args()

def main():
	parser=parse_args()

	watch_dirs = [os.path.join(parser.root, d) for d in WATCH_DIRECTORIES]
	watcher = file_changes_watcher.file_changes_watcher(watch_dirs, ".tex", stopwords=STOPWORDS)

	while True:
		try:
			for file_path in watcher.get_changed_files():
				make_pdf(file_path)
		except Exception as e:
			print(traceback.format_exc())
			if parser.debug:
				raise e

		time.sleep(1)

if __name__ == "__main__":
    main()
