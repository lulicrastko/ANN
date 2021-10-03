from src.utils.common import read_config
from src.utils.data_mgmt import get_data
import argparse

def training(config_path):
    config = read-config(config_path)
    validation_datasize = config['params']['validation_datasize']
    (X_train, y_train), (X_valid, y_valid), (X_test,y_test) = get_data(validation_datasize)

if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument('--config','-c',default='config.yaml')

    parsed_args = args.prase_args()

    training(config_path=parsed_args.config)