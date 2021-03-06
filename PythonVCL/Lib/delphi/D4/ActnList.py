###
#  This file was generated by VCL Generator
#  Copyright 1998 - Morgan Martinet
#  06/07/1999 07:59:02
#  it declares the symbols of the Delphi unit ActnList.pas
###

from System import *
from Classes import *
from ImgList import *
import _ActnList

####################################################
class TContainedAction( TBasicAction ):
    def Create( Self, AOwner ):
        return _ActnList.CreateContainedAction( Self, AOwner )

    def __getattr__( Self, Key ):
        return _ActnList.ContainedAction_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _ActnList.ContainedAction_SetAttr( Self, Key, Value )

####################################################
class TCustomActionList( TComponent ):
    def Create( Self, AOwner ):
        return _ActnList.CreateCustomActionList( Self, AOwner )

    def __getattr__( Self, Key ):
        return _ActnList.CustomActionList_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _ActnList.CustomActionList_SetAttr( Self, Key, Value )

####################################################
class TActionList( TCustomActionList ):
    def Create( Self, AOwner ):
        return _ActnList.CreateActionList( Self, AOwner )

    def __getattr__( Self, Key ):
        return _ActnList.ActionList_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _ActnList.ActionList_SetAttr( Self, Key, Value )

####################################################
class TCustomAction( TContainedAction ):
    def Create( Self, AOwner ):
        return _ActnList.CreateCustomAction( Self, AOwner )

    def __getattr__( Self, Key ):
        return _ActnList.CustomAction_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _ActnList.CustomAction_SetAttr( Self, Key, Value )

####################################################
class TAction( TCustomAction ):
    def Create( Self, AOwner ):
        return _ActnList.CreateAction( Self, AOwner )

    def __getattr__( Self, Key ):
        return _ActnList.Action_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _ActnList.Action_SetAttr( Self, Key, Value )

####################################################
class TActionLink( TBasicActionLink ):
    def Create( Self, AClient ):
        return _ActnList.CreateActionLink( Self, AClient )

    def __getattr__( Self, Key ):
        return _ActnList.ActionLink_GetAttr( Self, Key )

    def __setattr__( Self, Key, Value ):
        return _ActnList.ActionLink_SetAttr( Self, Key, Value )

