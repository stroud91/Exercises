from flask import Blueprint, render_template
from app.sample_form import SampleForm

bp = Blueprint('', __name__)

@bp.route('/')
def home():
    return render_template('page.html', title="Welcome")


@bp.route('/about')
def about():
    return '<h1>About</h1>'

@bp.route('/help')
def help():
    return render_template('page.html', title="Help")

@bp.route('/form', methods=['GET', 'POST'])
def form():
    # instantiate form
    form = SampleForm()
    if form.validate_on_submit():
        return 'Submit complete'
    # send form into Jinja template (with form=form)
    return render_template('form.html', form=form)
