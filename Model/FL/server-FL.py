import flwr as fl
from typing import List, Tuple, Optional, Dict
import numpy as np

# Define strategy
strategy = fl.server.strategy.FedAvg(
    fraction_fit=1.0,  # Sample 100% of available clients for training
    fraction_evaluate=1.0,  # Sample 100% of available clients for evaluation
    min_fit_clients=2,  # Never sample less than 2 clients for training
    min_evaluate_clients=2,  # Never sample less than 2 clients for evaluation
    min_available_clients=2,  # Wait until at least 2 clients are available
)

# Start server
if __name__ == "__main__":
    fl.server.start_server(
        server_address="0.0.0.0:8080",
        config=fl.server.ServerConfig(num_rounds=3),
        strategy=strategy,
    )