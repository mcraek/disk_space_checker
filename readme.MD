## Program Name 
disk_space_checker

## Summary
Determines based on user defined or default thresholds, whether or not each partition on a system is in a 
critical / warning or non-critical / warning state based on the amount of free space available.

**Tested with Python 3.8.1**
** Designed for Windows systems only **

## Setup
1. Create and activate your virtual environment
2. Install requirements with pip install -r requirements.txt
3. Call main program via disk_space_checker.py


## Author
Kyle McRae


## Arguments
-ct, --checktype {critical, warning}, default = critical: Specifies how thresholds should be calculated for 
each partition. Critical sets the most strict thresholds

-dpt, --datapercentthreshold {int,%}, default = **See below**: Allows specifying an alternate percentage of 
overall partition space to determine data partition status. Overall status is taken as the lesser of this or 
the data size threshold in GB

-dst, --datasizethreshold {int,GB}, default = **See below**: Allows specifying an alternate amount of free space
in GB partition space to determine data partition status. Overall status is taken as the lesser of this or the 
data size % threshold

-i, --include {str, comma-separated list}; e.g., --include c,e: Allows specifying only certain partitions should
be checked instead of all partitions by default 

-sid, --systemisdata {true, false}, default = false: If true, the OS partition will use data partition thresholds 
instead of system partition to calculate the overal status of the partition

-st, --systemthreshold {int}, default = **See below**: Allows specifying an alternate threshold in GB that 
should be used for determining the system partition status 


# Explanation of thresholds used for checks

## Critical thresholds:
- By default a system partition is considered critical if it falls below 15 GB disk space

- By default a data partition is considered critical if it falls below the lesser of 15 % total partition size 
or 30 GB. This way a 3 TB drive with 15 % free disk space (450 GB) is not considered critical until it falls below 
30 GB

## Warning thresholds:
- By default a system parition is considered to be in a warning state if it falls below 30 GB disk space

- By default a data partition is considered to be in a warning state if it falls below the lesser of 40% total 
partition size or 60 GB. A 3 TB partition with 40% free space (1.2 TB) will not be considered to be in a warning 
state until it hits 60 GB

## Important note re: Default checks and using custom thresholds
- If a user specifies no argument when running the executable, the default check performed is a critical check 
with the default thresholds described above

- The -st, -dpt, and -dst arguments described above allow the user to specify alternate thresholds that should be 
used for determining whether system / data partitions are in a critical state

- The -ct argument allows the user to instead run a warning check against each partition

- If the -sid argument is specified as True, system partitions are calculated using data partition thresholds


# Examples

## Usage Example 1: Viewing critical paritition disk space status based on default thresholds

python .\disk_space_checker.py - Checks system against default thresholds

- Once complete, the program displays in the console whether or not all partitions are good or if any are in a 
critical state per default tresholds defined above

## Usage Example 2: Specifying custom thresholds

python .\disk_space_checker-py -st 50 -ct warning - Checks system partition setting the threshold to 50 GB and check type to warning

## Usage Example 3: Specifying specific partitions to check on a system

- You may not want to check all paritions by defualt on a system

- By specifying the -i, --include argument you can specify which particular partitions should be checked;

e.g., python .\disk_space_checker.py --include c e

- Do not include : symbols or commas. Each parition you wish to check should be separated by a space

   
## Meta

Distributed under the GNU Lesser General Public License (LGPL 3)+. See LICENSE file for more information.