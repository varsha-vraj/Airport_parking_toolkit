<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
</head>
<body>

  <h1>🚗 Airport Parking Management Toolkit</h1>

  <p><strong>Author:</strong> varshaa112003@gmail.com</p>
  <p><strong>Project Type:</strong> Python CLI Toolkit + PostgreSQL + Apache Spark</p>

  <div class="section">
    <h2>📖 Description</h2>
    <p>This toolkit is designed to simulate and manage airport parking events. It provides a command-line interface (CLI) for managing vehicles, zones, and parking events. It includes full integration with PostgreSQL for data storage, SQL for advanced queries, and Apache Spark for big data batch processing of parquet logs.</p>
  </div>

  <div class="section">
    <h2>🛠️ Technologies Used</h2>
    <table>
      <tr><th>Technology</th><th>Purpose</th></tr>
      <tr><td>Python</td><td>Core programming</td></tr>
      <tr><td>CLI</td><td>Command Line Interface</td></tr>
      <tr><td>PostgreSQL</td><td>Database backend</td></tr>
      <tr><td>SQLAlchemy</td><td>Database ORM</td></tr>
      <tr><td>Apache Spark - PySpark</td><td>ETL on parquet data</td></tr>
      <tr><td>Poetry</td><td>Dependency management</td></tr>
    </table>
  </div>

  <div class="section">
    <h2>📁 Folder Structure</h2>
    <pre>
airport_parking_project_demo/
│
├── airport_parking_toolkit/
│   ├── cli_tool.py
│   ├── spark_jobs.py
│
├── output_parquet/
│   ├── vehicles.parquet
│   ├── parking_zones.parquet
│   └── parking_events.parquet
│
├── tests/
│   ├── test_cli.py
│
├── queries/
│   ├── queries.sql
│   └── advanced_sql/
│       └── triggers.sql
│
├── logs/
│   └── parking_etl.log
│
├── load_parquet_to_db.py
├── pyproject.toml
└── README.html
    </pre>
  </div>

  <div class="section">
    <h2>🚀 How to Run</h2>
    <ol>
      <li>📦 Install dependencies:
        <pre><code>poetry install</code></pre>
      </li>
      <li>🧹 Clean old logs (if needed):
        <pre><code>rm -rf logs/parking_etl.log</code></pre>
      </li>
      <li>▶️ Run the CLI:
        <pre><code>python -m airport_parking_toolkit.cli_tool</code></pre>
      </li>
      <li>📥 Load parquet data to PostgreSQL:
        <pre><code>python load_parquet_to_db.py</code></pre>
      </li>
      <li>🔥 Run Apache Spark jobs:
        <pre><code>python airport_parking_toolkit/spark_jobs.py</code></pre>
      </li>
    </ol>
  </div>

  <div class="section">
    <h2>📸 Images</h2>
    <h3> 1. Vehicle Entry/Exit Logging<img src="https://github.com/varsha-vraj/Airport_parking_toolkit/blob/main/cs_pics/Capture1.JPG" alt="Vehicle Entry/Exit Logging" />
    <h3>Validate Parking Records<img src="https://github.com/varsha-vraj/Airport_parking_toolkit/blob/main/cs_pics/Capture2.JPG" alt="Validate Parking Records" />
    <h3>Analyze Zone Utilization<img src="https://github.com/varsha-vraj/Airport_parking_toolkit/blob/main/cs_pics/Capture3.JPG" alt="Analyze Zone Utilization" />
    <h3> Track Frequent Parkers<img src="https://github.com/varsha-vraj/Airport_parking_toolkit/blob/main/cs_pics/Capture4.JPG" alt="Track Frequent Parkers" />
    <h3> Data Quality Issues<img src="https://github.com/varsha-vraj/Airport_parking_toolkit/blob/main/cs_pics/Capture5.JPG" alt="Detect Data Quality Issues" />
    <h3> Compare Parking Zone Performance <img src="https://github.com/varsha-vraj/Airport_parking_toolkit/blob/main/cs_pics/Capture6.JPG" alt="Compare Parking Zone Performance" />
    <h3> Schema Diagram<img src="https://github.com/varsha-vraj/Airport_parking_toolkit/blob/main/cs_pics/schema.jpg" alt="Schema diagram" />
  </div>

  <div class="section">
    <h2>📚 Advanced SQL Features</h2>
    <ul>
      <li>Trigger to log insertions into <code>parking_events</code></li>
      <li>Stored Functions for computing durations</li>
      <li>Views for summarised parking statistics</li>
    </ul>
  </div>

  <div class="section">
    <h2>📦 Logs</h2>
    <p>ETL logs are written to <code>logs/parking_etl.log</code> after every Spark job run.</p>
  </div>

  <footer>
    <p>✨ Thank You </p>
  </footer>

</body>
</html>
