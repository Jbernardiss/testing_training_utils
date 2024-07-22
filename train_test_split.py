
import shutil, glob, os, sys, math, random
from distutils.dir_util import copy_tree

full_db_path = None
tests_percentage = None
ouput_path = None

for i, arg in enumerate(sys.argv):
  if arg == '-p':
    full_db_path = sys.argv[i + 1]

  if arg == '-t':
    tests_percentage = int(sys.argv[i + 1])/100

  if arg == '-o':
    output_path = sys.argv[i + 1]
    if output_path[0] != '/':
      output_path = os.getcwd() + '/' + output_path

if full_db_path == None or tests_percentage == None or output_path == None:
  print("Usage: python3 train_test_split.py -p <full_db_path> -t <tests_percentage> -o <output_path>")
  sys.exit(1)
  

source_files = glob.glob(full_db_path + "/*/*")
target_files = []


for i in range(round(tests_percentage * len(source_files))):
  target_files.append(source_files.pop(random.randint(0, len(source_files) - 1)))


os.mkdir(output_path)
os.mkdir(output_path + "/src")
os.mkdir(output_path + "/target")


for file in source_files:

  if not os.path.exists(output_path + "/src/" + file.split('/')[-2]):
    os.mkdir(output_path + "/src/" + file.split('/')[-2])

  shutil.copy(file, output_path + "/src/" + file.split('/')[-2])

for file in target_files:
  shutil.copy(file, output_path + "/target")
