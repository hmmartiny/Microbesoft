
#  >>>>>>>>>>>>  BLOCK 1 IMPORT DATA  <<<<<<<<<<<<  #

### Libraries and initialitation of variables
#import mafft
import sys


### Capturing the input requisites
if len(sys.argv) == 1:
  filename1 = input("Enter the fasta file containing the sequences for the multiple alignment: ")
  #output_format = input("\nChoose between FASTA or ClustalW output: ")
elif len(sys.argv) == 2:	# Change to 3 if we take the output format
  filename1 = sys.argv[1]
  #output_format = sys.argv[2]
else:
  sys.stderr.write("Instruction: microbesoft.py <fastafilename> <outputFormat>\n")
  sys.exit(1)

### Several error checks
# if output_format.upper() != "FASTA" | "CLUSTALW" :
  # sys.stdout.write("\nError! Please type only <FASTA> or <ClustalW>")
  # sys.exit(1) 
try:
  infile1 = open(filename1, 'r')
  outfile = open('aligned_seq.fs', 'w')
except IOError as error:
  sys.stdout.write("\nCan't open file(s), reason: \n" + str(error) + "\n")
  sys.exit(1)
try:
  line1 = infile1.readline()
  if line1[0] != '>':
    raise IOError("The file is not fasta format.")
except IOError as error:
  sys.stderr.write("\nFormat error! " + str(error) + "\n")
  sys.exit(1)

  

