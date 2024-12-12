import os
import shutil
import random

def split_images(src_dir, split_percentage=0.8):
    # Extract the parent directory of src_dir
    parent_dir = os.path.dirname(src_dir)  # Get the directory one level above src_dir
    
    # Set the copy structure directory to be at the same level as the original one
    copy_structure_dir = os.path.join(parent_dir, 'TestSet_OnlyVal')
    os.makedirs(copy_structure_dir, exist_ok=True)

    # Iterate over all subdirectories in the source directory
    for subdir in os.listdir(src_dir):
        subdir_path = os.path.join(src_dir, subdir)
        
        if os.path.isdir(subdir_path):
            # Get all image files in the subdirectory
            images = [f for f in os.listdir(subdir_path) if os.path.isfile(os.path.join(subdir_path, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            
            # Shuffle the images to ensure random distribution
            random.shuffle(images)
            
            # Calculate the split index
            split_index = int(len(images) * split_percentage)
            
            # Split images into two groups
            train = images[:split_index]
            val = images[split_index:]
            
            # Create two new directories in the subdirectory to store the split images
            train_dir = os.path.join(subdir_path, 'train')
            val_dir = os.path.join(subdir_path, 'val')
            
            os.makedirs(train_dir, exist_ok=True)
            os.makedirs(val_dir, exist_ok=True)
            
            # Create '0_real' and '1_fake' directories within 'train' and 'val'
            real_train_dir = os.path.join(train_dir, '0_real')
            fake_train_dir = os.path.join(train_dir, '1_fake')
            real_val_dir = os.path.join(val_dir, '0_real')
            fake_val_dir = os.path.join(val_dir, '1_fake')
            
            os.makedirs(real_train_dir, exist_ok=True)
            os.makedirs(fake_train_dir, exist_ok=True)
            os.makedirs(real_val_dir, exist_ok=True)
            os.makedirs(fake_val_dir, exist_ok=True)
            
            # Move all images to '1_fake' directory (train and val images)
            for image in train:
                shutil.move(os.path.join(subdir_path, image), os.path.join(fake_train_dir, image))
                
            for image in val:
                shutil.move(os.path.join(subdir_path, image), os.path.join(fake_val_dir, image))
            
            print(f"Processed '{subdir}', {len(train)} images in train, {len(val)} images in val.")
            
            # Now create a copy of the entire dataset with images only in 'val/1_fake'
            # Copy the entire directory structure and images to 'TestSet_OnlyVal'
            for root, dirs, files in os.walk(subdir_path):
                # Get the relative path from the source directory
                rel_path = os.path.relpath(root, src_dir)
                copy_root = os.path.join(copy_structure_dir, rel_path)
                
                # Create the corresponding directory in the copied structure
                os.makedirs(copy_root, exist_ok=True)

                # Copy files from the original directory structure to the copied structure
                for file in files:
                    src_file = os.path.join(root, file)
                    dst_file = os.path.join(copy_root, file)
                    shutil.copy(src_file, dst_file)
            
            # Now copy the images into the 'val/1_fake' in the copied structure
            for image in train:
                # Copy images from 'train' to 'val/1_fake' in the copied structure
                subdir_fake_copy = os.path.join(copy_structure_dir, 'val', '1_fake', subdir)
                os.makedirs(subdir_fake_copy, exist_ok=True)
                shutil.copy(os.path.join(subdir_path, 'train', '1_fake', image), os.path.join(subdir_fake_copy, image))
                
            for image in val:
                # Copy images from 'val' to 'val/1_fake' in the copied structure
                subdir_fake_copy = os.path.join(copy_structure_dir, 'val', '1_fake', subdir)
                os.makedirs(subdir_fake_copy, exist_ok=True)
                shutil.copy(os.path.join(subdir_path, 'val', '1_fake', image), os.path.join(subdir_fake_copy, image))

            print(f"Created a copy of the entire dataset in '{copy_structure_dir}' with all images in 'val/1_fake'.")

src_dir = '/home/disi/DiffDataset/TestSet'
split_percentage = 0.8  # 80% in train, 20% in val
split_images(src_dir, split_percentage)
