def format_batting_stats ( name: str ,at_bats: int , hits: int, home_runs: int ) -> str:
    batting_average = 0.0

    # 在這裡計算打擊率
    batting_average = hits / at_bats

    # 在這裡格式化字串
    formatted_string = f"{name} 的打擊數據：\n"
    formatted_string += f"打數: {at_bats}\n"
    formatted_string += f"安打: {hits}\n"
    formatted_string += f"全壘打: {home_runs}\n"
    formatted_string += f"打擊率: {batting_average:.3f}\n"

    return formatted_string

# 測試你的函式
stats = format_batting_stats ( "陳金鋒" ,450 ,150 ,30 )
print ( stats )

# 預期輸出 (打擊率可能因計算精度略有不同):
# 陳金鋒 的打擊數據：
# 打數: 450
# 安打: 150
# 全壘打: 30
# 打擊率: 0.333
