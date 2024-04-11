<h1>Radix Internship Challenge</h1>

<h2>The Challenge</h2>
The project consists on creating a simple back/front-end infrastructure to receive data from the sensors of an Oil & Gas Company and display them to the user.

<h2>The Tasks</h2>
<ul>
  <li>Model a database</li>
  <li>Create an API to:</li>
  <ul>
    <li>Receive and store the data from a JSON</li>
    <li>Receive and store the data from a CSV File</li>
    <li>Display the average value from the readings of a requested equipment sensors based on a specific period of time(24h, 48h, 1 week or 1 month)</li>
  </ul>
  <li>Write a documentation</li>
</ul>

<h2>The Project</h2>
<h3>Technologies Used</h3>
  The project was created using: 
  <ul>
    <li>Backend(Python)</li>
      <ul>
        <li>Flask</li>
        <li>SQLAlchemy</li>
        <li>SQLite</li>
      </ul>
    <li>Frontend(JavaScript)</li>
      <ul>
        <li>JQuery(AJAX)</li>
        <li>Charts.js</li>
      </ul>
  </ul>

  Other apps were also used, like Insomnia and SQLiteStudio, for testing requests and checking the DB.
  
  <h3>Database</h3>
  For the database, the table sensor_data was created, as in the following image:
    
  ![sensor_data_table](https://github.com/guiSantiago/Desafio-Radix/assets/68828288/759dfbc4-fe7a-400c-8a69-80879aa27b37)
  
  <h3>Structure</h3>
  <ul>
  <li>app.py: the main file, where the db and the API were defined</li>
  <li>templates/ : directory containing the main HTML file </li>
    <li>index.html : the main file for the graphic interface, containing the HTML structure and the requests logic</li>
  <li>static/ : directory containing the main CSS file </li>
  </ul>

  <h3>Installation and Usage</h3>
  <ul>
  <li>Clone the project repository to your local machine</li>
  <li>Install the Python dependencies listed in the requirements.txt file using pip3 (Command: pip3 install requirements.txt)</li>
  <li>Run the Flask server using the python app.py command</li>
  <li>Access the application in your browser at http://localhost:5000</li>
  <li>Insert data sending requests from Insomnia or other method of your preference</li>
  </ul>

  <h3>Endpoints</h3>
  <ul>
  <li>GET</li>
    <ul>
      <li>/equipments : get all the equipment IDs registered</li>
        Expected Response:
        <code>{
                  "equipment_ids": [
                  "EQ-4",
                  "EQ-2",
                  "EQ-6",
                  "EQ-1"
                  ]
              }
        </code>
      <li>/all_equipments : get all the equipment IDs and data registered</li>
         Expected Response:
        <code>
          {
            "EQ-1": [
              {
                "timestamp": "Mon, 08 Apr 2024 10:30:00 GMT",
                "value": "80.0000000000"
              },
              {
                "timestamp": "Mon, 08 Apr 2024 10:30:00 GMT",
                "value": "82.0000000000"
              }
            ],
            "EQ-2": [
              {
                "timestamp": "Mon, 08 Apr 2024 10:30:00 GMT",
                "value": "80.0000000000"
              },
              {
                "timestamp": "Mon, 08 Apr 2024 10:30:00 GMT",
                "value": "80.8000000000"
              }
            ],
            "EQ-4": [
              {
                "timestamp": "Mon, 08 Apr 2024 10:30:00 GMT",
                "value": "80.2300000000"
              }
            ]
          }
        </code>   
        <li>/avg_value : get the average value from specific equipment</li>
        Params: equipmentId, period <br>
        Expected Response:
        <code>
          {
            "avg_value": 82.0
          }
        </code>
    </ul>
    <li>POST</li>
    <ul>
      <li>/sensor_data : post data from specific equipment</li>
        Expected Body: <br>
         <code>{
                  "equipmentId": "EQ-1",
                  "timestamp": "2024-04-10T18:30:00.000-05:00",
                  "value": 7.09
                }  
        </code>
        <br>
        Expected Response:<br>
        <code>{
                "message": "Sensor data stored with success!"
              }
        </code>
      <li>/sensor_data_csv : post data from specific equipment</li>
        Expected Body: <br>
         <code>Multipart Form</code>
        <code>file: chosen_file.csv</code>
        <br>
        Expected Response:<br>
        <code>{
                "message": "CSV data stored with success!"
              }
        </code>
    </ul>
  </ul>

  

  






