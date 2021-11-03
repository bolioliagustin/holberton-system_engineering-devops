#!/usr/bin/env ruby
#The regular expression must match School

puts ARGV[0].scan(/(?<=from:|to:|flags:).*?(?=\])/).join(",")
