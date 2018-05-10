from flask import request, render_template, flash, redirect, url_for, get_flashed_messages
import json
from app import rdb, app
from app.forms import AddTableForm, DeleteTableform, UpdateTableForm, AddPointForm, DeletePointform, UpdatePointForm, ConnectRDB



@app.route('/', methods=['GET', 'POST'])
def login():
    if rdb.rdbState :
        return redirect(url_for('index'))
    else:
        return redirect(url_for('connectRDB'))


@app.route('/connectRDB', methods=['GET', 'POST'])
def connectRDB():
    form = ConnectRDB()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('connectRDB.html', title='Connect RDB', form=form)


@app.route('/index', methods=['GET', 'POST'])
def index():
    tablenames = rdb.GetTablesName()
    tableattributes = []
    if tablenames[0] > -1:
        tablenames = tablenames[1][0]
        for name in tablenames:
            tableattributes.append(rdb.GetTableAttributes(name)[1])
    else:
        pass
    return render_template('index.html', tablenames=tablenames, tableattributes=tableattributes)


@app.route('/getall')
def getall():
    tables = rdb.GetTablesName()
    if tables[0] > -1:
        tables = tables[1][0]
    else:
        pass
    table_info = {}
    for table in tables:
        points = rdb.GetPoints_From_table_hash(table)
        if points[0] > -1:
            points = points[1][0]
        else:
            continue
        table_info[table] = points
    return render_template('allpoints.html', tables=table_info)


@app.route('/addtable', methods=['GET', 'POST'])
def addtable():
    form = AddTableForm()
    if form.validate_on_submit():
        newid = rdb.CreateTableID()
        rdb.AddTable(form.tablename.data, form.protocol.data,
                     form.port.data, form.address.data, newid)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))
    return render_template('addtable.html', title='Add Table', form=form)


@app.route('/deletetable', methods=['GET', 'POST'])
def deletetable():
    form = DeleteTableform()
    tablenames = rdb.GetTablesName()
    if tablenames[0] > -1:
        tablenames = tablenames[1][0]
        choice = []
        for num in tablenames:
            choice.append((num,num))
        form.tablenames.choices = choice
    if form.validate_on_submit():
        name = form.tablenames.data
        result = rdb.DeleteTable(name)
        if result < 0:
            flash('Delete' & name & 'falied')
        return redirect(url_for('index'))
    return render_template('deletetable.html', title='Delete Table', form=form)


@app.route('/updatetable', methods={'GET', 'POST'})
def updatetable():
    form = UpdateTableForm()
    tablenames = rdb.GetTablesName()
    if tablenames[0] > -1:
        tablenames = tablenames[1][0]
        choice = []
        for num in tablenames:
            choice.append((num,num))
        form.tablename.choices = choice
    if form.validate_on_submit():
        tablename = form.tablename.data
        tableid = rdb.GetTableAttributes(tablename)
        if tableid[0] < 0:
            return render_template('addtable.html', title='Update', form=form)
        tableid = tableid[1]['id']
        newattributes = rdb.TableAttributes
        newattributes.protocol = form.protocol.data
        newattributes.address = form.address.data
        newattributes.port = form.port.data
        rdb.UpdateTableAtt(tableid, newattributes)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))
    return render_template('addtable.html', title='Update', form=form)

@app.route('/points/<tablename>', methods=['GET', 'POST'])
def points(tablename):
    points = rdb.GetPoints_From_table_hash(tablename)
    if points[0] > -1:
        points = points[1][0]
        tableattributes = rdb.GetTableAttributes_hash()[1][0][0]
        columns = rdb.Cls_point

        return render_template('points.html', tablename=tablename, columns=columns, points=points, tableattributes=tableattributes)
    else:
        flash('Table is empty')
        return render_template('points.html', tablename=tablename)

@app.route('/addpoint/<tablename>', methods=['GET', 'POST'])
def addpoint(tablename):
    form = AddPointForm()
    form.table.data = tablename
    if form.validate_on_submit():
        newpoint = rdb.Cls_point
        newpoint.name =form.name.data
        newpoint.modbusadd = form.address.data
        newpoint.protocol = form.protocol.data
        newpoint.type = form.datatype.data

        rdb.AddPoint(tablename, newpoint)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('points', tablename=tablename))
    return render_template('addpoint.html', title='Add Table', form=form)


@app.route('/deletepoint/<tablename>', methods=['GET', 'POST'])
def deletepoint(tablename):
    form = DeletePointform()
    points = rdb.GetPoints_From_table_hash(tablename)
    if points[0] > -1:
        points = points[1][0]
        choice = []
        for num in points:
            choice.append((str(num['id']), str(num['name'])))
        form.name.choices = choice
    if form.validate_on_submit():
        name = form.name.data
        result = rdb.DeletePoint(name)
        if result < 0:
            flash('Delete' & name & 'failed')
        return redirect(url_for('points', tablename=tablename))                           
    return render_template('deletepoint.html', title='Delete Point', form=form)

@app.route('/updatapoint/<tablename>', methods={'GET', 'POST'})
def updatapoint(tablename):
    form = UpdatePointForm()
    points = rdb.GetPoints_From_table_hash(tablename)
    if points[0] > -1:
        points = points[1][0]
        form.table.data = tablename
        choice = []
        for num in points:
            choice.append((str(num['id']),str(num['name'])))
        form.name.choices = choice
    if form.validate_on_submit():
        newpoint = rdb.Cls_point
        newpoint.id = form.name.data
        newpoint.name = form.newname.data
        newpoint.protocol = form.protocol.data
        newpoint.datatype = form.datatype.data
        newpoint.address = form.address.data
        return redirect(url_for('points', tablename=tablename))
    return render_template('addpoint.html', title='Update', form=form)
