# Average-Nucleotide-Identity
Another common task in bioinformatics – running the same task for different inputs. The use case here will be computing average nucleotide identity (ANI) for each pair 
(all-against-all  pairs)  of  input  fasta  file.    The  fasta  files  are  microbial  genome sequences.  The ANI is being calculated using MUMmer’s dnadiff.  Install the MUMmer 
package from here: https://mummer4.github.io/.  Assume that dnadiff is in our environment PATH.
Given a set of files, say A.fasta, B.fasta and C.fasta, this script will calculate the pairwise distance between them and print them in a matrix format.
The  threads  argument  is  key.    The  threads  specify  how  many  parallel  instances  of pairwise ANI calculations should be performed.  So, if the user says -t 3, launch 3 ANI computations  (obviously  for  different  pairs)  simultaneously and the program  should finish ~3 times faster for -t 3 when compared to a single thread (-t 1).
