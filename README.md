## To run...

1. Install required dependencies:
   > sudo apt install python3 python3-pip python3-virtualenv

1. Clone this project:
   > git clone git@github.com:cubisttriangle/BotaniCam.git

1. Enter project directory:
   > cd BotaniCam

1. If you haven't already, create a virtual environment:
   > mkdir ./venv
   
   > virtualenv ./venv

1. Activate the virtual environment:
   > source ./venv/bin/activate

1. Install required packages:
   > pip install -r ./requirements.txt

1. Run the app locally:
   > FLASK_APP=webapp python -m flask run

1. When you're done, stop the flask process. Then deactivate the virtual environment with:
   > deactivate

To override the settings in config.py. Create a folder in the top-level project directory called instance and add your custom config.py there.

1. Create instance directory. This shouldn't be added to version control.
   > mkdir instance

1. Copy the config.py from the root dir to your instance folder and override whatever variables you like.
   > cp ./config.py ./instance/config.py
