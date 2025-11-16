from flask import Flask, jsonify, send_from_directory
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
import secrets

# Random 16 Bytes key
KEY = secrets.token_bytes(16) 

current_dir = os.path.dirname(os.path.abspath(__file__))
with open(current_dir+'/flag.txt', 'r') as f: FLAG = f.read().strip()

app = Flask(__name__)

@app.route('/')
def serve_source():
    return send_from_directory(current_dir, 'app.py')


@app.route('/encrypt/<plaintext>/')
def encrypt(plaintext):
    try:
        plaintext_bytes = bytes.fromhex(plaintext)
    except ValueError:
        return jsonify({"error": "Invalid hex string for plaintext"}), 400

    data_to_pad = plaintext_bytes + FLAG.encode()
    
    padded = pad(data_to_pad, 16)
    
    # 3. Ініціалізація AES у режимі ECB
    cipher = AES.new(KEY, AES.MODE_ECB)
    
    try:
        encrypted = cipher.encrypt(padded)
    except ValueError as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"ciphertext": encrypted.hex()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
