from datetime import datetime
import numpy as np 
import pandas as pd 

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#Database Setup
engine = create_engine("sqlite:///hawaii_3.db")

#Reflect database and tables
Base = automap_base()
Base.prepare(engine, reflect=True)

#Save reference to table
Measurement=Base.classes.measurement_table
Station=Base.classes.station_table

#Create session
engine= Session(engine)

#Flask Setup
app = Flask(__name__)

#Flask Routes

@app.route("/")
def welcome():
    """List all available api routes."""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"-the dates and precipitation observations from the last year<br/>"
        f"/api/v1.0/stations"
        f"- list of stations from the dataset<br/>"
        f"/api/v1.0/tobs"
        f"- list of Temperature Observations for the previous year<br/>"
        f"/api/v1.0/calc_temps/<start>/<end>"
        f"- the 'TMIN', 'TAVG', and 'TMAX' for all dates greater than and equal to the start date<br/>"
        f"/api/v1.0/calc_temps/<start>/<end>"
        f"- the 'TMIN', TAVG', and 'TMAX' for dates between the start and end date inclusive<br/>"
    )