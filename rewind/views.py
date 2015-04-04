from flask import render_template
from rewind import app
# routes
@app.route('/')
def title_screen():
    return render_template('main.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/record/<recordid>/')
def record(recordid):
    # TODO use functions to dynamically retrieve info needed to render template (given a record_id).

    return render_template('record.html',
                           band_name="Lemuria",
                           record="Get Better",
                           record_cover="/static/img/lemuriaGetBetter.jpg",
                           price="$10.00",
                           current_buyers="420",
                           max_buyers="500",
                           pitchfork_score="6.4",
                           pitchfork_link="http://pitchfork.com/reviews/albums/11537-get-better/",
                           review_snippet="\"We have a lot of fun rappin' with ya here at Pitchfork, but let's get serious for a moment: were the 1990s really that bad? Maybe it's a sign I need to spend less time talking with other music writers, because the consensus appears to be an overwhelming, \'dear fucking god,\' TOTALLY. Maybe I'm just naive, having exited the decade as a teen, but Pinkerton, the NHL 92-96, Higher Learning...we had some good times, right? It's within this context that I fear for Lemuria, even with a promising debut in tow. Because their sales pitch can definitely double as a dealbreaker for some: This sounds just like 1993...\"",
                           days_to_go="26"
                           )