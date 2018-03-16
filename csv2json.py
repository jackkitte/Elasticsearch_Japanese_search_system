# -*- coding: utf-8 -*-

import pandas as pd
import json

def extract_csv_column_data(filepath):

    print("CSVファイルからのデータ抽出開始")

    df = pd.read_csv(filepath)
    df = df.fillna("なし")

    index_count = 0
    index_json = {}
    json_data = {}

    for key, column in df.iterrows():
        #index_json.update({"index": {"_index": "opc_known_db", "_type": "_doc", "_id": index_count}})
        #index_json.update({"index": {"_index": "opc_case_db", "_type": "_doc", "_id": index_count}})
        index_json.update({"index": {"_index": "opc_troubleshooting_db", "_type": "_doc", "_id": index_count}})
        #json_data.update({"db_id": column.get("既知化DB番号", "なし"), "db_name": column.get("既知化DB名", "なし"), "case_id": column.get("案件ID", "なし"), "case_name": column.get("案件名", "なし"), "solution": column.get("対応方法", "なし")})
        #json_data.update({"case_id": column.get("案件ID", "なし"), "case_name": column.get("案件名", "なし"), "notice": column.get("注意事項", "なし"), "summary": column.get("案件概要", "なし")})
        json_data.update({"issue_name": column.get("故障名", "なし"), "case_id": column.get("案件ID", "なし"), "case_name": column.get("案件名", "なし"), "receiving_contents": column.get("受付内容", "なし"), "break_down_issue": column.get("切り分け内容", "なし"), "restoration_contents": column.get("復旧内容", "なし"), "cause": column.get("原因", "なし"), "time_series": column.get("時系列", "なし")})

        with open("OPC_troubleshooting_db.json", "a") as f:
            f.write(json.dumps(index_json, ensure_ascii = False, sort_keys = True))
            f.write("\n")
            f.write(json.dumps(json_data, ensure_ascii = False, sort_keys = True))
            f.write("\n")

        index_count += 1

if __name__ == "__main__":

    print("start")

    extract_csv_column_data("~/AI/OPC/Data/故障対応リスト.csv")

    print("end")
