import os
import re
import json
import subprocess
from urllib import request


def get_resolution():
    cmd = ['xrandr']
    cmd2 = ['grep', '*']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)
    p.stdout.close()

    resolution_string, junk = p2.communicate()
    resolution = resolution_string.split()[0]
    return resolution.decode('utf-8')


url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
resolution = get_resolution()

with request.urlopen(url) as res:
    data = res.read()

bing_json = json.loads(data.decode('utf-8'))
wallpaper_urlbase = bing_json['images'][0]['urlbase']

wallpaper_name = re.search('\w+$', wallpaper_urlbase).group()

wallpaper_url = 'http://www.bing.com{}_{}.jpg'.format(
    wallpaper_urlbase, resolution)


request.urlretrieve(wallpaper_url, '{}_{}.jpg'.format(
    wallpaper_name, resolution))
