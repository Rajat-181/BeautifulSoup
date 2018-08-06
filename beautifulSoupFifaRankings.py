# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 03:00:19 2018

@author: rajat
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup

for pagenumber in range(23,270):
    url = "https://www.fifa.com/fifa-world-ranking/ranking-table/men/rank="+ str(pagenumber)+"/index.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all(class_="row row-first")[0]
    year = soup.find_all(class_="navbar navbar-pageheader navbar-rankingtbl nav-scrollspy")[0]
    year_container = year.select('.module')[0]
    date_ul = year_container.find('ul',class_='slider-list items-1')
    date_ranking = date_ul.text
    month_ranking = date_ranking.split(' ')[1][0:3]
    year_ranking = date_ranking.split(' ')[2]
    date_ranking = month_ranking + ' ' + year_ranking
    rank_data = pd.DataFrame()
    
    rankingtable = table.find_all(class_="table tbl-ranking table-striped")[0]
    tablebody = rankingtable.select('tbody')[0]
    anchor = tablebody.select('.anchor')
    Teams = []
    Ranks = []
    CountryCode = []
    Points = []
    PrevPoints = []
    RankChange = []
    CurrentYear_Avg = []
    CurrentYear_WtAvg = []
    Year1_Avg = []
    Year1_WtAvg = []
    Year2_Avg = []
    Year2_WtAvg = []
    Year3_Avg = []
    Year3_WtAvg = []
    
    for anch in anchor:
        Ranks.append(anch.select('.tbl-rank')[0].get_text())
        Teams.append(anch.select('.tbl-teamname')[0].get_text())
       # CountryCode.append(anch.select('.tbl-countrycode hidden')[0].get_text())
        Points.append(anch.select('.tbl-points')[0].get_text())
        PrevPoints.append(anch.select('.tbl-prevpoints')[0].get_text())
        RankChange.append(anch.select('.tbl-prevrank')[0].get_text())
        CurrentYear_Avg.append(anch.select('.tbl-points-avg')[0].get_text())
        CurrentYear_WtAvg.append(anch.select('.tbl-points-avg-weight')[0].get_text())
        Year1_Avg.append(anch.select('.tbl-points-avg')[1].get_text())
        Year1_WtAvg.append(anch.select('.tbl-points-avg-weight')[1].get_text())
        Year2_Avg.append(anch.select('.tbl-points-avg')[2].get_text())        
        Year2_WtAvg.append(anch.select('.tbl-points-avg-weight')[2].get_text())
        Year3_Avg.append(anch.select('.tbl-points-avg')[3].get_text())
        Year3_WtAvg.append(anch.select('.tbl-points-avg-weight')[3].get_text())
        
    rank_data["Name"] = Teams
    rank_data["Ranks"] = Ranks
    #rank_data["CountryCode"] = CountryCode
    rank_data["Points"] = Points
    rank_data["PrevPoints"] = PrevPoints
    rank_data["RankChange"] = RankChange
    rank_data["CurrentYear_Avg"] = CurrentYear_Avg
    rank_data["CurrentYear_WtAvg"] = CurrentYear_WtAvg
    rank_data["Year1_Avg"] = Year1_Avg
    rank_data["Year1_WtAvg"] = Year1_WtAvg
    rank_data["Year2_Avg"] = Year2_Avg
    rank_data["Year2_WtAvg"] = Year2_WtAvg
    rank_data["Year3_Avg"] = Year3_Avg
    rank_data["Year3_WtAvg"] = Year3_WtAvg
    
    rank_data.to_csv("fifa-world-cup/FIFA_data/"+date_ranking+".csv")
    