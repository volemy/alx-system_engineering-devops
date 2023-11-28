#!/usr/bin/env ruby
# This script has regular expression that matches only capital letters

puts ARGV[0].scan(/[A-Z]/).join
