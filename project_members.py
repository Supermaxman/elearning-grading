
import os
import docx
import re
import argparse
import pdfplumber


def get_pdf_txt(file_path):
	# creating a pdf file object
	text = []
	with pdfplumber.open(file_path) as pdf:
		for page in pdf.pages:
			page_text = page.extract_text()
			text.append(page_text)
	return '\n'.join(text)


def get_word_txt(file_path):
	doc = docx.Document(file_path)
	text = []
	for para in doc.paragraphs:
		text.append(para.text)
	return '\n'.join(text)


netid_pattern = re.compile(r'[A-Za-z]{3}\d{6}')


def get_net_ids(text):
	netids = set()
	ordered_ids = []
	for netid in netid_pattern.findall(text):
		netid = netid.lower()
		if netid in netids:
			continue
		ordered_ids.append(netid)
		netids.add(netid)
	return ordered_ids


def collect_ids(root_dir):
	for file in os.listdir(root_dir):
		file_path = os.path.join(root_dir, file)
		try:
			if file_path.endswith('.pdf'):
				file_text = get_pdf_txt(file_path)
			elif file_path.endswith('.docx'):
				file_text = get_word_txt(file_path)
			else:
				print(f'UNKNOWN FILE FORMAT: {file_path}')
				continue
		except Exception as e:
			print(f'ERROR READING {file_path}: {e}')
			continue
		file_ids = get_net_ids(file_text)
		print(f'{file}:')
		for netid in file_ids:
			print(f'  {netid}')
		print()


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("root_dir", type=str)
	args = parser.parse_args()
	collect_ids(args.root_dir)
