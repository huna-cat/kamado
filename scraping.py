import pandas as pd
import urllib.request
import const
from bs4 import BeautifulSoup as bsoup


# 定数
# TODO Baseに変換
const.baseUrl = "http://www.nhk.or.jp/kamado/"
const.recipeUrl = const.baseUrl + "recipe.html" 
const.recipeTableColumns = ["OnAir", "url", "title"]

"""
    レシピを取得
"""
def getRecipeDF() :
    
    soup = getBeautifulSoup()

    ul = soup.find("ul", class_="recipeTable")

    # リストに整形する無名関数
    func = (
        lambda i, pTags :
        [pTags[0].string, pTags[1].a.get("href"), pTags[2].string]
    )

    # DataFrameにまとめる
    recipedf = ( pd.DataFrame(
        [ func(i, li.find_all("p")) for i, li in enumerate(ul.find_all("li"))], 
        columns=const.recipeTableColumns)
    )
    return recipedf

"""
    かまどのURLを受け取ってBeautifulSoupを返す
"""
def getBeautifulSoup() :
    # リクエストの設定
    req = urllib.request.Request(const.baseUrl)
    soup = None

    # リクエストを投げる
    with urllib.request.urlopen(req) as res :
        soup = bsoup(res.read(), "html.parser")
    
    return soup
