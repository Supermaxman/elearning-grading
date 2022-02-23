
import os
import re
import argparse
from collections import defaultdict
import shutil

import pandas as pd



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


def collect_team_files(team_map, root_dir):
	team_files = defaultdict(list)
	for file in os.listdir(root_dir):
		file_path = os.path.join(root_dir, file)
		if file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.zip'):
			netids = get_net_ids(file)
			if len(netids) == 1:
				netid = netids[0]
				team_id = team_map[netid]
				team_files[team_id].append(file_path)
			elif len(netids) > 1:
				print(f'ERROR: File {file} has multiple netids!')
			else:
				print(f'ERROR: File {file} has no netids!')
		else:
			continue
	return team_files


def load_teams(team_file):
	df = pd.read_excel(team_file)
	df = df[['Username', 'Team']].set_index('Username')
	df = df.to_dict()['Team']
	return df


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("root_dir", type=str)
	parser.add_argument("team_file", type=str)
	parser.add_argument("out_dir", type=str)
	args = parser.parse_args()
	team_map = load_teams(args.team_file)
	team_files = collect_team_files(team_map, args.root_dir)

	out_dir = args.out_dir
	if not os.path.exists(out_dir):
		os.mkdir(out_dir)
	for team_id, t_files in team_files.items():
		for f_idx, file_path in enumerate(t_files):
			f_name = f'team-{team_id}'
			if f_idx != 0:
				f_name = f'{f_name}-{f_idx}'
			file_type = os.path.splitext(file_path)[-1]
			f_name = f'{f_name}{file_type}'
			new_file_path = os.path.join(out_dir, f_name)
			# print(f'{team_id}-{f_idx} ({file_path} -> {new_file_path}')
			shutil.copy(file_path, new_file_path)


if __name__ == '__main__':
	main()
