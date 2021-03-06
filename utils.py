import os
if os.name == 'nt':
	import win32gui, win32api, win32con
import ctypes
import subprocess

def get_screen_resolution():
	if os.name == 'nt':
		user32 = ctypes.windll.user32
		user32.SetProcessDPIAware()
		resolution = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
	else:
		p = subprocess.Popen('xdpyinfo', stdout = subprocess.PIPE)
		p2 = subprocess.Popen(['awk', '/dimensions/{print $2}'], stdin = p.stdout, stdout = subprocess.PIPE)
		p.stdout.close()
		r, _ = p2.communicate()
		resolution = str(r.split()[0], encoding = 'utf-8')
		resolution = resolution.split('x')
	if int(resolution[0]) > 1920:
		resolution = (1920, 1080)
	return resolution