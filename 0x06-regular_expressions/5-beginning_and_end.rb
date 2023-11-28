#!/usr/bin/env ruby
# This ruby cript accepts one argument and passes it to a  regular expresion

puts ARGV[0].scan(/^h.n$/).join
