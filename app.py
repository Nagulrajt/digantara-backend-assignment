from flask import Flask, request, jsonify
from algorithms import binary_search, quick_sort, bfs
from logger import log_api_call, get_logs
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Flask DSA API! Use /binary-search, /quick-sort, or /bfs endpoints."})

@app.route('/binary-search', methods=['POST'])
def binary_search_api():
    data = request.get_json()
    array = data.get("array", [])
    target = data.get("target")
    
    if not isinstance(array, list) or not isinstance(target, (int, float)):
        return jsonify({"error": "Invalid input format. Expected a list and a target number."}), 400
    
    sorted_array = sorted(array)
    result = binary_search(sorted_array, target)
    log_api_call("Binary Search", data, result)
    return jsonify({"sorted_array": sorted_array, "result": result})

@app.route('/quick-sort', methods=['POST'])
def quick_sort_api():
    data = request.get_json()
    array = data.get("array", [])
    
    if not isinstance(array, list) or not all(isinstance(i, (int, float)) for i in array):
        return jsonify({"error": "Invalid input. Array must contain only numbers."}), 400
    
    result = quick_sort(array)
    log_api_call("Quick Sort", data, result)
    return jsonify({"sorted_array": result})

@app.route('/bfs', methods=['POST'])
def bfs_api():
    data = request.get_json()
    graph = data.get("graph", {})
    start_node = data.get("start_node")
    
    if not isinstance(graph, dict) or not isinstance(start_node, str):
        return jsonify({"error": "Invalid input. Graph must be a dictionary and start_node a string."}), 400
    
    result = bfs(graph, start_node)
    log_api_call("BFS", data, result)
    return jsonify({"bfs_traversal": result})

@app.route('/logs', methods=['GET'])
def get_logs_api():
    return jsonify(get_logs())

if __name__ == '__main__':
    app.run(debug=True)