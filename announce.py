import os
import os.path
import socket

unix = '/path/to/socketbot/channels'
channels = ['#socketbot']

prefix = 'http://or/maybe/ftp/prefix'


def announce(final, airdate):
	filename = os.path.basename(final)
	message = "New series: ({0}) {1} ".format(airdate, os.path.join(prefix, filename))
	for channel in channels:
		s = socket.socket(socket.AF_UNIX)
		s.connect(os.path.join(unix, channel))
		s.send(message)

