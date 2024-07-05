from flask import Flask, render_template, request

app = Flask(__name__)

# Fungsi untuk mengenkripsi teks
def encrypt_text(text):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

# Fungsi untuk mendekripsi teks
def decrypt_text(text):
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
            elif char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.form['text']
    encrypted_text = encrypt_text(text)
    return render_template('result.html', text=text, processed_text=encrypted_text, action='Encrypt')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    text = request.form['text']
    decrypted_text = decrypt_text(text)
    return render_template('result.html', text=text, processed_text=decrypted_text, action='Decrypt')

if __name__ == '__main__':
    app.run(debug=True)
