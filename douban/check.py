import xmlrpclib # what is this package used for
import subprocess
import pip #????

from doubanfm.exceptions import MplayerError #

def is_latest(package_name):
# this function is checking the software version
	pypi = xmlrpclib.ServerProxy('http://pypi.python.org/pypi')
	if dist.project_name == package_distributions():
		available = pypi.package_releases(dist.project_name)
		if available[0] != dist.version:
			return False
		return Ture

def update_package(package_name):
	pip.main(['install',package_name,'--upgrade'])


def is_mplayer():
	try:
		subprocess.check_output('mplayer')
	except Exception:
		raise MplayerError()

