#!/usr/bin/env bash
# Run a BitBake build with a Linux-only PATH, logging to the build directory. Usage: build.sh [target]
set -euo pipefail
target=${1:-core-image-minimal}
setup=${YOCTO_SETUP:-$HOME/yocto/bitbake-builds/poky-wrynose}
threads=${YOCTO_THREADS:-8}
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

conf="$setup/build/conf/local.conf"
if ! grep -q '^# mastery tuning' "$conf"; then
    printf '\n# mastery tuning: parallelism sized for the available RAM\nBB_NUMBER_THREADS = "%s"\nPARALLEL_MAKE = "-j %s"\n' "$threads" "$threads" >> "$conf"
fi

log="$setup/build/logs/$(date +%Y%m%d-%H%M%S)-$target.log"
mkdir -p "$(dirname "$log")"
cd "$setup/build"
source ./init-build-env >/dev/null
echo "Building $target, log: $log"
bitbake "$target" 2>&1 | tee "$log" | grep -E '^(NOTE: Tasks Summary|ERROR|Summary)' || true
tail -3 "$log"
