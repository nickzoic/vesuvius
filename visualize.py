import numpy as np
import os
import random

nx = 8096
ny = 7888

fs = os.stat('scroll.dat').st_size
assert fs % (nx*ny*2) == 0
nz = fs//(nx*ny*2)

# "uint16" is little-endian, at least on my machine ...
fp = np.memmap('scroll.dat', dtype='uint16', mode='r', shape=(nx,ny,nz))

# just quickly check that endianness
assert fp[0][0][0] == 0x60a9

pp = []
cc = []


SIZE = 100

# pick an arbitrary point for the center
cx = random.randint(0, nx-SIZE-1)
cy = random.randint(0, ny-SIZE-1)
cz = random.randint(0, nz-SIZE-1) if nz > SIZE else 0

POINTS = 1000000

pp = np.zeros((POINTS,3), dtype='float')
cc = np.zeros((POINTS,3), dtype='float')
for n in range(0,POINTS):
    v = 0
    while v < 32768:
        xx = cx + random.random() * (SIZE-1)
        yy = cy + random.random() * (SIZE-1)
        zz = cz + random.random() * (min(SIZE,nz)-1)
        v = fp[int(xx)][int(yy)][int(zz)]
        #v = interp([xx,yy,zz])[0]

    pp[n] = [xx,yy,zz]
    vv = (v-32768)/32768
    cc[n] = [vv,1-vv,0]

import open3d as o3d

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(pp)
pcd.colors = o3d.utility.Vector3dVector(cc)
o3d.visualization.draw_geometries([pcd])
