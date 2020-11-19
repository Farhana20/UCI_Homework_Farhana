import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask,jsonify
import datetime as dt


#set database and create engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#reflecting an existing db in a new model

Base = automap_base()

#reflecting the tables

Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


# Create our session (link) from Python to the DB
session = Session(engine)

#Flask Name

app = Flask(__name__)

#Flask Routes

@app.route("/")
def home():
    return (
        f"<p> Hawaii Weather API</p>"
        f"<p> Available routes:</p>"
        f"<br/>"
        f"/api/v1.0/precipitation<br/> List of previous year precipitation for all stations"
        f"<br/>"
        f"/api/v1.0/stations<br/>List of weather stations"
        f"<br/>"
        f"/api/v1.0/tobs<br/> List of Teamperature Observations (tobs) for most active station"
        f"<br/>"
        f"/api/v1.0/<start> <br> Calculates the MIN/AVG/MAX temperature for all dates greater than and equal to the start date <br/>"
        f"<br/>"
        f"/api/v1.0/<start>/<end> <br> Calculate the MIN/AVG/MAX temperature for dates between the start and end date inclusive<br/>"



    )



@app.route("/api/v1.0/precipitation")
def precipitation():
    #query for previous 12 months of precipitation data
    latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    latest_date = latest_date[0]
    year_ago = dt.datetime.strptime(latest_date, "%Y-%m-%d") - dt.timedelta(days=366)
    previous_yr_prcp = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_ago).all()
    
    #returning the dict in a jsonified formart
    precipitation_data = dict(previous_yr_prcp)
    return jsonify(precipitation_data)

    ###############################################################################################################
@app.route("/api/v1.0/stations")
def stations():
    station_name = session.query(Station.name, Station.station)
    stations = pd.read_sql(station_name.statement, station_name.session.bind)
    return jsonify(stations.to_dict())

####################################################################################################

@app.route("/api/v1.0/tobs")
def tobs():
    # define dates
    latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    latest_date = latest_date[0]
    year_ago = (dt.datetime.strptime(latest_date, "%Y-%m-%d") - dt.timedelta(days=365)).date()

#query for date and temperatuture observations for previous year

    tobs_dates = session.query(Measurement.date, Measurement.tobs).\
                    filter(Measurement.date >= year_ago).order_by(Measurement.date).all()

    #Create list of dicts with date and tobs

    tobs_year = []

    for data in tobs_dates:
        row = {}
        row["date"] = data[0]
        row["tobs"] = data[1]
        tobs_year.append(row)
            
    return jsonify(tobs_year)

###################################################################################################

@app.route("/api/v1.0/<start>") 
def start(start):
    
    start_date = session.query(Measurement.date,func.avg(Measurement.tobs),func.min(Measurement.tobs),func.max(Measurement.tobs)) \
             .filter(Measurement.date >= start).group_by(Measurement.date).all()
    
    return jsonify(start_date)

################################################################################################

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    
      
    range_date = session.query(Measurement.date,func.avg(Measurement.tobs),func.min(Measurement.tobs),func.max(Measurement.tobs)) \
             .filter(Measurement.date >= start).filter(Measurement.date <= end).group_by(Measurement.date).all()
    
    return jsonify(range_date)

if __name__ == '__main__':
    app.run(debug=True)

    

    

