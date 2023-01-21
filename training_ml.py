import torch

from radar_network_models import Advenced_RadarCube
from radar_preprocessing_torch import range_velocity_map, range_angle_map, radar_cube
from network_functions import train_loop
from dataset import load_radar_data

import torch.nn as nn
import torch.optim as optim

model_folder = 'type0_split100_batchsize32_rng0_epoch40' #  Radar Cube solution

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
neural_nets = Advenced_RadarCube

net = neural_nets()
net.to(device)

dataset_dir = 'Scenario9/development_dataset' # Development dataset location
csv_file = 'scenario9_dev_train.csv' # Test CSV file


# Load Data
X_train, y_train = load_radar_data(dataset_dir, csv_file, radar_column='unit1_radar_1', label_column='beam_index_1')

preprocessing_functions = radar_cube

# Radar Preprocessing
preprocessing_function = preprocessing_functions
X_train = preprocessing_function(X_train)

# PyTorch Tensors
X_train = torch.from_numpy(X_train)
y_train = torch.from_numpy(y_train)


optimizer = optim.Adam(net.parameters())
criterion = nn.CrossEntropyLoss()

# Define your batch size and number of training epochs
batch_size = 128
num_epochs = 40

# Train the model
for epoch in range(num_epochs):
    loss, acc = train_loop(X_train, y_train, net, optimizer, criterion, device, batch_size=batch_size)
    print(f"Epoch {epoch + 1}/{num_epochs} - Loss: {loss:.4f}, Acc: {acc:.2f}%")