#!/usr/bin/ruby
# WANT_JSON

require 'rubygems'
require 'json'

File.open(ARGV[0]) do |fh|

   data = JSON.parse(fh.read())

   begin
      name = data['name'].to_s()
   rescue
      # to raise an error, return failed=True and a msg string.

      print JSON.dump({
          'failed' => true,
          'msg'    => 'failed to parse input'
      })

      # the error code here is not so important, the JSON is!

      exit(1)
   end

   result = {
      'msg' => "Hello #{name}",
      'changed' => False
   }

   print JSON.dump(result)

end
