import git
import os
from data_prep.covid_19_ny_times_data_prep.covid_19_cases_by_county import process_county
from data_prep.covid_19_ny_times_data_prep.covid_19_cases_by_state import process_state


#WEBSITE_HOME=${PRJ_BASE}/covid_19_analysis
#DATA_HOME=${PRJ_BASE}/covid-19-data


def check_nytimes_data():
    uname = os.uname()
    if uname.sysname == "Darwin":
        prj_base = "/Users/danhiggins/Code/GATech/CSE6242_Data_Visual_Analytics"
    else:
        prj_base = "/home/ubuntu/Applications"

    g = git.cmd.Git(prj_base+"/covid-19-data")
    ret_val = g.pull()
    print("message = {}".format(ret_val))
    if ret_val == "Already up to date.":
        print("do nothing")
    else:
        print("process data")
        from_base_dir = '{}/covid-19-data'.format(prj_base)
        to_base_dir = '{}/covid_19_analysis/website/static/data'.format(prj_base)
        to_html_dir = '{}/covid_19_analysis/website/templates'.format(prj_base)
        process_county(from_base_dir, to_base_dir, to_html_dir)
        process_state(from_base_dir, to_base_dir)

if __name__ == "__main__":
    check_nytimes_data()