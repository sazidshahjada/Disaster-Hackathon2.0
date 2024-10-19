import os

# Directory containing the files
directory = '/home/sajid/Work/DISASTER-HACKATHON-2.0/Frames'

# Iterate over all the files in the directory
for i, filename in enumerate(os.listdir(directory)):
    # Construct full file path
    old_file = os.path.join(directory, filename)
    
    # Make sure it's a file (not a directory)
    if os.path.isfile(old_file):
        # Generate new file name (for example, adding a prefix or renaming completely)
        new_filename = f"frame_{i}"
        new_file = os.path.join(directory, new_filename)

        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed: {old_file} -> {new_file}')
