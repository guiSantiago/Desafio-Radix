from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import csv
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sensors.db'
db = SQLAlchemy(app)

#sensor class
class SensorData(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    equipmentId = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime)
    value =db.Column(db.Float(10,2), nullable=False)


@app.route('/', methods= ['GET'])
def health_check():
     return jsonify({'message': 'Online!'}), 200 


#endpoint to send sensor data for storage
@app.route('/send_sensor_data', methods= ['POST'])
def get_sensor_data():
    data = request.json
    new_data = SensorData(
        equipmentId=data['equipmentId'],
        timestamp=datetime.strptime(data['timestamp'], '%Y-%m-%dT%H:%M:%S.%f%z'),
        # timestamp=datetime.utcnow(),
        value=round(data['value'], 2)
    )
    db.session.add(new_data)
    db.session.commit()
    
    return jsonify({'message': 'Sensor data stored with success!'}), 200

#endpoint to get average value in specific period of time
@app.route('/get_avg_value', methods=['GET'])
def avg_value():
    equipment_id = request.args.get('equipmentId')
    period = request.args.get('period')
    
    if period == '24h':
        start_period = datetime.now() - timedelta(hours=24)
    elif period == '48h':
        start_period = datetime.now() - timedelta(hours=48)
    elif period == '1w':
        start_period = datetime.now() - timedelta(weeks=1)
    elif period == '1m':
        start_period = datetime.now() - timedelta(days=30)
    else:
        return jsonify({'error': 'Please set a valid period of time (24h / 48h / 1w / 1m)!'}), 400

    req_data = db.session.query(db.func.avg(SensorData.value)).filter(SensorData.equipmentId == equipment_id, SensorData.timestamp >= start_period).scalar()
    result = round(req_data, 2)
    return jsonify({'avg_value': result}), 200

#endpoint to post CSV file with sensor data
@app.route('/post_sensor_data_csv', methods=['POST'])
def post_csv():
    csv_file = request.files['file']
    csv_file.save(csv_file.filename)
    
    with open(csv_file.filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_data = SensorData(
                equipmentId=row['equipmentId'],
                timestamp=datetime.strptime(row['timestamp'], '%Y-%m-%dT%H:%M:%S.%f%z'),
                value=float(row['value'])
            )
            db.session.add(new_data)
            db.session.commit()
    
    return jsonify({'message': 'CSV data stored with success!'}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    