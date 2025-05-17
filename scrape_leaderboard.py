import pandas as pd

url = "https://github.com/vectara/hallucination-leaderboard"
output_filename = "leaderboard_data.csv"

try:
    # Read all tables from the page
    tables = pd.read_html(url)

    # Assuming the leaderboard is the third table (index 2)
    leaderboard = tables[2]

    # Save the leaderboard to CSV
    leaderboard.to_csv(output_filename, index=False, encoding='utf-8')
    print(f"Leaderboard data successfully saved to {output_filename}")

except Exception as e:
    print(f"An error occurred: {e}")
