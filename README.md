# FastAPI Crypto Toolbox
Welcome to FastAPI Crypto Toolbox! This Python application provides a set of cryptographic tools accessible through a FastAPI web interface. You can use it for various tasks such as encryption, decryption, hash lookups, and more.

## Features
- **Cipher Tools**:
  - Caesar Cipher
  - Atbash Cipher
  - Rail Fence Cipher (To Be Added)
  - Rot13 Cipher (To Be Added)
  - Columnar Transposition Cipher (To Be Added)
- **Hash Lookup**: Lookup common password hashes such as md4, md5, smd160, sha1, sha256, sha512.
- **Encodings**: Encode text into binary format, and more on the way.

## Installation
To run this application, make sure you have Docker installed on your system. Then, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/your_username/repo_name.git
   ```

2. Navigate to the repository directory:
   ```bash
   cd repo_name
   ```

3. Build the Docker image:
   ```bash
   docker build -t fastapi-crypto-toolbox .
   ```

4. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 fastapi-crypto-toolbox
   ```

Now, you can access the application by visiting `http://localhost:8000` in your web browser.

## Usage
- **API Endpoints**:

  - `/`: Home endpoint to greet hackers and provide basic information about the tool.
  - `/usage`: Endpoint to get details about available features and endpoints.
  - `/ciphers`: Endpoint to access cipher tools.
  - `/lookup`: Endpoint for hash lookup.
  - `/encodings`: Endpoint to encode text.

For detailed usage instructions for each endpoint, visit the corresponding endpoint URLs.
