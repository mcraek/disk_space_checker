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

	Description: 	Receives any triggered / warning status partitions and outputs these to console.
                   
'''

def summarize_results(triggered_partitions,arguments_received):

    import time


    # Define ype of check being done.

    if arguments_received['check type'] == 'critical':

            check_type = 'Critical'

    elif arguments_received['check type'] == 'warning':

        check_type = 'Warning'

    else:

        check_type = 'Critical'

    if triggered_partitions == None:

        # Set partition_status to good

        partition_status = 'Good'

        time.sleep(2)
        print('\nFree space status for all partitions is good!\n')
        time.sleep(2)
	
    # For any triggered partitions, set check to critical / warning depending on arguments passed to program & output results to console

    else:

        time.sleep(2)
        print('\nThere is at least one partition with free space less than the ' + str(check_type) + ' threshold! Here they are: \n')
        time.sleep(2)

        for partition in triggered_partitions:

            print(partition)
            
            time.sleep(1)