from flask import Blueprint, render_template, current_app, request, redirect, url_for

from .plant_form import PlantForm
from .plant_photo_form import PlantPhotoForm

from ...models.Plant import Plant
from ...models.PlantPhoto import PlantPhoto

plants = Blueprint( 'plants', __name__, url_prefix='/plants',
                   template_folder='templates' )

plant_fields=[ 'id', 'common_name', 'genus', 'species' ]

@plants.route( '' )
@plants.route( '/' )
def list():

    plants = current_app.session.query( Plant ).all()

    return render_template( 'simple_list.html',
                            name_plural='plants',
                            name_singular='plant',
                            objs=plants,
                            fields=plant_fields )

@plants.route( '/add', methods=( 'GET', 'POST' ) )
@plants.route( '/add/', methods=( 'GET', 'POST' ) )
def add():

    if request.method == 'POST':

        # TODO: Handle case-insensitive, duplicates.
        plant = Plant( common_name=request.form['common_name'],
                       genus=request.form['genus'],
                       species=request.form['species'] )
        current_app.session.add( plant )
        current_app.session.commit()

        # TODO: Redirect to appropriate row id ( '/plants#id' )
        return redirect( url_for( 'plants.list' ) )

    else:

        form = PlantForm()

        if form.validate_on_submit():
    
            return redirect( url_for( 'plants.list' ) )

    return render_template( 'plants/add.html', form=form, action="add" )

@plants.route( '<int:id>' )
@plants.route( '<int:id>/' )
def plant( id ):

    plant = current_app.session.query( Plant ).filter( Plant.id == id ).first()

    if not plant:
        return redirect( 404 )

    return render_template( 'simple_obj.html', obj=plant, fields=plant_fields )


@plants.route( '/<int:id>/edit', methods=( 'GET', 'POST' ) )
@plants.route( '/<int:id>/edit/', methods=( 'GET', 'POST' ) )
def edit( id ):

    plant = current_app.session.query( Plant ).filter( Plant.id == id ).first()

    if not plant:
        # TODO: Take a more informative action.
        return redirect( 404 )

    if request.method == 'POST':

        plant.genus = request.form['genus']
        plant.species = request.form['species']
        plant.common_name = request.form['common_name']

        current_app.session.commit()

        # TODO: Redirect to appropriate row id
        return redirect( url_for( 'plants.list' ) )

    else:

        form = PlantForm( obj = plant )

        if form.validate_on_submit():

            return redirect( url_for( 'plants.list' ) )

        return render_template( 'plants/add.html', form=form, action="edit", id=plant.id )

@plants.route( '/<int:id>/delete', methods=( 'GET', 'POST' ) )
@plants.route( '/<int:id>/delete/', methods=( 'GET', 'POST' ) )
def delete( id ):

    plant = current_app.session.query( Plant ).filter( Plant.id == id ).first()

    if not plant:
        # TODO: Take a more informative action.
        return redirect( 404 )

    current_app.session.delete( plant )
    current_app.session.commit()

    return redirect( url_for( 'plants.list' ) )

@plants.route( '/<int:id>/add_photo', methods=( 'GET', 'POST' ) )
@plants.route( '/<int:id>/add_photo/', methods=( 'GET', 'POST' ) )
def add_photo( id ):

    if request.method == 'POST':

        # TODO: Handle case-insensitive, duplicates.
        photo = PlantPhoto( plant_id=id,
                            photo_path=request.form['photo_path'] )
        current_app.session.add( photo )
        current_app.session.commit()

        # TODO: Redirect to appropriate row id ( '/plants#id' )
        return redirect( url_for( 'plants.list' ) )

    else:

        form = PlantPhotoForm()

        if form.validate_on_submit():

            return redirect( url_for( 'plants.list' ) )

    return render_template( 'plants/add_photo.html', form=form, id=id )
