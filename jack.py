import os
from datetime import date

# Create immutable variables
TEST_NAMES = ["CIC", "EMT", "LST", "MAT", "PSA", "SLT"]
TEST_TOTAL = [2, 12, 1, 3, 1, 7]

SFTP_STRING = "sftp"
MKDIR_STRING = "mkdir"

DATA_REMOTE_PATH = ":/home/pi/Desktop/cambridge-ic-spi/logs/cic-data.txt"
TODAY_STRING = str(date.today())

# Generate list of ip names to grab data from
ip_list = []

for idx, source in enumerate(TEST_NAMES):
    # Grab each tests specific number of instances
    num_sources_with_name = TEST_TOTAL[idx]

    # For each instance of each test, add it to ip list
    for i in range(1, num_sources_with_name + 1):
        number_string = "%06d" % (i,)
        source_string = source + "-" + number_string

        ip_list.append(source_string)

for ip in ip_list:
    # Make a directory for every machine if it doesn't exist
    make_directory_string = MKDIR_STRING + " " + ip
    print(make_directory_string)
    '''os.system(make_directory_string)'''

for ip in ip_list:
    # Create local file path, consisting of directory name and todays date
    LOCAL_FILE_PATH = ip + "/" + TODAY_STRING + ".txt"

    # SFTP a file from a raspberry pi into it's respective directory
    SFTP_command = SFTP_STRING + " " + ip + DATA_REMOTE_PATH + " " + LOCAL_FILE_PATH
    print(SFTP_command)
    '''os.system(SFTP_command)'''
