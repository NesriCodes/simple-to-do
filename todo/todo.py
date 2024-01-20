"""this is a to do app"""
# January 19, 2023

import json
import os


print('''Welcome to our humble to-do list app.
	** you don\'t have to use 'a' character to start adding item at the beginning
	- "a" to add item to the to-do list. It will give you the key word 'add' to indicate you start adding items. you can add more than one item by using "enter" on your keyboard.
	- "d" to delete items from our to-do. you can delete more than one item by using "enter" on your keyboard.
	- "m" to mark items as done in our to-do. you can mark more items from your to-do by using "enter" on your keyboard.''')

todo = {}

# add to-do
def add_todo():
	global todo
	
	
	adding = True
	while adding:
		todo_input = input('add: ')
		todo[todo_input] = False

		if todo_input == 'q':
			del todo['q']
			adding = False

		if todo_input == 'd':
			del todo['d']
			delete_todo()

		if todo_input == 'm':
			del todo['m']
			markas_done()

		if todo_input == 'p':
			del todo['p']
			print_done()
	

# delete to-do
def delete_todo():
	global todo

	if len(todo) == 0:
		print('\nYour to-do is empty please add at least one item.\n')
	while todo:
		delete_input = input('which item do you want to delete: ')
		if delete_input == 'q':
			break
		if delete_input == 'p':
			del todo['p']
			print_done()

		del todo[delete_input]
		

# mark as done
def markas_done():
	global todo

	if len(todo) == 0:
		print('\nYour to-do is empty please add at least one item.\n')

	while todo:
		markas_done_input = input('which item do you want to mark as done: ')
		# if markas_done_input not in to-do:
		# 	print('Item is not in the list. please add it first.')
		# 	add_todo()
		
		if markas_done_input == 'q' :
			quit()

		# if markas_done_input == 'p':
			
		# 	print_done()

		if markas_done_input in todo:
			todo[markas_done_input] = True

		elif markas_done_input == 'p':
			print_done()
		else:
			print('\nItem is not in the list. please add it first.\n')
			choose_input = input(f'''Do you want to add "{markas_done_input}" to your item list? (y/n). if you choose "y" it will be marked as done.
				* Enter "a" if you want to just "add" item.''')
			if choose_input == 'y':
				todo[markas_done_input] = True

			elif choose_input == 'n':
				continue

			elif choose_input == 'a':
				add_todo()

			else:
				print('Please insert only "y" - yes or "n" for no.')


	

# save 
def print_done():
	global todo

	print(f'you have done the following items\n')

	for key, value in todo.items():
		if value == True:
			print(f'\t-{key}')


		elif value == None:
			print('No progress yet.')
	print()

add_todo()
