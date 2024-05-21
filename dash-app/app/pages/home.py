from dash import html, register_page

register_page(
    __name__,
    name='Home',
    top_nav=True,
    path='/'
)

def layout():
    page_layout = html.Div([
        html.P(
            "Welcome to the Crash Prediction Dashboard! This application provides insights and forecasts "
            "related to vehicular crashes. Our goal is to help you understand the trends and factors affecting "
            "crash occurrences and provide you with tools to predict future crashes.",
            style={'font-size': '24px', 'padding': '10px 20px'}
        ),
        html.P(
            "This project focuses on creating an interactive web application for analyzing and providing "
            "statistics on airplane crashes using a dataset downloaded from Kaggle. The application allows data "
            "visualization and provides various statistics and analyses related to airplane crashes.",
            style={'font-size': '24px', 'padding': '10px 20px'}
        ),
        html.Ul([
            html.Li([
                html.H4("Application Functionality", style={'font-size': '28px', 'padding': '10px 0'}),
                html.P(
                    "The application offers the following features:",
                    style={'font-size': '24px', 'padding': '10px 20px'}
                ),
                html.Ul([
                    html.Li("Analysis of crashes by year, location, causes, operator, and aircraft type: Users can browse and filter data based on various criteria.", style={'font-size': '24px', 'padding': '5px 20px'}),
                    html.Li("Visualization of survival rates and predictions based on historical data: The application includes various charts and visualizations that show survival rates and allow predictions of future trends.", style={'font-size': '24px', 'padding': '5px 20px'}),
                    html.Li("Viewing raw and processed data: Users can view both the original and processed data and export them in CSV and PDF formats.", style={'font-size': '24px', 'padding': '5px 20px'})
                ])]),
            html.Li([
                html.H4("Installation and Running the Application", style={'font-size': '28px', 'padding': '10px 0'}),
                html.P(
                    "To run the application, follow these steps:",
                    style={'font-size': '24px', 'padding': '10px 20px'}
                ),
                html.Ol([
                    html.Li([
                        html.P("Clone the repository", style={'font-size': '24px', 'padding': '5px 20px'}),
                        html.Pre("git clone https://github.com/your-repository/airplane-crashes.git\ncd airplane-crashes", style={'font-size': '24px', 'padding': '5px 20px'})
                    ]),
                    html.Li([
                        html.P("Install required packages", style={'font-size': '24px', 'padding': '5px 20px'}),
                        html.P("Ensure you have Python installed. Then, install the required packages using:", style={'font-size': '24px', 'padding': '5px 20px'}),
                        html.Pre("pip install -r requirements.txt", style={'font-size': '24px', 'padding': '5px 20px'})
                    ]),
                    html.Li([
                        html.P("Run the application", style={'font-size': '24px', 'padding': '5px 20px'}),
                        html.P("Start the application with the command:", style={'font-size': '24px', 'padding': '5px 20px'}),
                        html.Pre("python app.py", style={'font-size': '24px', 'padding': '5px 20px'})
                    ]),
                    html.Li([
                        html.P("Access the application", style={'font-size': '24px', 'padding': '5px 20px'}),
                        html.P("Open a web browser and go to:", style={'font-size': '24px', 'padding': '5px 20px'}),
                        html.Pre("http://127.0.0.1:8050", style={'font-size': '24px', 'padding': '5px 20px'})
                    ])
                ])]),
            html.Li([
                html.H4("Tools and Libraries Used", style={'font-size': '28px', 'padding': '10px 0'}),
                html.P(
                    "The application is built using the following tools and libraries:",
                    style={'font-size': '24px', 'padding': '10px 20px'}
                ),
                html.Ul([
                    html.Li("Dash: A framework for building web applications in Python.", style={'font-size': '24px', 'padding': '5px 20px'}),
                    html.Li("Plotly: A library for creating interactive charts and visualizations.", style={'font-size': '24px', 'padding': '5px 20px'}),
                    html.Li("Pandas: A library for data manipulation and analysis.", style={'font-size': '24px', 'padding': '5px 20px'}),
                    html.Li("NumPy: A library for numerical computations.", style={'font-size': '24px', 'padding': '5px 20px'}),
                    html.Li("Scipy: A library for scientific and technical computing.", style={'font-size': '24px', 'padding': '5px 20px'}),
                    html.Li("Statsmodels: A library for statistical modeling and time series analysis.", style={'font-size': '24px', 'padding': '5px 20px'}),
                    html.Li("Matplotlib: A library for creating static, animated, and interactive visualizations.", style={'font-size': '24px', 'padding': '5px 20px'}),
                    html.Li("Joblib: A library for efficient saving and loading of Python objects.", style={'font-size': '24px', 'padding': '5px 20px'})
                ])
            ])
        ])
    ], style={'padding': '20px'})
    return page_layout
