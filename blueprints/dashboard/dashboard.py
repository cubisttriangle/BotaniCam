from flask import Blueprint, render_template

blueprint = Blueprint( 'dashboard', __name__,
                       template_folder="templates" )

@blueprint.route( "/" )
def index():
    return render_template( "dashboard/index.html" )
