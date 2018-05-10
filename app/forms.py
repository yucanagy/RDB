from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField,SelectField,SelectMultipleField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email, Length, IPAddress
from app import rdbalchemy, rdb
from config import Config
from flask import flash, get_flashed_messages
from suds.client import Client
import copy
import sys
sys.setrecursionlimit(5000)

class ConnectRDB(FlaskForm):
    serverIP = StringField('ServerIP',validators=[DataRequired(), IPAddress()], default= Config.RDB_IP)
    submit = SubmitField('Confirm')

    def validate_serverIP(self, serverIP):
        self.deepcopyRDB(rdb,rdbalchemy.RDBAlchemy(serverIP.data))
        if  not rdb.rdbState:
            raise ValidationError('Can not connect to RDB,please check IP.')

    def deepcopyRDB(self, left, right):
        left.rdb = right.rdb
        left.ArrayOfCls_point = right.ArrayOfCls_point
        left.ArrayOfCls_point_main = right.ArrayOfCls_point_main
        left.ArrayOfCls_point_main_py = right.ArrayOfCls_point_main_py
        left.ArrayOfKeyValueOfanyTypeanyType = right.ArrayOfKeyValueOfanyTypeanyType
        left.ArrayOfTableAttributes = right.ArrayOfTableAttributes
        left.ArrayOfanyType = right.ArrayOfanyType
        left.ArrayOfint = right.ArrayOfint
        left.ArrayOfstring = right.ArrayOfstring
        left.Cls_point = right.Cls_point
        left.Cls_point_main = right.Cls_point_main
        left.Cls_point_main_py = right.Cls_point_main_py
        left.TableAttributes = right.TableAttributes
        left.char = right.char
        left.duration = right.duration
        left.guid = right.guid
        left.anyType = right.anyType
        left.rdbState = right.rdbState

class AddTableForm(FlaskForm):
    tablename = StringField('Tablename', validators=[DataRequired()])
    protocol = SelectField('Protocol', choices=[('OPC', 'OPC'), ('RTU', 'RTU'), ('TCP', 'TCP')], validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    port = StringField('Port', validators=[DataRequired()])
    submit = SubmitField('Confirm') 

    def validate_tablename(self,tablename):
        result = rdb.GetTablesName()[1][0]
        if tablename.data in result:
            raise ValidationError('Please use a different tablename.')


class DeleteTableform(FlaskForm):
    tablenames = SelectField('TableName', validators=[DataRequired()], choices=[])
    submit = SubmitField('Confirm')


class UpdateTableForm(FlaskForm):
    tablename = SelectField('Tablename', choices=[], validators=[DataRequired()])
    protocol = SelectField('Protocol', choices=[('OPC', 'OPC'), ('RTU', 'RTU'), ('TCP', 'TCP')], validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    port = StringField('Port', validators=[DataRequired()])
    submit = SubmitField('Confirm') 

    # def validate_newtablename(self,newtablename):
    #     result = rdb.GetTableAttributes(newtablename)
    #     if result[0] > -1:
    #         raise ValidationError('Please use a different newtablename.')


class AddPointForm(FlaskForm):
    name = StringField('Point', validators=[DataRequired()])
    protocol = SelectField('Protocol',  choices=[('OPC', 'OPC'), ('RTU', 'RTU'), ('TCP', 'TCP')], validators=[DataRequired()])
    table = StringField('Table',validators=[DataRequired()])
    datatype = SelectField('Type', choices=[('Numeric','Numeric'), ('Boolean', 'Boolean'), ('String', 'String')], validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()]) 
    submit = SubmitField('Confirm') 
    
    def validate_name(self,name):
        result = rdb.GetTablePointsName(self.table.data)[1][0]
        if name.data in result:
            raise ValidationError('Please use a different name.')

class DeletePointform(FlaskForm):
    name = SelectField('PointName', validators=[DataRequired()], coerce=str, choices=[])
    submit = SubmitField('Confirm')


class UpdatePointForm(FlaskForm):
    name = SelectField('PointName', choices=[], validators=[DataRequired()])
    newname = StringField('NewPointName', validators=[DataRequired()])
    protocol = SelectField('Protocol',  choices=[('OPC', 'OPC'), ('RTU', 'RTU'), ('TCP', 'TCP')], validators=[DataRequired()])
    table = StringField('Table',validators=[DataRequired()])
    datatype = SelectField('Type', choices=[('Numeric','Numeric'), ('Boolean', 'Boolean'), ('String', 'String')], validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()]) 
    submit = SubmitField('Confirm') 

    def validate_newname(self, name):
        result = rdb.GetTablePointsName(self.table.data)[1]
        if name.data in result:
            raise ValidationError('Please use a different name.')
