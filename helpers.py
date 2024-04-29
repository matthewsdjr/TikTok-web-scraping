def process_results(data):

    # Valores que obtendremos de value['itemList']
    nested_values = ['desc', 'author', 'music', 'authorStats', 'stats', 'statsV2', 'video']
    # Valores que necesitaremos de cada dato de nested_value
    author_values = ['id', 'nickname', 'uniqueId', 'signature']
    video_values = ['duration', 'format', 'height']
    authorStats_values = ['followerCount', 'followingCount', 'heart', 'videoCount']
    stats_values = ['commentCount', 'playCount']
    music_values = ['album', 'authorName']      
    statsV2_values = ['playCount', 'commentCount', 'diggCount']
    # Nuevo diccionario para almacenar datos los keys() que necesitemos que estaran anidados para 
    # Posteriormente extraer los ideales
    flattened_data = {}
    # Iteramos en la data desordenada que extrajimos
    for value in data:
        # idx es el indice de la cantidad de busqueda que hicimos con la API de tiktok, esto nos arrojo 30 usuarios
        # crt vendrian a ser los valores
        # itemList es el key() principal donde esta toda la data que necesitamos
        for idx, crt in enumerate(value['itemList']):
            # En el diccionario creado anteriormente ordenamos los 30 usuarios que obtuvimos
            flattened_data[idx] = {}
            # de itemList extraemos toda la data que obtuvimos de la API
            for prop_idx, prop_value in crt.items():
                # Solo necesitamos datos predeterminados anteriormente en neste_values
                if prop_idx in nested_values:
                    # Rellenamos nuestro diccionario con la data necesitada
                    flattened_data[idx][prop_idx] = prop_value

    # Nuevo diccionario para almacenar los datos filtrados de flattened_data
    filtered_data = {}
    # Iterar sobre los datos obtenidos anteriormente
    for idx, crt in flattened_data.items():
        filtered_data[idx] = {}
        if 'desc' in crt:
            filtered_data[idx]['desc'] = {crt['desc']}
        # Extraer valores de 'author'
        if 'author' in crt:
            filtered_data[idx]['author'] = {key: value for key, value in crt['author'].items() if key in author_values}
        # Extraer valores de 'music'
        if 'music' in crt:
            filtered_data[idx]['music'] = {key: value for key, value in crt['music'].items() if key in music_values}
        # Extraer valores de 'authorStats'
        if 'authorStats' in crt:
            filtered_data[idx]['authorStats'] = {key: value for key, value in crt['authorStats'].items() if key in authorStats_values}
        # Extraer valores de 'stats'
        if 'stats' in crt:
            filtered_data[idx]['stats'] = {key: value for key, value in crt['stats'].items() if key in stats_values}
        # Extraer valores de 'statsV2'
        if 'statsV2' in crt:
            filtered_data[idx]['statsV2'] = {key: value for key, value in crt['statsV2'].items() if key in statsV2_values}

    # Nuevo diccionario para almacenar los valores totales con claves modificadas
    modified_data = {}
    # Iterar sobre los datos filtrados
    for idx, crt in filtered_data.items():
        modified_data[idx] = {}
        # Verificar y anadir desc a la data final
        if 'desc' in crt:
            # crt['desc'] vendria a ser un set, por lo que tenemos que cambiarlo a str 
            # Por lo que establecemos un delimitador que serian los espacios que hay dentro del set para al final 
            # poder unirlos y establecer nuestro 'desc' en str
            delimiter = ' '
            modified_data[idx]['desc'] = delimiter.join(crt['desc'])
        # Verificar y modificar los valores de 'author'
        if 'author' in crt:
            for key, value in crt['author'].items():
                modified_data[idx][f'author_{key}'] = value
        # Verificar y modificar los valores de 'music'
        if 'music' in crt:
            for key, value in crt['music'].items():
                modified_data[idx][f'music_{key}'] = value
        # Verificar y modificar los valores de 'authorStats'
        if 'authorStats' in crt:
            for key, value in crt['authorStats'].items():
                modified_data[idx][f'authorStats_{key}'] = value
        # Verificar y modificar los valores de 'stats'
        if 'stats' in crt:
            for key, value in crt['stats'].items():
                modified_data[idx][f'stats_{key}'] = value
        # Verificar y modificar los valores de 'statsV2'
        if 'statsV2' in crt:
            for key, value in crt['statsV2'].items():
                modified_data[idx][f'statsV2_{key}'] = value

    return(modified_data)