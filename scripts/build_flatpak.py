#!/usr/bin/env python3

import sys
import subprocess
from os import path
from tempfile import TemporaryDirectory

manifest = sys.argv[1]
output = sys.argv[2]
app_id = path.basename(manifest).rpartition('.')[0]

with TemporaryDirectory(prefix='gwe-flatpak-repo') as temprepo:
    with TemporaryDirectory(prefix='gwe-flatpak-build') as tempbuild:
        subprocess.call(['flatpak-builder', ' --install-deps-from=flathub', tempbuild, manifest, '--repo=' + temprepo])
    subprocess.call(['flatpak', 'build-bundle', temprepo, output, app_id])
