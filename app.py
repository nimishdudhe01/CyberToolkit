from fastapi import FastAPI
import CTCiphers # CTEncoding CTShells
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
def ciphers_00(type, string):
#	return f"{type}:{string}"
	if (type == '00'):
		all_shifted_ciphers = CTCiphers.caesar_cipher(string)
		return all_shifted_ciphers
	if (type == '01'):
		return "AtBash Logic Here"

if __name__ == '__main__':
	uvicorn.run("app:app", reload=True)