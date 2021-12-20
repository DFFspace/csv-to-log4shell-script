# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ***************************************************************************************************
# Script:             csv_2_log4shell.py
# Create Date:        18-12-2021
# Author:             Pasquale D.
# Description:        Convert a CSV file to log4shell markdown tables 
#                     
#
#                    
# ***************************************************************************************************
# SUMMARY OF CHANGES
# Date(dd-mm-yyyy)    Author              Comments
# ------------------- ------------------- -----------------------------------------------------------
# 18-12-2021          Pasquale D. 	  Initial Release
# 20-12-2021          Pasquale D. 	  Added other CVE rows									  
# 
# ***************************************************************************************************
import csv

# Enter the path to the csv file
csv_path = ""

# Enter the path to save the new text file
text_file = ""
statuses = ['Vulnerable', 'Fix', 'Workaround', 'Not vuln', 'Investigation']

with open(csv_path, mode='r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	next(csv_reader, None)
	for row in csv_reader:
		supplier, product, version, status_cve_2021_4104, status_cve_2021_44228, status_cve_2021_45046, status_cve_2021_45105, notes, link = row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
		with open(text_file, 'a') as f:
			f.write(f"| {supplier} | {product} | {version} | {status_cve_2021_4104} | {status_cve_2021_44228} | {status_cve_2021_45046} | {status_cve_2021_45105} | {notes} | [source]({link}) |\n")
