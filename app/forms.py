from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField,SelectField,SelectMultipleField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email, Length
from app import rdb

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
