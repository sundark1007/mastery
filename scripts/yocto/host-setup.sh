#!/usr/bin/env bash
# One-time Yocto build host setup on Ubuntu (needs sudo). Package list from the Yocto 6.0 quick build guide.
set -euo pipefail
sudo apt-get update
sudo apt-get install -y build-essential chrpath cpio debianutils diffstat file gawk gcc git \
    iputils-ping libacl1 libcrypt-dev locales python3 python3-git python3-jinja2 python3-pexpect \
    python3-pip python3-subunit python3-venv socat texinfo unzip wget xz-utils zstd
grep -q '^en_US.UTF-8 UTF-8' /etc/locale.gen || echo 'en_US.UTF-8 UTF-8' | sudo tee -a /etc/locale.gen >/dev/null
sudo locale-gen
echo "Host setup complete."
