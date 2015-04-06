from flask import render_template, g, request, redirect, url_for, flash
from flask.ext.login import login_user,  logout_user
from models import select_record, get_shop_info, User, insert_user
from rewind import app, login_manager

# routes
@app.route('/')
def title_screen():
    return render_template('main.html')

@app.route('/shop')
def shop():
    return render_template('shop.html', records=get_shop_info())

@app.route('/record/<recordid>/')
def record(recordid):
    rec = select_record(recordid)[0]
    return render_template('record.html',
                           band=rec[1],
                           record=rec[2],
                           record_cover=rec[3],
                           price=rec[4],
                           current_buyers=rec[5],
                           max_buyers=rec[6],
                           pitchfork_score=rec[7],
                           pitchfork_link=rec[8],
                           review_snippet=rec[9],
                           days_to_go=rec[10]
                           )

@app.route('/signup')
def signup():
    return '''
        <form action="/signup/confirm" method="post">
            <p>Username: <input name="username" type="text"></p>
            <p>Password: <input name="password" type="password"></p>
            <input type="submit">
        </form>
    '''
@app.route('/signup/confirm', methods=['post'])
def signup_confirm():
    import ipdb; ipdb.set_trace()
    user = insert_user(request.form['username'], request.form['password'])
    login_user(user)
    return redirect(url_for('/'))

@app.route('/login')
def login():
    return '''
        <form action="/login/check" method="post">
            <p>Username: <input name="username" type="text"></p>
            <p>Password: <input name="password" type="password"></p>
            <input type="submit">
        </form>
    '''

@app.route('/login/check', methods=['post'])
def login_check():
    # validate username and password
    user = User.get(request.form['username'])
    if (user and user.password == request.form['password']):
        login_user(user)
        user.is_authenticated = True;
    else:
        flash('Username or password incorrect')

    return redirect(url_for('/'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('/'))