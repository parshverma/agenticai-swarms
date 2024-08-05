from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
test_cases = [
    {"id": 1, "title": "Login functionality", "description": "Test login with valid credentials", "status": "pass"},
    {"id": 2, "title": "Signup functionality", "description": "Test signup with new user details", "status": "fail"},
    {"id": 3, "title": "Password reset", "description": "Test password reset functionality", "status": "pending"},
    {"id": 4, "title": "Profile update", "description": "Test profile update with valid data", "status": "pass"}
]

# Endpoint to get all test cases
@app.route('/test_cases', methods=['GET'])
def get_test_cases():
    return jsonify(test_cases)

# Endpoint to get a test case by ID
@app.route('/test_cases/<int:test_case_id>', methods=['GET'])
def get_test_case(test_case_id):
    test_case = next((tc for tc in test_cases if tc["id"] == test_case_id), None)
    if test_case:
        return jsonify(test_case)
    else:
        return jsonify({"error": "Test case not found"}), 404

# Endpoint to search for test cases by title
@app.route('/test_cases/search', methods=['GET'])
def search_test_cases():
    query = request.args.get('query', '')
    results = [tc for tc in test_cases if query.lower() in tc["title"].lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
