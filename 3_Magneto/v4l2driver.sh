sudo modprobe bcm2835-v4l2
v4l2-ctl --overlay=1 
v4l2-ctl --overlay=0
v4l2-ctl --set-fmt-video=width=1920,height=1088,pixelformat=4
v4l2-ctl --stream-mmap=3 --stream-count=100 --stream-to=somefile.264
v4l2-ctl --set-fmt-video=width=2592,height=1944,pixelformat=3
v4l2-ctl --stream-mmap=3 --stream-count=1 --stream-to=somefile.jpg
v4l2-ctl --set-ctrl video_bitrate=10000000
v4l2-ctl --list-formats
