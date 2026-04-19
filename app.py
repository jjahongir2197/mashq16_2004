@app.route('/result12', methods=['GET', 'POST'])
def result12():
    res = None
    
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()

        if '@' in email and phone.startswith('+') and len(phone) >= 11:
            res = [email, phone]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

    return render_template('result12.html', res=res)
