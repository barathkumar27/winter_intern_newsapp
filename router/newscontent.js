const express = require('express')
// const mongoose = require("mongoose")
var MongoClient = require('mongodb').MongoClient;
var url = 'mongodb://127.0.0.1:27017/'

function addFunc(data, result) {
    var result1 ={
        'headline':result.headline,
        "newscontent":result.news_content
    }
    // console.log(result1)
    return data.push(result1)  
}

const router =new express.Router()

router.post('/news',async (req,res)=>{
    
    MongoClient.connect(url, async (err, db) => {
        data=[]
        if (err) throw err;
        var dbo = db.db("database");
        const col=dbo.collection("feeder")
        await col.find().forEach((result) => {
             addFunc(data, result)
        })
        res.send(data)
      }); 

      
})


module.exports = router
