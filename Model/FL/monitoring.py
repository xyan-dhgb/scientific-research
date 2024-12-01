import flwr as fl
from typing import List, Tuple, Optional, Dict
import numpy as np
from flask import Flask, jsonify
import threading
import queue

app = Flask(__name__)
metrics_queue = queue.Queue()
current_round = 0
latest_metrics = {}

# Flask routes
@app.route('/')
def home():
    return '''
    <h1>Federated Learning Monitor</h1>
    <p>Current round: {}</p>
    <p>Latest metrics: {}</p>
    <script>
        setTimeout(function(){{
            window.location.reload();
        }}, 5000);
    </script>
    '''.format(current_round, latest_metrics)

@app.route('/metrics')
def get_metrics():
    return jsonify({
        'current_round': current_round,
        'metrics': latest_metrics
    })

class MonitoringStrategy(fl.server.strategy.FedAvg):
    def aggregate_evaluate(self, server_round, results, failures):
        """Aggregate evaluation losses using weighted average."""
        if not results:
            return None

        global current_round, latest_metrics
        current_round = server_round

        # Weigh accuracy of each client by number of examples used
        accuracies = [r.metrics["accuracy"] * r.num_examples for r in results]
        examples = [r.num_examples for r in results]

        # Aggregate and print metrics
        accuracy_aggregated = sum(accuracies) / sum(examples)
        latest_metrics = {
            'accuracy': accuracy_aggregated,
            'num_clients': len(results)
        }
        print(f"Round {server_round} accuracy aggregated from client results: {accuracy_aggregated}")
        
        return accuracy_aggregated

def start_flask():
    app.run(host='0.0.0.0', port=8081)

# Start Flask server in a separate thread
flask_thread = threading.Thread(target=start_flask)
flask_thread.daemon = True
flask_thread.start()

# Define strategy
strategy = MonitoringStrategy(
    fraction_fit=1.0,
    fraction_evaluate=1.0,
    min_fit_clients=2,
    min_evaluate_clients=2,
    min_available_clients=2,
)

if __name__ == "__main__":
    print("Access monitoring interface at http://localhost:8081")
    fl.server.start_server(
        server_address="0.0.0.0:9090",
        config=fl.server.ServerConfig(num_rounds=3),
        strategy=strategy,
    )