# Vesuvius Challenge Code

This is just some code messing around with https://scrollprize.org/

## tif2dat.py

Dealing with a whole bunch of .TIF files is inconvenient as the program would
have to load them every time it starts up.  This little utility unpacks a bunch
of TIF files (in `tifs/*.tif`) into a single uncompressed raw data file called
`scroll.dat`.  If you have a lot of slices this is going to be a very big file.

`scroll.dat` can then be make available as a Python numpy array with code like:

    nx = 8096
    ny = 7888
    nz = os.stat('scroll.dat').st_size // (nx * ny * 2)

    scroll = np.memmap('scroll.dat', dtype='uint16', mode='r', shape=(nx,ny,nz))

Note that the fixed 8096 x 7888 x 16 bit scan size is a baked-in assumption here.

The data isn't actually loaded at this time, just mapped into memory using mmap
so it's up to your OS to page it in, cache it, etc.

## visualize.py

This uses the `scroll.dat` file above to display a random little piece of the 
scroll using the open3d point cloud visualizer, which gives you some idea of 
how challenging it is going to be to extract anything much out of this data.


