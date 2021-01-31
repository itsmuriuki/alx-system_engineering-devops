#This project is about Shell Permissions

## 0. My name is Betty
### su betty changes the user id to betty using only 8 characters. su is the command that subsitutes the user identity. It requests credentials and switches to that user ID (the default user is the superuser).

## 1. Who am I
### whoami is the command that displays the user id (identity)

## 2. Groups
### groups will show the groups the current user is part of

## 3. New owner
### chown betty hello where chown changes the file's owner and group (either are optional) owner:group file

## 4. Empty!
### touch is the command to create an empty file. touch filename

## 5. Execute
### chmod u+x hello where chmod is the command to change permission for users, group or other users. u represents user/owner and x is for executable. hello is the specific file.

## 6. Multiple Permissions
### chmod ug+x,o+r hello where a comma is used to change the permissions for two different user types. The user and group have executable permission including what they already have while all other users have read permissions as well as what they originally had

## 7. Everybody!
### chmod a+x hello where a is for all

## 8. James Bond
### chmod 007 hello where it only allows all other users all the permissions. 004(All read by others)+002(Allow write by others)+001(Allow execute for all others). Using a number forces chmod to behave in absolute mode.

## 9. John Doe
### To set file to these permissions: -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello. chmod 753 hello 400+200+100+040+010+002+001

## 10. Look in the mirror
### chmod --reference=olleh hello where this sets the mode of the file hello the same as olleh. Both files are in the working directory. chmod --reference=file 1 file2 where file2 is reference off of file1's permission

## 11. Directories
### chmod -R a+x * where -R changes the mode for all the files under the file/directory instead of the parent file/directory. * is for all files

## 12. More directories
### mkdir -m 751 dir_holberton, this script creates a directory named dir_holberton with permission 751 in the working direcory. -m Sets the file permission bits of the final created directory to the specified mode.

## 13. Change group
### chgrp holberton hello - this command changes the group owner to holberton for the file hello

## 14. Owner and group
### chown -R betty:holberton . - changes all the files and directories in the working directory to owner betty and group owner to holberton. -R allows chmod to apply to all files under the main file/directory without changing them. user:group while . represents current directory.

## 15. Symbolic links
### chown -h betty:holberton _hello where -h is used when the file being changed is a symbolic link, and this allows you to change the user ID/group ID of the link itself

## 16. If only
### chown --from=guillaume betty hello changes the file hello to user betty only if the original owner was guillaume. --from=CURRENTUSER/CURRENTGROUP newUser/newGROUP file
