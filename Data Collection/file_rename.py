import os
import glob

directory = '/home/sajid/Work/DISASTER-HACKATHON-2.0/output_frames'
files = glob.glob(os.path.join(directory, '*.jpg'))

for file in files:
    file_name, file_extension = os.path.splitext(os.path.basename(file))
    new_file_name = f"new_{file_name}{file_extension}"
    new_file_path = os.path.join(directory, new_file_name)
    os.rename(file, new_file_path)
    print(f"Renamed: {file} -> {new_file_path}")
