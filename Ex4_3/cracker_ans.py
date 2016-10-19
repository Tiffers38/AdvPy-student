def main(file):
zfile = zipfile.ZipFile(file, 'r')# creates zipfile-->zfile object
start = time.time()
print('Starting crack at {}'.format(time.strftime(%j: %H:%M:%S', time.localtime(start)))
print('.', end='')
for i, p in enumerate(gen_pass(maxval=4)): #enumerate--> everytime you loop it will give a +1
    if not i % 1000: print('.', end='')
    if not i % 100000: print('\n{}'.format(i / 1



def gen_pass(minval=3, maxval=4):
    letters = string.ascii.lowercase
# yield returns things one at a time, iteratively.  
