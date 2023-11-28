#!/usr/bin/env ruby
# This script outputs sender, receiver,flags

puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")
