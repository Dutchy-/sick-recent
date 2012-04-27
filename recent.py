#!/usr/bin/python
import sys
import datetime
import os
import os.path

# Announce
ANNOUNCE = True
# location of the recent series directory
RECENT = '/home/dutchy/shares/mirrorpush'
# days
AIRED_WITHIN = 7
# delete link after
DELETE_AFTER = 14

def sickbeard_run():
	# It passes 6 parameters to these scripts:
	# 1 final full path to the episode file
	# 2 original name of the episode file
	# 3 show tvdb id
	# 4 season number
	# 5 episode number
	# 6 episode air date
	# example call:
	# ['/home/sickbeard/sicksubs/sicksubs.py',
	# u'/media/media/Series/Qi/Season 09/QI.S09E12.Illumination.avi',
	# u'/media/bin2/usenet_downloads/tv/QI.S09E12.HDTV.XviD-FTP/qi.s09e12.hdtv.xvid-ftp.avi',
	# '72716', '9', '12', '2011-11-25']
	
	# We need these
	final = sys.argv[1]
	airdate = sys.argv[6]

	link(final, airdate)
	unlink()

	return

def unlink():
	# We need to do something about old links
	for file in os.listdir(RECENT):
		filepath = os.path.join(RECENT, file)
		if not check_date(get_ctime(filepath), DELETE_AFTER):
			print("Removing old link: {0}".format(file))
			os.remove(filepath)
	return

def link(final, airdate):
	print("Checking episode {0}".format(final))
	if check_date(get_date(airdate)):
		if ANNOUNCE: announce(final, airdate)
			
		print("Air date {0} within {1} days, linking".format(airdate, AIRED_WITHIN))
		linkname = os.path.join(RECENT, os.path.basename(final))
		if not os.path.exists(linkname):
			os.link(final, linkname)
		else:
			# perhaps insert .proper. in the filename?
			if get_ctime(linkname) < get_ctime(final):
				# The file is newer
				print("We downloaded a newer file of the same episode, updating")
				os.remove(linkname)
				os.link(final,linkname)
	else:
		print("Air date {0} not within {1} days, not linking".format(airdate, AIRED_WITHIN))
		# What do we do with older episodes?
	return

def announce(final, airdate):
	from announce import announce
	announce(final, airdate)

def get_ctime(file):
	return datetime.datetime.fromtimestamp(os.path.getctime(file))

def get_date(airdate):
	return datetime.datetime.strptime(airdate, '%Y-%m-%d')

def check_date(dt, d=AIRED_WITHIN):
	delta =  datetime.datetime.now() - dt
	return delta.days < d

if __name__ == '__main__':
	if len(sys.argv) == 7:
		sickbeard_run()
