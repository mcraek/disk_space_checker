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

	Description: 	Receives the information on all partitions on the system calculated by the calculate_partition_status function. It handles this dictionary
                    by searching for any partitions with a "Warning" or "Critical" status, and adds them to a list. This list is then returned back to the
                    main program.

                    If there are no critical / warning partitions found, "None" is returned

                    If -i, --include argument was specified, this will output only the partitions specified by the user 

'''

def find_triggered_partitions(partitions,arguments_received):

    # Import built-in functions

    import time

    # Excellent explanation of searching nested dicitonaries here: https://www.reddit.com/r/learnpython/comments/2ttuwa/python_27_searching_nested_dictionary/

    triggered_partitions = [] # Initialize empty list of partitions with critical disk space

    # Define list of partitions to be checked if -i, --include argument was specified by the user
    # If -i or --include was not specified, all partitions are checked

    if arguments_received['target partitions'] != None:
        
        targets_specified = True

        # In order to properly match these up below, we need to format parittions so they're labelled as such: X:, Y:, Z:, instead of X, Y, Z
        
        specified_partitions = [] # Initialize empty list to store the formatted parition labels
        
        for partition in arguments_received['target partitions']:

            label = str(partition) + ':'
            specified_partitions.append(label)

    else:

        targets_specified = False

    # Define type of check being done to set partition status accordingly: Warning / Critical as needed

    if arguments_received['check type'] == None:

        check_type = 'critical' # Sets default check to critical

    elif arguments_received['check type'] == 'warning':

        check_type = 'warning'

    elif arguments_received['check type'] == 'critical':

        check_type = 'critical'

    # Find critical / warning partitions depending on argument passed to program

    # Critical partitions

    if check_type == 'critical':

        if targets_specified == True:

            for partition in partitions: # Note: Grabbing "partition" here pulls the label; e.g., E:

                if partitions[partition]['Partition status'] == 'Critical' and partition in specified_partitions:

                    triggered_partitions.append(partition)

        else:

             for partition in partitions:
                
                if partitions[partition]['Partition status'] == 'Critical':
                    
                    triggered_partitions.append(partition)

        
    # Warning partitions

    else:

        if targets_specified == True:

            for partition in partitions:

                if partitions[partition]['Partition status'] == 'Warning' and partition in specified_partitions:

                    triggered_partitions.append(partition)

        else:

            for partition in partitions:

                if partitions[partition]['Partition status'] == 'Warning':

                    triggered_partitions.append(partition)            

    # Return findings / Output file if triggered partition found

    if len(triggered_partitions) > 0:

        return triggered_partitions
    
    else:
        
        return None
