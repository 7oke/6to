import os 
import random 
import shutil

def create_random_file(base_folder, num_files=10):
        os.makedirs(base_folder,exist_ok=True)
        extensions= ['.txt','csv','jpg']

        for i in range (num_files):
                ext = random.choice(extensions)
                file_path = os.path.join(base_folder,f'file_{i}{ext}')
                with open(file_path, 'w') as f:
                         if ext == ".txt":
                                 f.write("Esto es un texto")
                         if ext == ".csv":
                                 f.write("col1, col2, col3\nv1, v2, v3")
                         if ext == ".jpg":
                                 f.write("\xFF\xD8\xFF")

if __name__ == "__main__":
        base_folder = "archivos"
        create_random_files(base_folder, num_files=15) 