from fastapi import FastAPI
import CTCiphers as ciph # CTEncoding CTShells
import CTEncoding as enc
import CTLookup as look
import uvicorn
from starlette.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def greet_hackers():
	return "Hello Hackers, Thank you all for trying out this tool, This is something I made just to learn how FastAPI works but I think this can be a Useful tool. Especially when used with the commandline. You can visit the endpoint '/usage' for details of the features."

@app.get("/usage")
def usage():
	return "/ciphers, /lookup, /revshell, /encodings , More to be added. Open to Suggestions!"

@app.get("/ciphers")
def ciphers_usage():
	return "/ciphers/{type}/{string-to-encrypt}, 00 -> Caesar, 01 -> Atbash, 02 -> Rail Fence, 03 -> Rot13, 04 -> Columnar Transposition"

@app.get("/ciphers/{type}/{string}")
def ciphers(type, string):
#	return f"{type}:{string}"
	if (type == '00'):
		return HTMLResponse(content=ciph.caesar_cipher(string), status_code=200)
	if (type == '01'):
		return ciph.atbash_cipher(string)

@app.get("/lookup")
def lookup():
	return "endpoint -> /lookup/{hash}Here you can do hash lookup for the most common 100k Passwords, the available hash types are md4, md5, smd160, sha1, sha256, sha512."

@app.get("/lookup/{hash}")
def hash_lookup(hash):
	result = look.reverse_lookup(hash)
	if result:
		return result
	else:
		return {"error": "String not found for the given hash value."}

@app.get("/encodings")
def encodings_usage():
	return "/encodings/{type}/{string-to-encode}, 00 -> binary, 01 -> bash64, That's all for now, More to be added later."

@app.get("/encodings/{type}/{string}")
def encodings(type, string):
	if (type == '00'):
		return enc.tobinary(string)
	elif (type == '01'):
		return enc.tobase64(string)

if __name__ == '__main__':
	uvicorn.run("app:app", reload=True)
