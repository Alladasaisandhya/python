Q1="select avg(age) from player;"

Q2="select match_no,play_date from match where audience > 50000 order by match_no asc;"

#Q3="select team.team_id,count(team_id) from team inner join matchteamdetails where win_lose='W' group by team.team_id order by team.team_id asc, match_no desc;"

Q4="select match_no,play_date from match where stop1_sec >(select avg(stop1_sec) from match) order by match_no desc;"

Q6="select match.match_no,player.name,player.jersey_no from player inner join match on player.player_id=match.player_of_match order by match.match_no asc;"

Q7="select team.name, avg(age) from player inner join team on player.team_id=team.team_id group by team.name having avg(age)>26 order by team.name ASc; "
