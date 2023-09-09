from flask import Blueprint, render_template

bp = Blueprint('inventory', __name__, url_prefix='/inventory')

@bp.route('/item/<int:id>')
def item(id):
    if(id > 0 and id< 100):
        item = {
            'id': id,
            'name': f"Fancy Item with ID of {id}",
            'description': "Comming Soon!!"
        }
        return render_template('item.html', item=item )
    else:
        return '<h1>Item not found !</h1>'
