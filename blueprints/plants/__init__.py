from flask import Blueprint, render_template, current_app, request, redirect, url_for

from plant_form import PlantForm

from ...models.Plant import Plant

plants = Blueprint( 'plants', __name__,
                   template_folder='templates' )

@plants.route( '/plants' )
@plants.route( '/plants/' )
def list():

    plants = current_app.session.query( Plant ).all()

    return render_template( 'plants/list.html', plants=plants )

@plants.route( '/plants/<int:id>' )
@plants.route( '/plants/<int:id>/' )
def plant( id ):

    plant = current_app.session.query( Plant ).filter( Plant.id == id ).first()

    if not plant:
        return redirect( 404 )

    return render_template( 'plants/plant.html', plant=plant )


@plants.route( '/plants/add', methods=( 'GET', 'POST' ) )
@plants.route( '/plants/add/', methods=( 'GET', 'POST' ) )
def add():

    if request.method == 'POST':

        # TODO: Handle case-insensitive, duplicates.
        plant = Plant( genus=request.form['genus'],
                        species=request.form['species'],
                        common_name=request.form['common_name'] )
        current_app.session.add( plant )
        current_app.session.commit()

        # TODO: Redirect to appropriate row id
        return redirect( url_for( 'plants.list' ) )

    else:

        form = PlantForm()

        if form.validate_on_submit():
    
            return redirect( url_for( 'plants.list' ) )

    return render_template( 'plants/add.html', form=form, action="add" )

@plants.route( '/plants/edit/<int:id>', methods=( 'GET', 'POST' ) )
@plants.route( '/plants/edit/<int:id>/', methods=( 'GET', 'POST' ) )
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

@plants.route( '/plants/delete/<int:id>', methods=( 'GET', 'POST' ) )
@plants.route( '/plants/delete/<int:id>/', methods=( 'GET', 'POST' ) )
def delete( id ):

    plant = current_app.session.query( Plant ).filter( Plant.id == id ).first()

    if not plant:
        # TODO: Take a more informative action.
        return redirect( 404 )

    current_app.session.delete( plant )
    current_app.session.commit()

    return redirect( url_for( 'plants.list' ) )
