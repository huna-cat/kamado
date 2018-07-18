import pandas as pd
import urllib.request
import const
from bs4 import BeautifulSoup as bsoup


# 定数
# TODO Baseに変換
const.url = "http://www.nhk.or.jp/kamado/recipe.html"
const.recipeTableColumns = ["OnAir", "url", "title"]

"""
    全てのレシピを返す
"""
def getAllRecipeTable() :
    soup = getBeautifulSoup()
    pastRecipeTable = getPastRecipeTable(soup)
    # newRecipeTable = getNewRecipe(soup)
        
    return

"""
    過去のレシピを取得
"""
def getPastRecipeTable(soup = None) :
    
    recipeTable = pd.DataFrame(columns=const.recipeTableColumns)

    # 引数がない場合はsoupを取得
    if soup is None :
        soup = getBeautifulSoup()

    ul = soup.find("ul", class_="recipeTable")

    # リストに整形する無名関数
    func = (
        lambda i, pTags :
        [pTags[0].string, pTags[1].a.get("href"), pTags[2].string]
    )

    # DataFrameにまとめる
    recipeTable = ( pd.DataFrame(
        [ func(i, li.find_all("p")) for i, li in enumerate(ul.find_all("li"))], 
        columns=const.recipeTableColumns)
    )
    return recipeTable


"""
    直近のレシピを取得
"""
def getNewRecipe(soup = None) :
    if soup is None :
        soup = getBeautifulSoup()
    return 

"""
    かまどのURLを受け取ってBeautifulSoupを返す
"""
def getBeautifulSoup() :
    # リクエストの設定
    req = urllib.request.Request(const.url)
    soup = None

    # リクエストを投げる
    with urllib.request.urlopen(req) as res :
        soup = bsoup(res.read(), "html.parser")
    
    return soup
