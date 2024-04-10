from fastapi import FastAPI
import CTCiphers as ciph # CTEncoding CTShells
import CTEncoding
import uvicorn

app = FastAPI()

@app.get("/")
def greet_hackers():
	return "Hello Hackers, Thank you all for trying out this tool, This is something I made just to learn how FastAPI works but I think this can be a Useful tool. Especially when used with the commandline. You can visit the endpoint '/usage' for details of the features."

@app.get("/usage")
def usage():
	return "/ciphers, /revshell, /encodings , More to be added. Open to Suggestions!"

@app.get("/ciphers")
def ciphers_usage():
	return "/ciphers/{type}/{string-to-encrypt}, 00 -> Caesar, 01 -> Atbash, 02 -> Rail Fence, 03 -> Rot13, 04 -> Columnar Transposition"

@app.get("/ciphers/{type}/{string}")
def ciphers(type, string):
#	return f"{type}:{string}"
	if (type == '00'):
		all_shifted_ciphers = ciph.caesar_cipher(string)
		return all_shifted_ciphers
	if (type == '01'):
		return ciph.atbash_cipher(string)

@app.get("/encodings")
def encodings_usage():
	return "/encodings/{type}/{string-to-encode}, 00 -> binary, 01 -> bash64, That's all for now, More to be added later."

@app.get("/encodings/{type}/{string}")
def encodings(type, string):
	if (type == '00'):
		return CTEncoding.tobinary(string)
	elif (type == '01'):
		return 'Base64 Logic Here'

if __name__ == '__main__':
	uvicorn.run("app:app", reload=True)
