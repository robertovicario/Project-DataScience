from ydata_profiling import ProfileReport
import os
import webbrowser

# -------------------------

def profile_data(df, file_name='data_profiling', report_title='YData Profiling Report'):
    """
    Profiles the given DataFrame and generates an HTML report.

    Parameters:
        - df (pd.DataFrame): The DataFrame to profile.
        - file_name (str): The name of the output HTML file (without extension). Default is 'data_profiling'.
        - report_title (str): The title of the report. Default is 'YData Profiling Report'.
    """

    # Ensuring the output directory exists
    WORK_DIR = os.path.abspath('../res/data-profiling')
    if not os.path.exists(WORK_DIR):
        os.makedirs(WORK_DIR)

    # Creating the report
    OUT_FILE = os.path.join(WORK_DIR, f"{file_name}.html")
    profile = ProfileReport(df, explorative=True, title=report_title)
    profile.to_file(OUT_FILE)

    # -------------------------

    # Opening the report in the default web browser
    webbrowser.open(f"file://{OUT_FILE}")
