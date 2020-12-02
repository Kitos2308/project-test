



class Analytic():
    def __init__(self, frame, level):
        self.frame=frame
        self.level=level

    @classmethod
    def timedelta(cls, frame1,frame2):
        print("===============================================================================")

    @classmethod
    def check_ip(cls, frame):
        len_before=len(frame.index)
        tmp_ip=frame.iat[0,2]
        frame_ip=frame['ip_address']

        mask_frame_ip=frame.loc[frame_ip==tmp_ip]

        len_after=len(mask_frame_ip.index)

        if len_after==len_before:
            return True
        else:
            return  False

    @classmethod
    def find_pair_ip(cls, frame):

        frame_length=len(frame.index)
        cnt=0

        while frame_length-1>cnt:

            if frame.iat[cnt,2]==frame.iat[cnt+1,2]:
                cnt=cnt+1
            else:
                cls.timedelta(frame.iat[cnt,0],frame.iat[cnt+1,0])
                cnt=cnt+1










    def find_ip(self,frame,level):


        mask_level=frame["level"]  # sort by method

        mask_level_=frame.loc[mask_level==level] #assign all stream with LEVEL from function as parameter

        mask_sid=mask_level_["sid"]   #mask for sid

        mask_drop_sid=mask_sid.drop_duplicates(keep='first', inplace=False)

        for sid in mask_drop_sid:               # use all
            if sid=="None":
                pass
            else:
                frame_sid = mask_level_.loc[mask_sid == sid]    # taking sid from frame
                if self.check_ip(frame_sid):
                    pass
                else:
                    self.find_pair_ip(frame_sid)# computing time between two ip address







        # mask_sid_=mask_level_.loc[mask_sid==mask_level_.iat[0,3]]

        # print(mask_sid_)
        #
        # if self.check_ip(mask_sid_):
        #     print("only one ip in session")
        # else:
        #     print(mask_sid_,"ip more than one in session")












