import pandas as pd

FROM_BASE_DIR = '../../../covid-19-data'
TO_BASE_DIR = '../../website/static/data'
# date,county,state,fips,cases,deaths

def fetch_data(from_base_dir=FROM_BASE_DIR):
    # Load the data to be processed
    file_name="{}/us-counties.csv".format(from_base_dir)
    data_set = pd.read_csv(file_name, sep=',',converters={'fips': lambda x: str(x)},parse_dates=[0],
                 date_parser=lambda t:pd.to_datetime(str(t),
                                            format='%Y-%m-%d'))
    print(data_set.columns)
    max_date = max(data_set['date'])
    print("data_set (rows, columns) {}\n".format(data_set.shape))
    print("data_set missing values \n{}\n".format(data_set.isnull().sum()))
    dataTypeSeries = data_set.dtypes

    print('Data type of each column of Dataframe :')
    print(dataTypeSeries)
    return data_set, max_date

def select_cases_by_date(data_set, max_date):
    #search_dt = pd.to_datetime(str(dt_str),format='%Y-%m-%d')
    query_str = 'date == "{}"'.format(max_date)
    cases_data_set = data_set.query(query_str)
    del cases_data_set['date']
    print(cases_data_set.head())
    return cases_data_set

def aggregate_cases_by_state(data_set):
    cases_data_set = data_set.groupby('state').agg({'fips':'max','state':'min','cases':'sum','deaths':'sum'})
    cases_data_set['state_id'] = cases_data_set['fips'].str[0:2]
    del cases_data_set['fips']
    return cases_data_set

def write_data(data_set, to_base_dir=TO_BASE_DIR):
    file_name = "{}/covid_19_cases_by_state.csv".format(to_base_dir)
    data_set.to_csv(file_name, header=True, index=False)

def process_state(from_base_dir, to_base_dir):
    print("Starting process")
    data_set, max_date = fetch_data(from_base_dir)
    data_set = select_cases_by_date(data_set, max_date)
    data_set = aggregate_cases_by_state(data_set)
    write_data(data_set, to_base_dir)

def main():
    print("Starting")
    data_set, max_date = fetch_data()
    data_set = select_cases_by_date(data_set, max_date)
    data_set = aggregate_cases_by_state(data_set)
    write_data(data_set)

if __name__=='__main__':
    main()