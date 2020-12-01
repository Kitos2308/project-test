


def find_ip(frame,level):
    mask_level=frame["level"]
    mask_level_=frame.loc[mask_level==level]

    mask_sid=mask_level_["sid"]

    mask_sid_=mask_level_.loc[mask_sid==mask_level_.iat[0,3]]

    print(mask_sid_)




