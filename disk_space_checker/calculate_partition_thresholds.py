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

	Description: 	Receives the information on each partition from the collect_partitions function.
                    With this information, depending on whether each partition is a system or data
                    partition, will set the thresholds accordingly that will trigger a Warning
                    or Critical disk space status for each partition.

                    Thresholds are calculated based on a percentage or hard GB limit or a combination
                    of both. For example, a data partition may trigger a Critical status based on the 
                    lesser of 80 GB or 15% free disk space.

'''


def calculate_partition_thresholds(partitions,arguments_received):

    # # ///--- Debug / Notes (Unindent / uncomment contents once to run) ---///

        # print(type(partitions)) # Check that we have received a dictionary to work with
        
        # # Basics on how to access nested dictionaries 

        # try:
        #     print(partitions[0]) # Returns a "KeyError" error, need to access dictionary by name
        # except KeyError:
        #     print("Error. Try accessing dictionary values by name")

        # print(partitions['C:']) # Matching a dictionary by name works
        
        # # Let's store one of the dictionaries now

        # partition_all_stats = partitions['C:']
        # print(type(partition_all_stats)) # We are returned another dictionary
        # partition_type = partition_all_stats['Partition Type'] # Let's access one of the dictionaries values
        # print(partition_type)

        # Using this logic, we can create a for loop to iterate through each partition on the system and access
        # its key / value pairs as per what's actually run below 

    # # ///--- Debug / Notes (Unindent / uncomment contents once to run) ---///

    # Import required built-in modules

    import time

    # Set thresholds for determining status of partition based on type / free space
    # For data drives, the threshold used will be the lesser of the percentage
    # or gb free thresholds

    if arguments_received['check type'] == 'critical':

        # Set critical system partition threshold
    
        if arguments_received['system threshold limit (GB)'] == None:   # If user didn't specify this parameter (and therefore "None" is submitted), set
                                                                        # default threshold. Similar logic is used throughout this function
                                                                                               
            system_threshold = 10 # Set threshold to 10 GB

        else:

            system_threshold = arguments_received['system threshold limit (GB)']

        # Set critical data partition thresholds

        # Percent free space threshold
        if arguments_received['data threshold limit (% total drive space)'] == None:

            data_threshold_percent = 15 # Set threshold to 15 % of the total partition size

        else:

            data_threshold_percent = arguments_received['data threshold limit (% total drive space)']

        # Size threshold (GB)
        if arguments_received['data threshold limit (GB)'] == None:

            data_threshold_gb = 15 # Set threshold to 15 GB

        else:

            data_threshold_gb = arguments_received['data threshold limit (GB)']

    # Set warning thresholds (similar logic to the critical thresholds)

    else:

        # Set warning system partition threshold
    
        if arguments_received['system threshold limit (GB)'] == None:  
                                                                                             
            system_threshold = 20 # Set threshold to 20 GB

        else:

            system_threshold = arguments_received['system threshold limit (GB)']

        # Set warning data partition thresholds

        # Percent free space threshold
        if arguments_received['data threshold limit (% total drive space)'] == None:

            data_threshold_percent = 30 # Set threshold to 30% of the total partition size

        else:

            data_threshold_percent = arguments_received['data threshold limit (% total drive space)']

        # Size threshold (GB)
        if arguments_received['data threshold limit (GB)'] == None:

            data_threshold_gb = 30 # Set threshold to 60 GB

        else:

            data_threshold_gb = arguments_received['data threshold limit (GB)']
    
    # Output thresholds utilized (critical or warning)

    time.sleep(1)
    print('\nData partition threshold (GB) set to: ' + str(data_threshold_gb))
    time.sleep(1)
    print('Data partition threshold (%) set to: ' + str(data_threshold_percent))
    time.sleep(1)
    print('System partition threshold (GB) set to: ' + str(system_threshold))
    print('\n')
    time.sleep(2)
    

    # Calculate threshold for each partition

    for partition in partitions:

        partition_name = str(partition)                     # Returns C:, D:, E:, etc. and used for accessing ea. dictionary
        partition_all_stats = partitions[partition_name]    # Store all stats on the partition, now we can accesss
                                                            # ea. property value by name
        
        # Using Partition Type property and thresholds specified above, determine partition status

        # Determine which threshold limit to use if partition is used for data

        if partition_all_stats['Partition Type'] == 'Data':

            # Calculate free space threshold based on percentage limit specified above
            threshold_calculation_percentage = round(partition_all_stats['Total size (GB)'] * (data_threshold_percent / 100))

            # Set threshold for data partition to the lesser of the percentage calculation or hard limit
            if threshold_calculation_percentage < data_threshold_gb:
                threshold = threshold_calculation_percentage
            else:
                threshold = data_threshold_gb

        # Set threshold for system partition

        else:
            threshold = system_threshold

        print('Threshold for ' + partition_name + ' partition set to ' + str(threshold) + ' GB')
        
        # Add the partition's threshold to the original collection of partition info

        partitions[partition]['Partition free space threshold (GB)'] = threshold

        time.sleep(1)
       
    # Return partition info with calculated thresholds included

    return partitions