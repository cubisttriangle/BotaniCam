from flask import Blueprint, render_template, current_app, request, redirect, url_for

from user_form import UserForm

from ...models.Person import Person

users = Blueprint( 'users', __name__,
                   template_folder='templates' )

@users.route( '/users' )
@users.route( '/users/' )
def list():

    users = current_app.session.query( Person ).all()

    return render_template( 'users/list.html', users=users )

@users.route( '/users/<int:id>' )
@users.route( '/users/<int:id>/' )
def user( id ):

    user = current_app.session.query( Person ).filter( Person.id == id ).first()

    if not user:
        return redirect( 404 )

    return render_template( 'users/user.html', user=user )


@users.route( '/users/add', methods=( 'GET', 'POST' ) )
@users.route( '/users/add/', methods=( 'GET', 'POST' ) )
def add():

    if request.method == 'POST':

        # TODO: Handle case-insensitive, duplicates.
        person = Person( first_name=request.form['first_name'],
                         last_name=request.form['last_name'],
                         email=request.form['email'] )
        current_app.session.add( person )
        current_app.session.commit()

        # TODO: Redirect to appropriate row id
        return redirect( url_for( 'users.list' ) )

    else:

        form = UserForm()

        if form.validate_on_submit():
    
            return redirect( url_for( '/Users' ) )

    return render_template( 'users/add.html', form=form, action="add" )

@users.route( '/users/edit/<int:id>', methods=( 'GET', 'POST' ) )
@users.route( '/users/edit/<int:id>/', methods=( 'GET', 'POST' ) )
def edit( id ):

    user = current_app.session.query( Person ).filter( Person.id == id ).first()

    if not user:
        # TODO: Take a more informative action.
        return redirect( 404 )

    if request.method == 'POST':

        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.email = request.form['email']

        current_app.session.commit()

        # TODO: Redirect to appropriate row id
        return redirect( url_for( 'users.list' ) )

    else:

        form = UserForm( obj = user )

        if form.validate_on_submit():

            return redirect( url_for( 'users.list' ) )

        return render_template( 'users/add.html', form=form, action="edit", id=user.id )

@users.route( '/users/delete/<int:id>', methods=( 'GET', 'POST' ) )
def delete( id ):

    user = current_app.session.query( Person ).filter( Person.id == id ).first()

    if not user:
        # TODO: Take a more informative action.
        return redirect( 404 )

    current_app.session.delete( user )
    current_app.session.commit()

    return redirect( url_for( 'users.list' ) )