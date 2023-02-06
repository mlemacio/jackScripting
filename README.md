# Jack Scripting

Just a small example to help my friend access remote data in an automated fashion. Ended up being a decent example of a script. It can either execute all the commands or generate the list of commands that need to be run

mkdir CIC-000001
mkdir CIC-000002

sftp CIC-000001:/home/pi/Desktop/cambridge-ic-spi/logs/cic-data.txt CIC-000001/2023-02-06.txt
sftp CIC-000002:/home/pi/Desktop/cambridge-ic-spi/logs/cic-data.txt CIC-000002/2023-02-06.txt