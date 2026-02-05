import pandas as pd
import pathlib

# dynamically define dir path
PATH = pathlib.Path(__file__).parent.parent.joinpath("data")
MARKETING_CAMPAIGN_DATASET_PATH = PATH.joinpath('marketing_campaign_data.xlsx')

def get_f_campaign_performance():
    """
    Loads campaign performance table
    """
    try:
        df = pd.read_excel(
            MARKETING_CAMPAIGN_DATASET_PATH,
            sheet_name='CampaignPerformance'
        )
        return df
    
    except Exception as e:
        print(f"Error:{e}")


def get_d_campaign():
    """
    Loads dimensional data for campaigns
    """
    try:
        df = pd.read_excel(
            MARKETING_CAMPAIGN_DATASET_PATH,
            sheet_name='CampaignMeta'
        )
        
        return df
    
    except Exception as e:
        print(f"Error:{e}")

def get_f_channel_kpis():
    """
    Loads channel's kpis data
    """
    try:
        df = pd.read_excel(
            MARKETING_CAMPAIGN_DATASET_PATH,
            sheet_name='ChannelRates'
        )
        return df
    
    except Exception as e:
        print(f"Error:{e}")
