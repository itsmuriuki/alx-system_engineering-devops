#This project is about Shell Commands

##0. Where am I?
### pwd command gives the absolute path name of the current working directory

## 1. What's in there?
### ls lists out the contents of the current directory

## 2. There is no place like home
### cd command changes from working to the user's home directory

## 3. The long format
### ls -l is the command that lists out the directory contents in a long format where ls lists and -l gives a long format output

## 4. Hidden Files
### ls -la is the command that lists all your files including the hidden files with (.). ls lists out the files l gives out in long format and a outputs all files

## 5. I love numbers
### ls -la -n commands outputs all files in long format while -n outputs with the group IDs displayed numerically

## 6. Welcome Holberton
### mkdir /tmp/holberton command makes the directory 'holberton' in the /tmp/ folder. The /tmp/ folder must exist for this command to work.

## 7. Betty in Holberton
### mv betty /tmp/holberton - if the file betty is in the /tmp/ folder, using the mv command moves the file into the destination, which is the holberton directory in tmp

## 8. Bye bye Betty
### rm /tmp/holberton/betty deletes the file betty from the /tmp/holberton location

## 9. Bye bye Holberton
### rm -R /tmp/holberton is the command that removes a directory

## 10. Back to the future
### cd - is the command the moves you from the working directory to the previous one. Can be used to toggle

## 11. Lists
### ls -la . .. /boot where ls -la list everything in long format and . list out the current directory, .. lists out the parent directory of the working directory and /boot lists out the contents in boot

## 12. File type
### file /tmp/iamafile where the file command outputs out the type of file iamafile is

## 13. We are symbols, and inhabit symbols
### ls -s /bin/ls _ls_ where ln creates the link and when -s is used, it crates a symbolic link

## 14. Copy HTML files
### cp -u * .html where cp is the command to copy, -u is the command to that copies only when the source file is newer than the destination or when the destination file is missing * .html is uses to get all files with the end extension of .html

## 15. Let's move
### mv [[:upper:]]* /tmp/u where mv is move and [[:upper:]] targets only files that are uppercase

## 16. Clean Emacs
### rm*~  where rm removes the files and * removes all files that ends in ~

## 17. Tree
### mkdir -p welcome/to/holberton where -p will create all the directories leading up to the given directory that does not exists

## 18. Life is a series of commas, not periods
### ls -amp where ls lists out all the files, -a lists out hidden files including (.). -m adds a comma to each entry. -p adds a slash to the end of directories