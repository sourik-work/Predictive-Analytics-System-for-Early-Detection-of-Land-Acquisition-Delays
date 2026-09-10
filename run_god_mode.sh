#!/bin/bash
echo "Forwarding to scripts/run_god_mode.sh..."
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
exec "$SCRIPT_DIR/scripts/run_god_mode.sh" "$@"
