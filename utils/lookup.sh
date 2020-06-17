#!/bin/bash

if [ $# != 2 ]; then
  echo -e "\
    Usage:
     $./lookup.sh ./list.txt wordpress
     $./lookup.sh ./list.txt ghs.l.google
     $./lookup.sh ./list.txt 72.14.203.121 # ghs
     $./lookup.sh ./list.txt 67.207.139.81 # Posterous
     $./lookup.sh ./list.txt 72.32.231.8   # Tumblr
     $./lookup.sh ./list.txt typepad
  ";
  exit 1;
fi

while read line; do
  host=$( echo "$line" |
    grep -oE "[a-z0-9]([a-z0-9_\.\-]*[a-z0-9])?\.[a-z]{2,4}" |
    grep -vE "(aspx?|dotn|exe|fan|html?|php|zh)$"
  );
  [ "$host" ] && [ "$(nslookup $host | grep -i $2)" ] && echo $host;
done < "$1"

