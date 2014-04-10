#!/bin/sh -ex
# -ex:
# bail on errors and show debugging stuff
read -r -d '' HELP <<-'EOF'
HELP TEXT HERE

EOF

################################################################################
### TEMPFILES
# From:
#   http://stackoverflow.com/questions/430078/shell-script-templates
# create a default tmp file name
tmp=${TMPDIR:-/tmp}/prog.$$
# delete any existing temp files
trap "rm -f $tmp.?; exit 1" 0 1 2 3 13 15
# then do
#   ...real work that creates temp files $tmp.1, $tmp.2, ...

################################################################################
#### USAGE AND ERRORS
COMMAND=`basename $0`
# Load basic functions; primarily messaging functions
# Rename file name here to match actual functions
source "`dirname $0`/template-functions"

# Note that LOGFILE is used by functions for log commands: log_message,
# log_warning, log_error, etc.
#
# replace log file with another value if you want
LOGFILE=LOG_${COMMAND}_`tstamp`.log

usage() {
   echo "Usage: $cmd [ARGS..]"
}

print_help() {
  echo "$HELP"
}

################################################################################
### OPTIONS
while getopts "h" opt; do
  case $opt in
    h)
      usage
      print_help
      exit 1
      ;;
    \?)
      echo "ERROR Invalid option: -$OPTARG" >&2
      echo ""
      usage
      exit 1
      ;;
  esac
done

shift $((OPTIND-1))


################################################################################
### THESCRIPT





################################################################################
### EXIT
# http://stackoverflow.com/questions/430078/shell-script-templates
rm -f $tmp.?
trap 0
exit 0
