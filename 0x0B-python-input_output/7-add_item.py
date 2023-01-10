#!/usr/bin/python3
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

a = []

for i in range(1, len(sys.argv)):
    try:
        a = load_from_json_file('add_item.json')
    except FileNotFoundError:
        pass
    finally:
        a.append(sys.argv[i])
        save_to_json_file(a, 'add_item.json')
    
