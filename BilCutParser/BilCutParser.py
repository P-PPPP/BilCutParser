# -*- coding: utf-8 -*-
r"""
    BCUT Sub Parser
    .xml file can be found at C:\Users\xxx\Documents\MYVideoProject\xxx\project.xml
        @Author: PPPPP
        @Time: 2021-12-09
"""

import xml.dom.minidom
from datetime import datetime
from datetime import timedelta
class BCUTParser:
    def __init__(self,path:str)->None:
        self.path = path

    def loadXml(self,path:str)->None:
        """
        Get A Xml Object From Path
        """
        return xml.dom.minidom.parse(path)
    
    def ParseToList(self)->list:
        """
        Parse A Xml Object To Srt String
        """
        xml_obj = self.loadXml(self.path)
        Root_Dom = xml_obj.documentElement
        # Make a root Dom Tree
        AllCaptions = Root_Dom.getElementsByTagName("caption")
        # Get All Caption And Return A List
        srt_str = []
        for node in AllCaptions:
            Text,Start_Time,Durtion = node.getAttribute("text"),node.getAttribute("inPoint"),node.getAttribute("duration")
            srt_str.append([Text,Start_Time,Durtion])
        return srt_str

    def ListToSrt(self,SrtList:list)->str:
        """
        Parse A List To Str
        """
        def us_to_string(microseconds:int)->str:
            # Convert Microseconds To String
            return (datetime(1, 1, 1) + timedelta(microseconds=microseconds)).strftime('%H:%M:%S') + ',' + str((microseconds % 10**6) // 10**3).zfill(3)

        def to_time_str(Start_Time:int,Durtion:int)->str:
            # Convert Start_Time And Durtion To String
            End_Time = Start_Time + Durtion
            Start_Time = us_to_string(Start_Time)
            End_Time = us_to_string(End_Time)
            return Start_Time + ' --> ' + End_Time

        srt = ""
        for number,node in enumerate(SrtList):
            srt += str(number+1) + "\n"
            srt += to_time_str(int(node[1]),int(node[2])) + "\n"
            srt += node[0] + "\n\n"
        return srt

def ParseList(path:str)->list:
    """
    Parse A Xml File To List
    """
    BCut = BCUTParser(path)
    return BCut.ParseToList()

def ParseSrt(path:str)->str:
    """
    Parse A Xml File To String
    """
    BCut = BCUTParser(path)
    return BCut.ListToSrt(BCut.ParseToList())

def Save_Srt(inputPath:str,OutputPath:str)->None:
    """
    Save A String To A File
    """
    srt = ParseSrt(inputPath)
    with open(OutputPath,"w",encoding='utf-8') as f:
        f.write(srt)