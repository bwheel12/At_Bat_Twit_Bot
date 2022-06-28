library(baseballr)
today_batters = scrape_statcast_savant(start_date = Sys.Date() - 1,end_date = Sys.Date(),player_type = "batter")
write.csv(today_batters,file="./Todays_statcast.csv")