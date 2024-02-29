#!/bin/bash

# Problem: For some reason in Linux, I can't have both "internal" and "external" mic's ON at the same time.
# There is a way to switch between them, but you have to go through lot of clicks... or just use this script.

declare -i sources_count=`pacmd list-sources | grep -c index:[[:space:]][[:digit:]]`
declare -i active_source_index=`pacmd list-sources | sed -n -e 's/\*[[:space:]]index:[[:space:]]\([[:digit:]]\)/\1/p'`
declare -i major_source_index=$sources_count-1
declare -i next_source_index=0

if [ $active_source_index -ne $major_source_index ] ; then
	next_source_index=active_source_index+1
fi

#change the default source
pacmd "set-default-source ${next_source_index}"

#display notification
declare -i ndx=0
pacmd list-sources | sed -n -e 's/device.description[[:space:]]=[[:space:]]"\(.*\)"/\1/p' | while read line;
do
	if [ $next_source_index -eq $ndx ] ; then
		notify-send -i notification-audio-volume-high "Sound output switched to" "$line"
		exit
	fi
	ndx+=1
done;