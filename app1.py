from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt

#app = Flask(__name__)

# Load the simulated data from the CSV file
data = pd.read_csv('./simulated_data.csv')

# Define the available columns for user selection
available_columns = {
    'totalVotes': 'Total Votes',
    'op_token': 'OP Token',
    'op_tokens_voting': 'OP Tokens for Voting',
    'followCount': 'Follow Count',
    'totalProposalInteraction': 'Total Proposal Interaction',
    'totalNft': 'Total NFT'
}

# Governance Model
#@app.route('/governance', methods=['GET', 'POST'])
#def governance():
    if request.method == 'POST':
        selected_column = request.form.get('column')
        selected_value = float(request.form.get('value'))

        filtered_data = data[data[selected_column] >= selected_value]

        # Perform analysis and create visualizations based on the filtered data
        # ...

        # Render the template with the generated visualizations
        return render_template('governance.html', column=selected_column, value=selected_value)

    return render_template('governance.html', columns=available_columns)

# Reputation Model
#@app.route('/reputation', methods=['GET', 'POST'])
def reputation():
    if request.method == 'POST':
        selected_column = request.form.get('column')
        selected_value = float(request.form.get('value'))

        filtered_data = data[data[selected_column] >= selected_value]

        # Perform analysis and create visualizations based on the filtered data
        # ...

        # Render the template with the generated visualizations
        return render_template('reputation.html', column=selected_column, value=selected_value)

    return render_template('reputation.html', columns=available_columns)

# Token Voting Model
#@app.route('/token_voting', methods=['GET', 'POST'])
def token_voting():
    if request.method == 'POST':
        selected_column = request.form.get('column')
        selected_value = float(request.form.get('value'))

        filtered_data = data[data[selected_column] >= selected_value]

        # Perform analysis and create visualizations based on the filtered data
        # ...

        # Render the template with the generated visualizations
        return render_template('token_voting.html', column=selected_column, value=selected_value)

    return render_template('token_voting.html', columns=available_columns)

# NFT Interaction Model
#@app.route('/nft_interaction', methods=['GET', 'POST'])
def nft_interaction():
    if request.method == 'POST':
        selected_column = request.form.get('column')
        selected_value = float(request.form.get('value'))

        filtered_data = data[data[selected_column] >= selected_value]

        # Perform analysis and create visualizations based on the filtered data
        # ...

        # Render the template with the generated visualizations
        return render_template('nft_interaction.html', column=selected_column, value=selected_value)

    return render_template('nft_interaction.html', columns=available_columns)

# Social Media Model
#@app.route('/social_media', methods=['GET', 'POST'])
def social_media():
    if request.method == 'POST':
        selected_column = request.form.get('column')
        selected_value = float(request.form.get('value'))

        filtered_data = data[data[selected_column] >= selected_value]

        # Perform analysis and create visualizations based on the filtered data
        # ...

        # Render the template with the generated visualizations
        return render_template('social_media.html', column=selected_column, value=selected_value)

    return render_template('social_media.html', columns=available_columns)

#if __name__ == '__main__':
#    app.run(debug=True)
