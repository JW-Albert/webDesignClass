class BaseballPlayer() :
    def __init__ ( self ,name: str ,number: int ,position: str ,batting_average: float = 0.0 ,home_runs: int = 0 ,hits: int = 0 ,at_bats: int = 0 ) -> None :
        self.name = name
        self.number = number
        self.position = position
        self.batting_average = batting_average
        self.home_runs = home_runs
        self.hits = hits
        self.at_bats = at_bats

    def display_info ( self ) -> None :
        print ( f"球員姓名: {self.name}" )
        print ( f"球員號碼: {self.number}" )
        print ( f"球員位置: {self.position}" )
        print ( f"打擊率: {self.batting_average:.3f}" )
        print ( f"全壘打數: {self.home_runs}" )

    def increase_batting_record ( self ,hits: int ,at_bats: int ) -> None:
        self.hits += hits
        self.at_bats += at_bats

        self.batting_average = self.hits / self.at_bats

    def hit_home_run ( self ) -> None:
        self.home_runs += 1

    def __str__ ( self ) -> str:
        return (f"球員姓名: {self.name:^20s}"
                f" 球員號碼: {self.number:^3d}"
                f" 球員位置: {self.position:^6s}"
                f" 打擊率: {self.batting_average:^.3f}"
                f" 全壘打數: {self.home_runs:^3d}"
                f" 安打數: {self.hits:^3d}"
                f" 打數: {self.at_bats:^3d}")
    

class Team:
    def __init__ ( self ,name: str ) -> None:
        self.name = name
        self.players = []

    def add_player ( self ,player: BaseballPlayer ) -> None:
        self.players.append ( player )

    def display_all_players ( self ) -> None:
        print ( f"球隊名稱: {self.name}" )
        for player in self.players :
            print ( player )

    def calculate_team_batting_average ( self ) -> float:
        total_hits = sum( player.hits for player in self.players )
        total_at_bats = sum( player.at_bats for player in self.players )

        if total_at_bats == 0:
            return 0.0

        return total_hits / total_at_bats

def main () -> int:
    player1 = BaseballPlayer("CHANG Cheng-Yu", 9, "IF")
    player2 = BaseballPlayer("CHEN Chieh-Hsien", 24, "OF")
    player3 = BaseballPlayer("CHIANG Kun-Yu", 90, "IF")

    # 建立球隊
    team = Team("TPE")

    # 加入球員
    team.add_player(player1)
    team.add_player(player2)
    team.add_player(player3)

    # 顯示其中一位球員初始資料
    print("\n--- 初始資訊 ---")
    player1.display_info()

    # 第一次打擊：2 安打，3 打數
    print("\n--- 第一次打擊紀錄更新 ---")
    player1.increase_batting_record(2, 3)
    player1.display_info()

    # 第二次打擊：1 安打，4 打數
    print("\n--- 第二次打擊紀錄更新 ---")
    player1.increase_batting_record(1, 4)
    player1.display_info()

    # 擊出一支全壘打
    print("\n--- 擊出全壘打 ---")
    player1.hit_home_run()
    player1.display_info()

    # 顯示全隊球員資訊
    print("\n--- 全隊球員資訊 ---")
    team.display_all_players()

    # 計算並顯示全隊平均打擊率
    print("\n--- 球隊平均打擊率 ---")
    print(f"球隊平均打擊率: {team.calculate_team_batting_average():.3f}")

    return 0

if ( __name__ == "__main__" ) :
    main()