"""this is a to do app"""
# January 19, 2023

import json
import os


print('''Welcome to our humble to-do list app.
	** you don\'t have to use 'a' character to start adding item at the beginning
	- "a" to add item to the to-do list. It will give you the key word 'add' to indicate you start adding items. you can add more than one item by using "enter" on your keyboard.
	- "d" to delete items from our to-do. you can delete more than one item by using "enter" on your keyboard.
	- "m" to mark items as done in our to-do. you can mark more items from your to-do by using "enter" on your keyboard.
	- "s" to save your to-do''')
	

# todo = {}

# add to-do
def add_todo():
	global todo
	try:
		with open('todo.json', 'r') as f:
			todo = json.load(f)
	except (FileNotFoundError, json.JSONDecodeError):
		todo = {}

	while True:
		todo_input = input('add: ').strip()
		
		if todo_input == 'q'.lower():
			print('quitting...')
			break

		elif todo_input == 'd'.lower():
			delete_todo()

		elif todo_input == 'm'.lower():
			markas_done()

		elif todo_input == 'p'.lower():
			print_done()

		elif todo_input == 's'.lower():
			with open('todo.json', 'w') as f:
				json.dump(todo, f)
			break
		else:
			todo[todo_input] = False

# delete to-do
def delete_todo():

	with open('todo.json', 'r') as f:
		todo = json.load(f)

	if len(todo) == 0:
		print('\nYour to-do is empty please add at least one item.\n')
	else:
		while True:
			delete_input = input('which item do you want to delete: ').strip()
			if delete_input == 'q'.lower():
				break
			if delete_input == 'p'.lower():
				del todo['p']
				print_done()
			elif delete_input in todo:
				print(delete_input)
				del todo[delete_input]
				print(todo)
			else: 
				print(f'Item {delete_input} not found.')
	with open('todo.json', 'w') as f:
		json.dump(todo, f)
	
		

# mark as done
def markas_done():

	with open('todo.json', 'r') as f:
		todo = json.load(f)

	if len(todo) == 0:
		print('\nYour to-do is empty please add at least one item.\n')

	while todo:
		markas_done_input = input('which item do you want to mark as done: ').strip()
		
		if markas_done_input == 'q'.lower():
			break

		elif markas_done_input == 'p'.lower():
			print_done()

		elif markas_done_input == 's'.lower():
			with open('todo.json', 'w') as f:
				json.dump(todo, f)
			break

		if markas_done_input in todo:
			todo[markas_done_input] = True
			print(todo)

		else:
			print('\nItem is not in the list. please add it first.\n')
			choose_input = input(f'''Do you want to add "{markas_done_input}" to your item list? (y/n). 
	if you choose "y" it will be marked as done.
	* Enter "a" if you want to just "add" item.''')
			if choose_input == 'y'.lower():
				todo[markas_done_input] = True

			elif choose_input == 'n'.lower():
				continue

			elif choose_input == 'a'.lower():
				add_todo()

			else:
				print('Please insert only "y" - yes or "n" for no.')
	with open('todo.json', 'w') as f:
		json.dump(todo, f)


# save 
def print_done():

	with open('todo.json', 'r') as f:
		todo = json.load(f)

	for key, value in todo.items():
		if value == True:
			print(f'Done items\n\t-{key}')
		elif value == False:
			print(f'Not done\n\t-{key}\nto tick of your items insert "m" to the console')


		else:
			print('No progress yet.')
	print()

add_todo()
