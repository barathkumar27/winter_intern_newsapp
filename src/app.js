const express=require('express')
const newsRouter = require('../router/newscontent.js')

const app=express()

// app.use(express.urlencoded({ extended : true }));
app.use(express.json()) //this parse the incoming data into an object

app.use(newsRouter)

module.exports = app