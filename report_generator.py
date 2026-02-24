import os
from datetime import datetime

def generate_html_dashboard(all_devices_data):
    os.makedirs("reports", exist_ok=True)

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Network Monitoring Dashboard</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f6f9;
                padding: 20px;
            }}
            h1 {{
                text-align: center;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
                background: white;
            }}
            th, td {{
                padding: 12px;
                text-align: center;
                border-bottom: 1px solid #ddd;
            }}
            th {{
                background-color: #2c3e50;
                color: white;
            }}
            .HEALTHY {{
                color: green;
                font-weight: bold;
            }}
            .STABLE {{
                color: orange;
                font-weight: bold;
            }}
            .CRITICAL {{
                color: red;
                font-weight: bold;
            }}
            .card {{
                background: white;
                padding: 15px;
                border-radius: 8px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                margin-bottom: 20px;
            }}
        </style>
    </head>
    <body>

    <h1>Network Monitoring Dashboard</h1>

    <div class="card">
        <strong>Report Generated At:</strong> {datetime.now()}
    </div>

    <table>
        <tr>
            <th>Device Name</th>
            <th>Total Interfaces</th>
            <th>Interfaces Down</th>
            <th>Health Score</th>
            <th>Status</th>
        </tr>
    """

    for device in all_devices_data:
        html_content += f"""
        <tr>
            <td>{device['name']}</td>
            <td>{device['total']}</td>
            <td>{device['down']}</td>
            <td>{device['health']:.2f}%</td>
            <td class="{device['status']}">{device['status']}</td>
        </tr>
        """

    html_content += """
    </table>
    </body>
    </html>
    """

    with open("reports/dashboard.html", "w") as file:
        file.write(html_content)