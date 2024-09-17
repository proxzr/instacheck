from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_email', methods=['POST'])
def check_email():
    email = request.form.get('email')

    url = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'

    headers = {
        'accept': '*/*',
        'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'mid=Zrd1ywAEAAGo9MoUL7ozjHiaWoQS; ig_did=E7527B4D-55E7-459C-955D-ADF145684C63; datr=Lv7EZiiJuVlrVZnI8Gryq2qB; shbid="7897\\05453202852429\\0541757598790:01f79e7dfb37f022d3e26dcbd5f5529bcd5a0f5cc5a692dfe7d58c50dd52f3265a77eeec"; shbts="1726062790\\05453202852429\\0541757598790:01f7c4125e06b9506a69e47daa0af9ba7a9b926a23b2e9f091b0103dfb542e037520de3f"; oo=v1%7C3%3A1725742980; rur="CLN\\05468862603594\\0541757954971:01f71b4785e6f4c3aa83c7b83cfa7e479d290f3a0c04ea4ccbe7451dba534149c249ba41"; csrftoken=Ba1B9QlE9YQeFkxvfvDi4P2k7eOKyE1r; wd=604x735',
        'origin': 'https://www.instagram.com',
        'pragma': 'no-cache',
        'referer': 'https://www.instagram.com/accounts/emailsignup/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-model': '"Nexus 5"',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36',
        'x-asbd-id': '129477',
        'x-csrftoken': 'Ba1B9QlE9YQeFkxvfvDi4P2k7eOKyE1r',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR1JSESfJX5jlfbVenNwZ7e-Rfu9wAFSzONf2lm4Xdc_HKWD',
        'x-instagram-ajax': '1016508803',
        'x-requested-with': 'XMLHttpRequest'
    }

    data = {
        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1726419038:AeFQAJKDDYIf0N4r2MOuseJ50oNOvyCQ4tVhYsIdqELT+V4S5q0TgUEI8OG1zBEa3vr7+ReGttjU/s0H6uWdRxcIuYtrRMnCdMsPMfGnoro0p4NIo0yV/SbsFXC9CnAAEowyn94eKzFCubnDJznb+Kp2Fw==',
        'email': email,
        'first_name': 'aaaaa',
        'username': 'aaaaaaaaaaaaajiehfj298',
        'client_id': 'Zrd1ywAEAAGo9MoUL7ozjHiaWoQS',
        'seamless_login_enabled': '1',
        'opt_into_one_tap': 'false',
        'use_new_suggested_user_name': 'true'
    }

    response = requests.post(url, headers=headers, data=data)
    
    try:
        response_json = response.json()
    except requests.exceptions.JSONDecodeError:
        result = "there is a problem here lol"
        return render_template('result.html', email=email, result=result, exists=False)
    
    exists = False
    if 'errors' in response_json and 'email' in response_json['errors']:
        email_error = response_json['errors']['email'][0]['code']
        if email_error == 'email_is_taken':
            result = "This email is associated with an Instagram account ! 🚀"
            exists = True
        else:
            result = "This email is not associated with an Instagram account! 😳"
    else:
        result = "This email is not associated with an Instagram account! 😳"

    return render_template('result.html', email=email, result=result, exists=exists)

if __name__ == '__main__':
    app.run(debug=True)
