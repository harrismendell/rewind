from flask import render_template, g, request, redirect, url_for, flash
from flask.ext.login import login_user,  logout_user, current_user, login_required
from models import select_record, get_shop_info, User, insert_user, buy_record, search_for_record, add_blog_post, get_blogs, remove_blog_data
from rewind import app, login_manager
import json


# routes
@app.route('/')
def title_screen():
    return render_template('main.html')

# routes
@app.route('/blog', methods=['post', 'get'])
def blog():
    if request.method == 'POST':
        data = add_blog_post(request.form)
    else:
        data = get_blogs()
    return render_template('blog.html', blogs=reversed(data))

# routes
@app.route('/manage_blog')
def manage_blog():
    return render_template('manage_blog.html')

@app.route('/remove/<blog>', methods=['POST'])
def remove_blog(blog):
    if current_user.is_anonymous() or (current_user.is_admin == 0):
        return render_template('admin.html')
    remove_blog_data(blog)   
    return redirect('/blog')


@app.route('/shop')
def shop():
    records = get_shop_info()
    return render_template('shop.html', records=records)

@app.route('/search', methods=['post'])
def search():
    url = search_for_record(request.form['srch-term'])
    if url == '':
        return render_template('no_record_found.html', term=request.form['srch-term'])
    return redirect(url)


@app.route('/record/<record>/')
def record(record):
    data = select_record(record)
    data_json = json.dumps(data)
    already_bought = False
    if not current_user.is_anonymous():
        for rec in current_user.records:
            if rec['record'] == record:
                already_bought = True

    return render_template('record.html', data=data, data_json=data_json, already_bought=already_bought)
                   

@app.route('/payment_confirm', methods=['post'])
@login_required
def payment_confirm():
    username = current_user.id
    buy_record(username, request.form['band'], request.form['record'],
               request.form['record_cover'], request.form['price'],
               request.form['days_to_go'])
    # below redirect not working.
    return redirect('/shop')


@app.route('/account')
@login_required
def account():
    records = current_user.get_bought_records()
    return render_template('account.html', user=current_user.name, records=records)


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signup/confirm', methods=['post'])
def signup_confirm():
    user = insert_user(request.form['username'], request.form['password'])
    login_user(user)
    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login/check', methods=['post'])
def login_check():
    try:
        user = User.get(request.form['username'])
        if (user and user.password == request.form['password']):
            login_user(user)
        else:
            return redirect('/login')
    except KeyError:
        return redirect('/login')

    return redirect('/')


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

@app.route('/contact')
def contact():
    return render_template('contact.html')