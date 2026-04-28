import requests
import json

# Your API Key
TBA_KEY = 'LAGBCnx05Jzue5pPdvMHXw0wpgIUDUtMUnmbQT3okrTi0vmNWhTjVcjrR1GgVc6w'
YEAR = 2026

def get_2026_teams():
    all_teams = []
    page = 0
    
    print(f"Fetching registered teams for {YEAR}...")
    
    while True:
        # TBA returns teams in pages of 500
        url = f"https://www.thebluealliance.com/api/v3/teams/{YEAR}/{page}/keys"
        headers = {'X-TBA-Auth-Key': TBA_KEY}
        
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break
            
        data = response.json()
        
        # If the page is empty, we've reached the end
        if not data:
            break
            
        # Clean 'frc123' -> 123
        cleaned_page = [int(team.replace('frc', '')) for team in data]
        all_teams.extend(cleaned_page)
        
        print(f"Page {page} loaded ({len(data)} teams found)")
        page += 1

    # Sort them numerically for a cleaner list
    all_teams.sort()
    
    # Save to a file for your extension
    with open(f'teams_{YEAR}.json', 'w') as f:
        json.dump(all_teams, f)
        
    print(f"\nSuccess! Total teams registered for {YEAR}: {len(all_teams)}")
    print(f"File saved as: teams_{YEAR}.json")
    
    # Return as a snippet you can copy/paste
    return all_teams

if __name__ == "__main__":
    team_list = get_2026_teams()
    # Print the first 20 for verification
    print("Snippet:", team_list[:20], "...")