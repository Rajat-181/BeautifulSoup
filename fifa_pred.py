
import pandas as pd
import os.path

data = pd.read_csv("WorldCupMatches.csv")
data.head()
data.columns
data.describe()
data.columns = data.columns.str.replace(' ','_')

for match in range(len(data)):
    data.Datetime[match] = data.Datetime[match].split(' ')[1] + ' ' + data.Datetime[match].split(' ')[2] 
    
data.head()    
diff_ranking = []
Home_Team = []
Away_Team = []
Winner = []    
Difference_CurrentYearWtAvg = []
Difference_Past3YearsWtAvg = []
HomeTeam_RankChange = []
AwayTeam_RankChange = []
MatchMonth = []

files_read = 0

unread_files = []

for particular_match in range(len(data)):
    matchday = data.Datetime[particular_match]
    
    if matchday.split(' ')[0] == 'Jun':
        matchday = 'May' + ' ' + matchday.split(' ')[1]
    
    filename = os.path.isfile('FIFA_data/'+ matchday +'.csv') 
    if filename:
        files_read = files_read + 1
        matchdayrankings = pd.read_csv('FIFA_data/'+ matchday +'.csv')
        HomeTeam = data.Home_Team_Name[particular_match]
        AwayTeam = data.Away_Team_Name[particular_match]
        length1 = len(matchdayrankings[matchdayrankings.Name==HomeTeam].Ranks.values)
        length2 = len(matchdayrankings[matchdayrankings.Name==AwayTeam].Ranks.values)
        if length1 & length2:
            Homerank = matchdayrankings[matchdayrankings.Name==HomeTeam].Ranks.values[0]
            Awayrank = matchdayrankings[matchdayrankings.Name==AwayTeam].Ranks.values[0]
            Cummulative_3YearHome = matchdayrankings[matchdayrankings.Name==HomeTeam].Year1_WtAvg.values[0] + matchdayrankings[matchdayrankings.Name==HomeTeam].Year2_WtAvg.values[0] + matchdayrankings[matchdayrankings.Name==HomeTeam].Year3_WtAvg.values[0]
            Cummulative_3YearAway = matchdayrankings[matchdayrankings.Name==AwayTeam].Year1_WtAvg.values[0] + matchdayrankings[matchdayrankings.Name==AwayTeam].Year2_WtAvg.values[0] + matchdayrankings[matchdayrankings.Name==AwayTeam].Year3_WtAvg.values[0]
            diff_ranking.append(Homerank-Awayrank)
            Difference_CurrentYearWtAvg.append(matchdayrankings[matchdayrankings.Name==HomeTeam].CurrentYear_WtAvg.values[0] - matchdayrankings[matchdayrankings.Name==AwayTeam].CurrentYear_WtAvg.values[0])
            Difference_Past3YearsWtAvg.append(Cummulative_3YearHome-Cummulative_3YearAway)
            AwayTeam_RankChange.append(matchdayrankings[matchdayrankings.Name==AwayTeam].RankChange.values[0])
            HomeTeam_RankChange.append(matchdayrankings[matchdayrankings.Name==HomeTeam].RankChange.values[0])
            Home_Team.append(HomeTeam)
            Away_Team.append(AwayTeam)
            MatchMonth.append(matchday)
            
            
            Winner.append(data.winner[particular_match])
    else:
        unread_files.append(matchday)
        
final_trainingData = pd.DataFrame()
final_trainingData["HomeTeam"] = Home_Team
final_trainingData["AwayTeam"] = Away_Team
final_trainingData["MatchTime"] = MatchMonth
final_trainingData["Difference_Ranks"] = diff_ranking
final_trainingData["HomeTeamRankChange"] = HomeTeam_RankChange
final_trainingData["AwayTeamRankChange"] = AwayTeam_RankChange
final_trainingData["Difference_TotalPoints"] = Difference_CurrentYearWtAvg
final_trainingData["DifferencePoints_3Years"] = Difference_Past3YearsWtAvg
final_trainingData["Winner"] = Winner

final_trainingData.to_csv('final_data_modeling.csv')

Year	Host
2014	Brazil
2006	Germany
2002	South Korea & Japan
1998	France
1994	USA
1990	Italy
1986	Mexico
1982	Spain
1978	Argentina
1974	Germany


