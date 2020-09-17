#!../bin/env/Scripts python

'''

						//----------// LICENSING //----------//

			This file is part of the test_internet_speed program and is free software:
			you can redistribute it and/or modify it under the terms of the
			GNU General Public License as published by the Free Software Foundation,
			either version 3 of the License, or (at your option) any later version.
			This program is distributed in the hope that it will be useful,
			but WITHOUT ANY WARRANTY; without even the implied warranty of
			MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
			GNU General Public License for more details.
			You should have received a copy of the GNU General Public License
			along with this program. If not, see <https://www.gnu.org/licenses/>.

						//----------// LICENSING //----------//

	Description: 	Main program which calls all other scripts as part of this module and determines the overall
					flow control of the program.

'''

# //--- Debug --- // #
# Copy and paste the following line into PoSh to test running the program using your virtual environment directly from the console in Code

# & "D:\Scripts\Python\disk_space_checker\bin\env\Scripts\python.exe" "D:\Scripts\Python\disk_space_checker\disk_space_checker\disk_space_checker.py"

# //--- Debug --- // #

def disk_space_checker():

	# Import built-in functions

	import sys # Required for determining if arguments have been passed to this program via commandline
	import time # Required for running sleep function

	# Import functions from other Python files part of this module

	from check_arguments 				import check_arguments					# Checks arguments passed to program
	from collect_partitions 			import collect_partitions 				# Stores info on ea. partition on the system (name, size, free space, etc.)
	from calculate_partition_thresholds import calculate_partition_thresholds 	# Determines status of ea. partition based on free space available
	from calculate_partition_status 	import calculate_partition_status 		# Determines partition status based on threshold calculated vs. amount of free space
	from find_triggered_partitions 		import find_triggered_partitions 		# If any paritions are in a critical status, this will output / return them. Otherwise returns None
	from summarize_results				import summarize_results				# Outputs results of check to console
	from output_console_messages		import output_console_messages			# Outputs messages to console to user for summarizing type of check to be done

	# Check / Handle arguments passed to program, also set default values here for parameters if necessary

	arguments_received = vars(check_arguments()) 	# Parse arguments submitted to program and store them into a variable
													# This is used to pass the arguments to further commands below.
													# If the user executes the program with no arguments passed. This will
													# set default values.
													# Important note: Do not pass sys.argv to argparse. It automatically
													# handles this, and passing sys.argv just confuses / breaks things with it

	# Output starting console messages to user summarizing check type

	output_console_messages(arguments_received)

	# Program Start - Collect partition info
	
	print('\nCollecting partition info...')
	time.sleep(2)
	partition_info = collect_partitions(arguments_received)

	# If --include specified and a specified partition doesn't exist on the system, end program

	if arguments_received['target partitions'] != None:

		for partition in arguments_received['target partitions']:

			label = str(partition) + ':'

			if label not in partition_info:

				print('\nCould not find the ' + label + ' partition. Please make sure you specify valid paritions for this argument in the following format: -i x y z or --include x y z. Terminating program...')
				time.sleep(10)
				exit()

	# Calculate free space threshold for ea. partition on the system

	time.sleep(2)
	print('\nCalculating partition free space threshold(s)...')
	time.sleep(2)
	partition_thresholds = calculate_partition_thresholds(partition_info,arguments_received)

	# Determine partition status based on threshold vs. amount of free space remaining

	time.sleep(2)
	print('\nDetermining partition status based on calculated threshold vs. amount of free space remaining...')
	time.sleep(2)
	partition_info_with_status = calculate_partition_status(partition_thresholds,arguments_received) # Pass collected partition info and calculated thresholds

	# Find critical / warning partitions
	# If -i, --include argument was specified, this will check only those partitions

	triggered_partitions = find_triggered_partitions(partition_info_with_status,arguments_received)

	# Summarize / Output results to console
	
	summarize_results(triggered_partitions,arguments_received)
	
# Execute the program

disk_space_checker()