#!/usr/bin/python3

import sys
import os
import platform
import subprocess

basedir = os.path.abspath(os.path.dirname(__file__))

synthbin=os.path.join(basedir,'SynthesizerV','synthv-studio')
synthlib=os.path.join(basedir,'lib-ext')

def encodePath(path):
    r=path
    r=r.replace(" ","\\ ")
    return r

if platform.machine()=='aarch64':
    os.system("LD_LIBRARY_PATH=\"%s\" exagear -- \"%s\"" % (synthlib,encodePath(synthbin)))
else:
    os.system("LD_LIBRARY_PATH=\"%s\" \"%s\"" % (synthlib,synthbin))
