from nba_api.stats.endpoints import commonteamroster, commonplayerinfo
from nba_api.stats.static import players

# Constants
MAVS_ID = "1610612742"


def get_mavs_roster():
    """
    Retrieves the names of the Mavericks roster as a list rather than a pandas dataframe

    Args:
        N/A

    Returns:
        list[str]: List of names of all Mavericks players
    """

    roster = commonteamroster.CommonTeamRoster(team_id=MAVS_ID).get_data_frames()[0]

    return roster["PLAYER"]


def get_player_info(name: str):
    """
    Retrieves the information of a player given their name

    Args:
        name (str): Name of the player

    Returns:
        dataframe: Data of the given player
    """

    player_id = _get_player_id(name)

    if player_id is None:
        return None

    return commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_data_frames()[0]
    

def _get_player_id(name: str):
    """ 
    Retrieves the NBA id of a player given their name

    Args:
        name (str): Name of the player

    Returns:
        id (int): The NBA player id
    """

    player_data = players.find_players_by_full_name(name)

    if len(player_data) > 0:
        return player_data[0]["id"]
    
    return None
