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

	Description: 	Outputs messages to console depending on arguments passed to program

'''

def output_console_messages(arguments_received):

    import time

	# Output message re: Type of check being performed (Critical or Warning)

    if arguments_received['check type'] == 'critical':

        check_type = 'Critical'

    else:

        check_type = 'Warning'

    print('\nCalculating disk space status for local system using the following threshold: ' + str(check_type))

    time.sleep(2)

	# Output message re: Partitions being checked

    if arguments_received['target partitions'] == None:

        print('\nAll partitions will be checked')

    else:

        print('\nThe following partitions will be checked:\n')

        for partition in arguments_received['target partitions']:

            time.sleep(1)
            print (partition + ':')

    time.sleep(2)

    # Output message re: System partition is also used for data, data thresholds will be used

    if arguments_received['system is data partition'] == 'true':

        print('\nSystem partition classified as data partition. Threshold for the system partition will use "data" partition type threshold')

        time.sleep(2)