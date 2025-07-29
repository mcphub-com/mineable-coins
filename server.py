import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/minerstat/api/mineable-coins'

mcp = FastMCP('mineable-coins')

@mcp.tool()
def get_coins_data() -> dict: 
    '''With this endpoint you can get a collection of all coins. **API alterations** - **Get one coin:** https://api.minerstat.com/v2/coins?list=BTC - **Get list of coins:** https://api.minerstat.com/v2/coins?list=BTC,BCH,BSV - **Get all coins from one algorithm:** https://api.minerstat.com/v2/coins?algo=SHA-256 - **Get all coins from multiple algorithms:** https://api.minerstat.com/v2/coins?algo=SHA-256,Scrypt,Ethash'''
    url = 'https://mineable-coins.p.rapidapi.com/coins'
    headers = {'x-rapidapi-host': 'mineable-coins.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
