<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Airport Parking Management Toolkit - README</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f8fc;
      color: #333;
      padding: 20px;
      line-height: 1.6;
    }
    h1, h2 {
      color: #2c3e50;
    }
    table {
      border-collapse: collapse;
      width: 100%;
      margin-bottom: 20px;
    }
    th, td {
      border: 1px solid #ddd;
      padding: 10px;
    }
    th {
      background-color: #3498db;
      color: white;
    }
    code {
      background-color: #eef;
      padding: 2px 6px;
      border-radius: 3px;
    }
    .emoji {
      font-size: 1.2em;
    }
    .section {
      margin-bottom: 40px;
    }
    img {
      width: 100%;
      max-width: 800px;
      margin: 10px 0;
      border: 1px solid #ccc;
      border-radius: 6px;
    }
  </style>
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
      <tr><td>Click</td><td>Command Line Interface</td></tr>
      <tr><td>PostgreSQL</td><td>Database backend</td></tr>
      <tr><td>SQLAlchemy</td><td>Database ORM</td></tr>
      <tr><td>Apache Spark</td><td>ETL on parquet data</td></tr>
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
    <p>Replace the links with raw GitHub URLs after uploading your images:</p>
    <img src="https://raw.githubusercontent.com/yourusername/yourrepo/main/images/img1.png" alt="Screenshot 1" />
    <img src="https://raw.githubusercontent.com/yourusername/yourrepo/main/images/img2.png" alt="Screenshot 2" />
    <img src="https://raw.githubusercontent.com/yourusername/yourrepo/main/images/img3.png" alt="Screenshot 3" />
    <img src="https://raw.githubusercontent.com/yourusername/yourrepo/main/images/img4.png" alt="Screenshot 4" />
    <img src="https://raw.githubusercontent.com/yourusername/yourrepo/main/images/img5.png" alt="Screenshot 5" />
    <img src="https://raw.githubusercontent.com/yourusername/yourrepo/main/images/img6.png" alt="Screenshot 6" />
    <img src="https://raw.githubusercontent.com/yourusername/yourrepo/main/images/img7.png" alt="Screenshot 7" />
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
    <p>✨ Built with ❤️ and Python</p>
  </footer>

</body>
</html>
