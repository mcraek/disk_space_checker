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


	Description: 	Receives the calculated partition thresholds that are used for determining the status of ea. partition.
                    Depending on whether the type of check being done is a Critical or Warning check, this will set the
                    status of ea. partition to Good, Warning, or Critical and return these statuses to the main program.

'''

def calculate_partition_status(partitions,arguments_received):

    import time

    # Determine if partition status is Good or Critical based on calculated thresholds

    for partition in partitions:

        # First store the free space and thresholds as integers

        partition_name = str(partition) 
        partition_all_stats = partitions[partition_name]

        partition_threshold = int(partition_all_stats['Partition free space threshold (GB)'])
        partition_free_space = int(partition_all_stats['Free space (GB)'])

        # If free space is less than the threshold, set partition status to critical / warning depending on argument passed to program

        # Critical partitions  

        if arguments_received['check type'] == 'critical':

            if partition_free_space < partition_threshold:

                partition_status = 'Critical'

            else:

                partition_status = 'Good'

        # Warning partitions

        else:

            if partition_free_space < partition_threshold:

                partition_status = 'Warning'

            else:

                partition_status = 'Good'

        # Add partition status to original collection of info

        partitions[partition]['Partition status'] = partition_status

    # Return updated partition information including Status

    return partitions
         