#!/usr/bin/env ruby

################################################################################
# Name: name.rb
#
# Usage: #{execuable_name} [FOLDER]
#
# Do something.
#
# [ARG]   Optional argument. 
#
# OPTIONS
#
#     -f, --format FORMAT              Choose ouput format: pretty [default], 
#                                      tabular, delimited
#
#-------------------------------------------------------------------------------

require 'optparse'

this_dir = File.dirname(__FILE__)

######################################################################
# CONSTANTS
######################################################################


######################################################################
# METHODS
######################################################################


######################################################################
# run the script
######################################################################


# get the options
options = {}
option_parser = OptionParser.new do |opts|
  execuable_name = CMD
  opts.banner = "
Usage: #{execuable_name} [FOLDER]

   Verify the contents of DNGs and derived files.
        
   [FOLDER]   Optional folder argument should either be the folder name
              (`0012_000052`, `\"My document 21v\"`) or, for numerically named
              folders like `0012_000052`, a short hand like `12.52`. Otherwise,
              the latest DNG folder will be used.
  "

  # opts.on('-x', '--exif', 'Run exiftool on all DNG images') do
  #   options[:exif] = true
  # end

  # opts.on('-v', '--verbose', "Be very talkative") do
  #   options[:verbose] = true
  # end

  # opts.on('-c FILE', '--config FILE', 
  #         "Use alternate config file \n    [DEFAULT #{DEFAULT_CONFIG_FILE}]") do |file|
  #   options[:config] = file
  # end  
end
option_parser.parse!


# do stuff
