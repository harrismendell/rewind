# import flask class and a render_template
from flask import Flask, render_template, request, redirect


# Create new instance of flask class
app = Flask(__name__)


@app.route('/')
def title_screen():
    return render_template('main.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/record/<recordid>/')
def record(recordid):
    # TODO use functions to dynamically rectrieve info needed to render template given a record_id

    return render_template('record.html',
                           band_name="Lemuria",
                           record="Get Better",
                           record_cover="/static/img/lemuriaGetBetter.jpg",
                           price="$10.00",
                           current_buyers="420",
                           max_buyers="500",
                           pitchfork_score="6.4",
                           pitchfork_link="http://pitchfork.com/reviews/albums/11537-get-better/",
                           days_to_go="26"
                           )

if __name__ == '__main__':
    app.run(debug=True)