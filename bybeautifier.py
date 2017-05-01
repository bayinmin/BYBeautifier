from libs.kjson_parser import beautify_json
from libs.kfile_handlers import get_file_content
from libs.kfile_handlers import write_json_output_file

import sys, getopt, os

def main(argv):
   k_argv_type_long = "type="
   k_argv_type_short = "-t"

   k_argv_input_file_long = "ifile="
   k_argv_input_file_short = "-i"

   help_wording = ("kbeautifier.py -h for help\n"
                  "-t <conversion type> type of conversion eg. json \n"
                  "-i <input filename> input source file to be converted \n")

   inputfile = None
   type = 'json'

   # Command Line parameter configuration
   try:
      opts, args = getopt.getopt(argv,"h:t:i:",[k_argv_type_long,k_argv_input_file_long])
   except getopt.GetoptError:
      print help_wording
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         print help_wording
         sys.exit()
      elif opt in (k_argv_type_short, k_argv_type_long):
         type = arg
      elif opt in (k_argv_input_file_short, k_argv_input_file_long):
         inputfile = arg

   if inputfile is None:
       print "kbeautifier.py -t <type> -i <input filename>"
       sys.exit(2)

   # Processing File
   if type == "json" or None:
       print "starting conversion!"
       file_content = get_file_content(inputfile, os.getcwd())
       write_json_output_file(beautify_json(file_content),inputfile,os.getcwd())
       print "conversion done!"
   else:
       print "Unable to parse"

if __name__ == "__main__":
   main(sys.argv[1:])