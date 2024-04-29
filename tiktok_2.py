from tikapi import TikAPI, ValidationException, ResponseException
import json
from helpers import process_results
import pandas as pd
import sys

def get_data(hashtag):

    api = TikAPI("HrPDeGOmS3eZeIbadY5Fyc1FIo75x7VUsKRI8YZZ0mBZXQzI")

    try:
        response = api.public.hashtag(
            name=hashtag
        )

        hashtagId = response.json()['challengeInfo']['challenge']['id']

        response = api.public.hashtag(
            id=hashtagId
        )

        # Lista para almacenar todos los datos obtenidos del hashtag "funny"
        all_data = []

        # Almacena los datos obtenidos en la lista hasta que el cursor sea igual a 30
        while response and response.json().get('cursor') != '60':
            cursor = response.json().get('cursor')
            print("Getting next items ", cursor)
            all_data.append(response.json())
            response = response.next_items()
        
        # Process data
        data_final = process_results(all_data)

        # # Escribe todos los datos en un archivo JSON
        # with open('inmuebles_data_test.json', 'w') as f:
        #     json.dump(data_final, f)

        # Convert the preprocess data to a dataframe
        df = pd.DataFrame.from_dict(data_final, orient='index')
        df.to_csv('data_final.csv', index=False)

    except ValidationException as e:
        print(e, e.field)

    except ResponseException as e:
        print(e, e.response.status_code)

if __name__ == '__main__':
    get_data(sys.argv[1])