import time
import os
import pandas as pd






class Analytic():

    def __init__(self, frame, level):
        self.frame=frame
        self.level=level
        self.file_name_routes = 'routes.txt'
        self.result = 'result.txt'
        self.path_result = os.path.abspath(self.result)
        self.path_routes = os.path.abspath(self.file_name_routes)



    def timedelta(self, time1,time2, frame1, frame2):
        delta=time2-time1
        if delta.seconds < 2:
            with open(self.result, 'a') as out:
                out.write(str(frame1) + '\n')
                out.write("============================================================================" + '\n')
                out.write(str(frame2) + '\n')
                


    def prohibit_route(self, frame):

        df=pd.read_csv(self.path_routes, sep='}',
        encoding='utf-8',
        names=["routes"], 
        usecols=["routes"], 
        engine='python'
        
        )
        
        length_df=len(df.index)
        cnt=0
        
        while length_df-1>=cnt:
            str_route=df.iat[cnt,0]
            mask=frame['api_route']
            mask_frame=frame.loc[mask==str_route[1:len(str_route)]]
            with open(self.result, 'a') as out:
                out.write("=======================================prohibited routes================================="+ '\n')
                out.write(str(mask_frame))
                out.write("===================================================================================="+ '\n')
                
            cnt=cnt+1
        


    def check_ip(self, frame):
        len_before=len(frame.index)
        tmp_ip=frame.iat[0,2]
        frame_ip=frame['ip_address']

        mask_frame_ip=frame.loc[frame_ip==tmp_ip]

        len_after=len(mask_frame_ip.index)

        if len_after==len_before:
            return True
        else:
            return  False


    def find_pair_ip(self, frame):

        frame_length=len(frame.index)
        cnt=0

        while frame_length-1>cnt:

            if frame.iat[cnt,2]==frame.iat[cnt+1,2]:
                cnt=cnt+1
            else:
                self.timedelta(frame.iat[cnt,0],frame.iat[cnt+1,0], frame.iloc[cnt,:], frame.iloc[cnt+1,:])
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



