# class Cls_point(object):
#     index   = 0 '序号
#     id   = 0 'id
#     name   '名称
#     globalname   = "" '全局名称
#     type   = "Numeric" '类型
#     protocol   = "ModbusTCP" '协议
#     value  Object = 0 '当前值
#     resolution  Double = 0.1 '分辨率
#     ratio  Double = 1 '比例系数
#     updatetime   = 0 '刷新时间
#     ltupdatevalue  Object = 0
#     ltupdatetime   = 0
#     unit   = "无" '单位
#     value_hlimit  Double '量程上限
#     value_llimit  Double '量程下限
#     alarmcls  Byte '报警等级
#     alarm_hh  Double
#     alarm_h  Double
#     alarm_l  Double
#     alarm_ll  Double
#     alarmmode   '报警类型
#     record   = False  '是否存档
#     setmessage   = "无" '设定描述
#     resetmessage   = "无" '复位描述
#     stationnum   = "1" ' 站号
#     chanelnum   = "1" ' 通道号
#     modbusadd   = "1" 'Modbus地址
#     alarmornot   = False  '是否报警
#     createtime   = 0  '是否报警
#     qualitygood     '数据质量
#     alarmstate     '报警状态
#     fatherid       '父节点ID
#     baud   = 9600  '波特率
#     dataformat   = "8N1" '数据格式
#     biglittleendian   = "1234" '大小端，0、1、2、3四种
#     decimalpoint   = 0 '小数点
#     readCode   = 0
#     writeCode   = 0
from app import rdb
class Cls_point_main(object):
    ID = 0
    updatetime = 0  
    value = object()
    qualitygood = True


class TableAttributes(rdb.TableAttributes):
    name = ''
    protocol = ''
    address  = ''
    port = ''
    id = 0
    createtime = 0  