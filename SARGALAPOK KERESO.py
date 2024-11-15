@app.route('/search_player', methods=['POST'])
def search_player():
    query = request.json.get('query', '').lower().strip()
    if not query:
        return jsonify([])  # Ha üres keresési kifejezés, akkor üres listát adunk vissza
    
    players = get_players()
    results = [p['name'] for p in players if query in p['name'].lower()]
    return jsonify(results)

def get_players():
    workbook = openpyxl.load_workbook(EXCEL_FILE_PATH)
    sheet = workbook['Sarga-piros lapok']
    players = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        name, team = row[0], row[1]
        if name:
            players.append({"name": name, "team": team})

    return players