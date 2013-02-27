# contribution.sh
# version: 0.01
#
# author: Minto Joseph
# email: mintojoseph@gmail.com
# Script to see the major contributors in rpm based distriutions (Package Maintainers, Developers). 
#!/bin/bash
for i in `rpm -qa`
	do
	rpm -q $i --changelog|grep \*|grep \@|awk '{print $6 " "$7}'>>.contributors
	done
cat .contributors|sort | uniq -c | sort -nr|head
rm -rf .contributors
