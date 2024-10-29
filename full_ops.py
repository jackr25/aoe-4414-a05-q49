# full_ops.py
#
# Usage: python3 full_ops.py c_in n_wv
#  script to determine the output shape and operation count of a convolution layer
# Parameters:
# c_in: input channel count
# n_wv: number of weight vectors

# Output:
# c_out: output channel count
# h_out: output height count
# w_out: output width count
# adds: number of additions performed
# muls: number of multiplications performed
# divs: number of divisions performed

# Written by Jack Rathert
# Other contributors: None

## imports---------------------------------------------------------------------------
import sys
## Functions--------------------------------------------------------------------------
def fullops(c_in:int,n_wv:int):
  c_out = n_wv
  h_out = 1
  w_out = 1
  adds = n_wv*c_in
  muls = n_wv*c_in
  divs = 0
  return c_out,h_out,w_out,adds,muls,divs
  

# Arguments---------------------------------------------------------------------------
# parsing
if len(sys.argv)==3:
      c_in = int(sys.argv[1])
      n_wv = int(sys.argv[2])
else:
  print(\
   'Usage: '\
   'python3 full_ops.py c_in n_wv'\
  )
  exit()

## Function Calls ----------------------------------------------------------------------
c_out, h_out, w_out, adds, muls, divs = fullops(c_in,n_wv)


print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed