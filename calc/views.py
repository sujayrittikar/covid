from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def get(request):
    state = request.GET["state"]

# COVID-19 Counts

    def state_counts(main_df, state_code):
        x = dict(main_df.iloc[1][state_code])
        confirmed = x['confirmed']
        deceased = x['deceased']
        recovered = x['recovered']
        tested = x['tested']
        response = "Confirmed Cases are: " + str(confirmed) + ", Deceased Cases: " + str(deceased) + ", Recovered Cases: " + str(recovered) + " and Tested Cases: " + str(tested)
        return response

    def response_giver(State = None):
        import urllib, json
        import pandas as pd
        url = "https://api.covid19india.org/v3/data.json"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        main_df = pd.DataFrame(data)
        main_df = main_df.drop(['delta', 'meta'], axis=0)
        main_df = main_df.fillna(0)
        state_codes = {'Andaman and Nicobar Islands': 'AN', 'Andhra Pradesh': 'AP', 'Arunachal Pradesh': 'AR', 'Assam': 'AS', 'Bihar': 'BR', 'Chandigarh': 'CH', 'Chattisgarh': 'CT', 'Dadra and Nagar Haveli': 'DN', 'Delhi': 'DL', 'Goa': 'GA', 'Gujarat': 'GJ', 'Haryana': 'HR', 'Himachal Pradesh': 'HP', 'Jammu and Kashmir': 'JK', 'Jharkhand': 'JH', 'Karnataka': 'KA', 'Kerala': 'KL', 'Lakshadweep Islands': 'LD', 'Madhya Pradesh': 'MP', 'Maharashtra': 'MH', 'Manipur': 'MN', 'Meghalaya': 'ML', 'Mizoram': 'MZ', 'Nagaland': 'NL', 'Odisha': 'OR', 'Pondicherry': 'PY', 'Punjab': 'PB', 'Rajasthan': 'RJ', 'Sikkim': 'SK', 'Tamil Nadu': 'TN', 'Telangana': 'TG', 'Tripura': 'TR', 'Uttar Pradesh': 'UP', 'Uttarakhand': 'UT', 'West Bengal': 'WB'}
        if State in state_codes:
            sc = state_codes[State]
        else: 
            sc = None
        if sc == None:
            resp = state_counts(main_df, 'TT')
        else:
            try:
                resp = state_counts(main_df, sc)
            except:
                resp = state_counts(main_df, 'TT')
        return resp
        

    return render(request, 'result.html', {'result':response_giver(state)})