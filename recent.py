#!/usr/bin/python
import sys
import datetime
import os
import os.path

# location of the recent series directory
RECENT = '/home/dutchy/shares/mirrorpush'
# days
AIRED_WITHIN = '7'
# delete link after
DELETE_AFTER = '14'

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
	return

def link(final, airdate):
	print("Checking episode {0}".format(final))
	if check_date(airdate):
		print("Air date {0} within {1} days, linking".format(airdate, AIRED_WITHIN))
		linkname = os.path.join(RECENT, os.path.basename(final))
		if not os.path.exists(linkname):
			os.link(final, linkname)
		else:
			# TODO: check for propers?
			pass
	else:
		print("Air date {0} not within {1} days, not linking".format(airdate, AIRED_WITHIN))
		# What do we do with older series?
		

	return

def check_date(airdate):
	delta =  datetime.datetime.now() - datetime.datetime.strptime(airdate, '%Y-%m-%d')
	return delta.days < AIRED_WITHIN

if __name__ == '__main__':
	if len(sys.argv) == 7:
		sickbeard_run()
