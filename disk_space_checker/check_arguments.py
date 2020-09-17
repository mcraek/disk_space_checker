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

	Description: 	Receives / validates arguments passed to the main program and sets defaults in the event
                    certain arguments are not passed to the program.

                    From the main program, pass arguments from sys.argv to here after subtracting the first argument from the list
                    (main program name)

                    Arguments pass are case insensitive

'''

# This can be your default in how to handle arguments passed to programs for future projects

def check_arguments():

    import argparse # Used for parsing arguments passed to program

    # Specify valid argumnets for program and set default values accordingly

    parser = argparse.ArgumentParser(description='Calculate free space status on each partition for the system')
    
    parser.add_argument('-ct', '--checktype', dest='check type', default='critical', choices=['critical','warning'], type=str.lower,
                        help="Type of check to perform. Specify warning or critical")
    
    parser.add_argument('-sid', '--systemisdata', dest='system is data partition', default='false', choices=['true','false'], type=str.lower,
                        help='use data partition threshold for the system partition')
    
    parser.add_argument('-st', '--systemthreshold', dest='system threshold limit (GB)', type=int,
                        help='specify alternate system partition threshold in GB to utilize for check')

    parser.add_argument('-dpt', '--datapercentthreshold', dest='data threshold limit (% total drive space)', type=int,
                        help='specify alternate percent free data partition threshold to use. threshold used will be lesser of the following: data percent thresold / data size threshold')

    parser.add_argument('-dst', '--datasizethreshold', dest='data threshold limit (GB)', type=int,
                        help='specify alternate data partition threshold in GB to utilize for check. threshold used will be lesser of the following: data percent thresold / data size threshold')
    
    parser.add_argument('-i', '--include', nargs='+', dest='target partitions', type=str.upper, # nargs+ allows specifying multiple values to an argument
                        help='specify target partitions to include in the check; e.g., c,e,f. by default, all partitions are checked, but this allows defining specific targets')


    # If no arguments were not passed to the program, use the defaults

    #if len(arguments) > 1:

    #passed_arguments = parser.parse_args('-cwc false')

    # If arguments were passed to the program, parse these and add to the list of arguments to return

    #else:

    passed_arguments = parser.parse_args() # Validate arguments passed to program against above permitted arguments
    
    # Return validated arguments to main program so it can pass them to other functions that may use them

    return passed_arguments