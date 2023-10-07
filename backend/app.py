from flask import Flask, request, jsonify
import maritalk
import requests

app = Flask(__name__)

API_KEY = '100967333014773694334$301a2d09eb5a949372342c6ce125335b346740cecd46dbe12fc2fa326cf315f3'

URL = "https://chat.maritaca.ai/api/chat/inference"

MODEL = maritalk.MariTalk(key=API_KEY)

auth_header = {
    "authorization": f"Key {API_KEY}"
}

def get_maritalk_response(request_data, headers):
  
  response = requests.post(
      URL,
      json=request_data,
      headers=headers
  )

  if response.status_code == 429:
    print("rate limited, tente novamente em breve")

  elif response.ok:
    data=response.json()
    return(data["answer"])

  else:
    response.raise_for_status()

@app.route('/generate_history', methods=['POST'])
def generate_history():
    try:
        data = request.json

        qtd_person = data['persons']
        target_public = data['target']
        theme = data['theme']
        environment = data['environment']

        print("TASK QUEUD-----------")
        
        prompt = f"Por favor, conte uma história envolvendo {qtd_person} personagens, com o público-alvo sendo {target_public}, com o tema {theme} e o ambiente em que a história acontece é {environment}."

        print("PROMPT FINISHED-----------")

        request_data = {
            "messages": prompt,
            "chat_mode": True,
            "do_sample": True,
            "max_tokens": 1000,
            "temperature": 0.7,
        }

        response = get_maritalk_response(request_data, auth_header)
        return jsonify({'history': response})
    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)





