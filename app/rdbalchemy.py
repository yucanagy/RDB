from suds.client import Client
from flask import flash, get_flashed_messages
import warnings

class RDBAlchemy(object):
    def __init__(self, IP = None):
        self.rdbState = False
        self.rdbIP = IP
        try:
            self.rdb = Client('%s%s%s' % ('http://' , IP ,':9001/docs'))
            self.ArrayOfCls_point = self.rdb.factory.create('ns0:ArrayOfCls_point')
            self.ArrayOfCls_point_main = self.rdb.factory.create('ns0:ArrayOfCls_point_main')
            self.ArrayOfCls_point_main_py = self.rdb.factory.create('ns0:ArrayOfCls_point_main_py')
            self.ArrayOfKeyValueOfanyTypeanyType = self.rdb.factory.create('ns2:ArrayOfKeyValueOfanyTypeanyType')
            self.ArrayOfTableAttributes = self.rdb.factory.create('ns0:ArrayOfTableAttributes')
            self.ArrayOfanyType = self.rdb.factory.create('ns2:ArrayOfanyType')
            self.ArrayOfint = self.rdb.factory.create('ns2:ArrayOfint')
            self.ArrayOfstring = self.rdb.factory.create('ns2:ArrayOfstring')
            self.Cls_point = self.rdb.factory.create('ns0:Cls_point')
            self.Cls_point_main = self.rdb.factory.create('ns0:Cls_point_main')
            self.Cls_point_main_py = self.rdb.factory.create('ns0:Cls_point_main_py')
            self.TableAttributes = self.rdb.factory.create('ns0:TableAttributes')
            self.char = self.rdb.factory.create('ns1:char')
            self.duration = self.rdb.factory.create('ns1:duration')
            self.guid = self.rdb.factory.create('ns1:guid')
            self.anyType = self.rdb.factory.create('ns1:anyType')
            self.rdbState = True
        except BaseException as err:
            self.rdbState = False
            return
        # finally:
        #     flash(self.rdbState, 'RDB')

    # def init_app(self, app):
    #     if (
    #         '123' not in app.config
    #     ):
    #         warnings.warn(
    #             '123 is not set. '
    #             'Defaulting 123 to "http://127.0.0.1:9001/docs".'
    #         )
    #     app.config.setdefault('123', 'http://127.0.0.1:9001/docs')
        
        #判断表是否存
    def ContainsPointID(self, id):
        result = self.rdb.service.ContainsPointID(id)
        return result

        #判断表是否存
    def ContainsTableID(self, id):
        result = self.rdb.service.ContainsTableID(id)
        return result

        #获取报警属性为true的点
    def GetAlarmPoints(self, point):
        points = self.ArrayOfCls_point
        points.point = self.ArrayOfCls_point
        result = self.rdb.service.GetAlarmPoints(points)
        return result

        #获取父节点
    def GetFatherAttrByID(self, id, fatherAtt):
        fatherAtt = self.TableAttributes
        result = self.rdb.service.GetFatherAttibuff(id,fatherAtt)
        return result
    
        #获取一个点的值
    def GetValue_byID(self, id):
        value = self.anyType
        result = self.rdb.service.GetValue_byID(id,value)
        return result

        #获取一些点的值
    def GetValues_byID(self, idss):
        ids = self.ArrayOfint
        ids.int = idss
        values = self.ArrayOfanyType
        result = self.rdb.service.GetValues_byID(ids,values)
        return result
    
        #获取一些点
    def GetPointsMain_byID_Hash(self, idss):
        ids = self.ArrayOfint
        ids.int = idss
        pointsMain = self.ArrayOfCls_point_main
        result = self.rdb.service.GetPointsMain_byID_hash(ids,pointsMain)
        return result


    def GetPoints_From_table_hash(self, tablename):
        points = self.ArrayOfCls_point
        result = self.rdb.service.GetPoints_From_table_hash(tablename, points)
        return result


        #获取服务器时间
    def GetSerTime(self, time):
        result = self.rdb.service.GetSerTime()
        return result

        #获取rdb信息
    def GetServerInfo(self):
        name=''
        serverIP=''
        result = self.rdb.service.GetServerInfo(name,serverIP)
        return result
    
        #获取表属性
    def GetTableAttributes(self, tableName):
        attributes = self.TableAttributes
        attributes.name = 0
        attributes.protocol = 0
        attributes.address = 0
        attributes.port = 0
        attributes.id = 0
        attributes.createtime = 0
        result = self.rdb.service.GetTableAttributes(tableName,attributes)
        return result

        #获取数据库中所有表属性
    def GetTableAttributes_hash(self):
        attributes = self.TableAttributes
        attributes.name = 0
        attributes.protocol = 0
        attributes.address = 0
        attributes.port = 0
        attributes.id = 0
        attributes.createtime = 0
        attributess = self.ArrayOfTableAttributes
        attributess.TableAttributes = attributes
        result = self.rdb.service.GetTableAttributes_hash(attributess)
        return result
        

        #获取某张表的点名
    def GetTablePointsName(self,tableName):
        pointsName = self.ArrayOfstring
        result = self.rdb.service.GetTablePointsName(tableName,pointsName)
        return result
        
        #获取所有表名
    def GetTablesName(self):
        names = self.ArrayOfstring
        result = self.rdb.service.GetTablesName(names)  
        return result

        #获取所有表名
    def GetTablesName_Hash(self):
        names = self.ArrayOfstring
        result = self.rdb.service.GetTablesName_Hash(names)
        return result

        #获取类型名称
    def GetTypeNames(self):
        names = self.ArrayOfstring
        result = self.rdb.service.GetTypeNames(names)
        return result

        #获取写队列第一个值
    def GetWriteQueueFirstPoint(self):
        point = self.Cls_point
        result = self.rdb.service.GetWriteQueueFirstPoint(point)
        return result

        #获取写队列的值
    def GetWriteQueuePoints(self):
        points = self.ArrayOfCls_point
        result = self.rdb.service.GetWriteQueuePoints(points)
        return result

        #更新一个点(修改一个点) point需要填充
    def UpdatePoint(self, id, point):
        point = self.Cls_point
        result = self.rdb.service.UpdatePoint(id,point)
        return result

        #更新一张表 属性tableAtt需要填充
    def UpdateTableAtt(self, id, tableAtt):
        tableAtt = self.TableAttributes
        result = self.rdb.service.UpdateTableAtt(id,tableAtt)
        return result

        #增加一个点
    def AddPoint(self, tableName, point):
        point = self.Cls_point
        result = self.rdb.service.AddPoint(tableName,point)
        return result

        #增加一些点
    def AddPoints(self, tableName, point):
        points = self.ArrayOfCls_point
        points.Cls_point = point
        result = self.rdb.service.AddPoint(tableName,points)
        return result

        #删除一个点
    def DeletePoint(self, id):
        result = self.rdb.service.DeletePoint(id)
        return result

        #删除一些点
    def DeletePoints(self, idss):
        ids =  self.ArrayOfint
        ids.int =idss
        result = self.rdb.service.DeletePoints(ids)
        return result

        #创建表ID
    def CreateTableID(self):
        result = self.rdb.service.CreateTableID()
        return result

        #增加一张表
    def AddTable(self, tableName,protocal,port,address,id):
        result = self.rdb.service.AddTable(tableName,protocal,port,address,id)
        return result

        #删除一张表 
    def DeleteTable(self, tableName):
        result = self.rdb.service.DeleteTable(tableName)
        return result

        #写到rdb内存一些值 pointMain 需要填充
    def SetPointsMain_byID_hash(self, pointssMain):
        pointsMain = self.ArrayOfCls_point_main
        pointsMain.pointMain=pointssMain
        result = self.rdb.service.SetPointsMain_byID_hash(pointsMain)
        return result

        #写到设备一个值 point需要填充
    def SetWriteQueueLastPoint(self, point):
        point = self.Cls_point
        result = self.rdb.service.SetWriteQueueLastPoint(point)
        return result

        #写到设备一些值 points需要填充
    def SetWriteQueuePoints(self, pointss):
        points = self.ArrayOfCls_point
        points.Cls_point =pointss
        result = self.rdb.service.SetWriteQueuePoints(points)
        return result

