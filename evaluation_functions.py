import numpy as np
def rmse_funct(predict_data,truth_data,*regions):
    """
    Calculate the rmse of prediction.
    Parameters:
        args: LeftBottom_idx, RightTop_idx.
    Returns:
    float: The RMSE.
    """
    regions=np.array(regions)
    LB=np.array(regions[0,:])
    RT=np.array(regions[1,:])
    rmse_data = np.sqrt(((predict_data[LB[0]:RT[0],LB[1]:RT[1]]-truth_data[LB[0]:RT[0],LB[1]:RT[1]])**2).mean())
    return rmse_data
def spatial_acc(predict_data,truth_data,*time_regions):
    from scipy.stats import spearmanr
    """
    Calculate the rmse of prediction.
    Parameters:
        args: time_span, LeftBottom_idx, RightTop_idx.
    Returns:
    float: The RMSE.
    """
    time_regions=np.array(time_regions)
    time = np.array(regions[0,:])
    LB   = np.array(regions[1,:])
    RT   = np.array(regions[2,:])

    predict_1d=b = np.ravel(predict_data[time[0]:time[1],LB[0]:RT[0],LB[1]:RT[1]])
    truth_1d     = np.ravel(truth_data[time[0]:time[1],LB[0]:RT[0],LB[1]:RT[1]])
    acc_data, p_value = spearmanr(predict_1d,truth_1d)
    return acc_data,p_value

def acc(predict_data,truth_data,*time_regions):
    from scipy.stats import pearsonr
    """
    Calculate the rmse of prediction.
    Parameters:
        args: time_span, LeftBottom_idx, RightTop_idx.
    Returns:
    float: The RMSE.
    """
    time_regions=np.array(time_regions)
    time = np.array(regions[0,:])
    LB   = np.array(regions[1,:])
    RT   = np.array(regions[2,:])
    acc_data, p_value = spearmanr(predict_data[time[0]:time[1],LB[0]:RT[0],LB[1]:RT[1]],truth_data[time[0]:time[1],LB[0]:RT[0],LB[1]:RT[1]])
    return acc_data,p_value
