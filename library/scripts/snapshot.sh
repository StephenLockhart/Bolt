#!/bin/sh
set -e
cd /workspace
mkdir -p .local-backups
tar czf ".local-backups/snap-$(date +%Y%m%d-%H%M%S).tar.gz" docs/ library/ 2>/dev/null || \
tar czf ".local-backups/snap-$(date +%Y%m%d-%H%M%S).tar.gz" docs/
ls -1t .local-backups/*.tar.gz 2>/dev/null | tail -n +21 | xargs -r rm -f
echo "snapshot: $(ls -1t .local-backups/*.tar.gz | head -1)"
