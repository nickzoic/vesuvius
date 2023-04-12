import glob
import os
import mmap

from PIL import Image

of = open("scroll.dat", "wb")

for number, filename in enumerate(sorted(glob.glob('tifs/*.tif'))):
    print(f"{number}: {filename}")
    im = Image.open(filename)
    assert im.height == 7888
    assert im.width == 8096
    assert im.mode == "I;16"
    assert im.getpixel((0,0)) == 0x60a9

    # At least on my machine, this is writing 16 bit little endian.
    # I'm not sure if this is specified anywhere.
    buf = im.tobytes()
    assert buf[0] == 0xa9
    assert buf[1] == 0x60
    of.write(buf)

of.flush()
