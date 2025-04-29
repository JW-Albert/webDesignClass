def determine_pitcher_result ( innings_pitched: float ,earned_runs: int ,total_runs: int ,is_winning_team: bool ) -> str:
    result = ""

    if ( innings_pitched >= 5.0 and is_winning_team ):
        result = "勝投"
    elif ( innings_pitched >= 5.0 and not is_winning_team ):
        result = "敗投"
    elif (innings_pitched < 5.0):
        result = "中繼"
    else :
        result = ""

    return result

def main () -> int:
    print(determine_pitcher_result(6.0 ,2 ,5 ,True))   # 預期輸出: 勝投
    print(determine_pitcher_result(7.0 ,1 ,3 ,False))  # 預期輸出: 敗投
    print(determine_pitcher_result(4.2 ,0 ,2 ,True))   # 預期輸出: 中繼
    print(determine_pitcher_result(3.0 ,3 ,1 ,False))  # 預期輸出: 中繼

    return 0

if ( __name__ == "__main__" ) :
    main()