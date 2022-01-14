const app =require('./app')
// const port=process.env.PORT 
const port=3000

app.listen(port,()=>{
    console.log("server is up and running in "+port)
})