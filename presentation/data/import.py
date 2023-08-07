import h5py
import os
import pandas as pd
import numpy as np

filename = 'data/sub-SA2p1a_1_SPARC_5Hz_LcVNS/derivatives/sub-SA2p1a_1_SPARC_5Hz_LcVNS_derived_data.mat'
with h5py.File(filename, 'r') as file:
    # Display the keys in the file to understand its structure
    for key in file.keys():
        print(key)
    print('--------')

    data = file['EMG_DuringStim'][:]

    params = file['AllParams'][:]

print(data)  
print("Type of elements:", data.dtype)
print("Number of dimensions:", data.ndim)
print("Shape of data:", data.shape)
print("Size (total number of elements):", data.size)
print('----------')

print(params)  
print("Type of elements:", params.dtype)
print("Number of dimensions:", params.ndim)
print("Shape of params:", params.shape)
print("Size (total number of elements):", params.size)
print('----------')


# List to store data that will be converted to the DataFrame
data = []

# Navigate through the data folder
data_folder = "data"
for subfolder in os.listdir(data_folder):
    subfolder_path = os.path.join(data_folder, subfolder)
    if os.path.isdir(subfolder_path):  # Ensure it's a folder
        derivatives_path = os.path.join(subfolder_path, "derivatives")
        # Assuming only one .mat file per derivatives folder
        for file in os.listdir(derivatives_path):
            if file.endswith(".mat"):
                file_path = os.path.join(derivatives_path, file)

                with h5py.File(file_path, 'r') as f:
                    # Extract the required data
                    emg_data = np.array(f["EMG_DuringStim"])
                    all_params = np.array(f["AllParams"])
                    
                    # Loop through the columns of emg_data and all_params
                    for col in range(emg_data.shape[1]):
                        avg_emg = emg_data[:, col].mean()
                        conditions = all_params[:, col]
                        # Append condition values and EMG average to the data list
                        row_data = list(conditions) + [avg_emg]
                        data.append(row_data)

# Convert the data list to a pandas DataFrame
columns = [f"Condition_{i+1}" for i in range(6)] + ["EMG_Average"]
df = pd.DataFrame(data, columns=columns)

# write df to a csv
df.to_csv('data.csv', index=False)



print(df)