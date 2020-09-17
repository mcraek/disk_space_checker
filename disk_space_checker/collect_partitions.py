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

	Description: 	Pulls ea. partition form the system and determines whether it's a data
                    or system drive based on whether or not the OS is installed on that
                    partition.

                    Calculates in GB the total partition size, total space remaining, and
                    drive letter of each partition.

                    This information is returned to the main program to pass to other functions
                    for performing other calculations with this information

'''

# Note: Install wmi module with "pip install wmi". You'll likely also need to run "pip install pywin32" as well to work with the module

'''
    Helpful note on using wmi queries with Python:
    https://technet.microsoft.com/en-us/windows/aa394084(v=vs.60) has a list of all Win32 classes and their attributes; e.g., find partitions
    within the Operating System Classes section rather than Hardware-related objects. 
    
    This is really useful for determining what properties a class has such as the Win32_LogicalDisk class which has a FreeSpace attribute we can access.

    WMI / Win32 queries can be used for obtaining / interacting with a variety of things on the system from the OS, to drivers, services, devices, etc.
'''

def collect_partitions(arguments_received):

    import time
    import os # Provides access to environment variables so we can query and find the system drive
    import wmi # Lets us query info on each partition
    wmi_connection = wmi.WMI() # Establish WMI connection with local system. Now we can execute various WMI Queries

    # Store information on each partition 

    partitions = {} # Initiallize empty nested dictionary to store partition info

    # First determine the System partition

    system_partition = str(os.getenv('SystemDrive')) # Convert to string so we can compare this to another value

    # Add information of each partition to the disks dictionary created above

    for partition in wmi_connection.Win32_LogicalDisk():
    
        if partition.Description == 'Local Fixed Disk': # Omit any detachable storage

            # Store info on the partition
            partition_letter = str(partition.DeviceID) # Convert to string so we can compare this to another value
            
            total_size = (int(partition.Size)) / 1073741824 # Convert bytes to GB
            total_size_rounded = round(total_size) # Round to nearest whole number
            
            free_space = (round(int(partition.FreeSpace)) / 1073741824)
            free_space_rounded = round(free_space)
            
            percent_free = (free_space_rounded / total_size_rounded) * 100
            percent_free_rounded = round(percent_free)

            # Set partition type to system or data. Depending on arguments passed to the program, set the system
            # partition to data to use data partition thresholds instead

            if partition_letter == system_partition and arguments_received['system is data partition'] != 'true':
                partition_type = 'System'
            else:
                partition_type = 'Data'

            # Create dictionary to store info on the partition

            partition_info = { 
                
                partition_letter : {

                    'Partition Type' : partition_type,
                    'Total size (GB)' : total_size_rounded,
                    'Free space (GB)' : free_space_rounded,
                    'Percent free' : percent_free_rounded

                } 

            }

            # Add the dictionary of info the dictionary containing info on all partitions

            partitions.update(partition_info)

    # Return dictionary for other scripts to reference

    return partitions