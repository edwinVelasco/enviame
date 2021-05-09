const express = require('express')
const cors = require('cors')
const { dbConnection } = require('../database/config')

class Server {
    constructor() {
        this.app = express()
        this.port = 8080
        this.companyPath = '/api/company'

        this.connectDB()

        this.middlewares()

        this.routes()
    }
    async connectDB(){
        await dbConnection()
    }


    middlewares(){
        // CORS
        this.app.use(cors())

        // body
        this.app.use( express.json() )

    }
    routes() {
        this.app.use(this.companyPath, require('../routes/company'))
    }
    listen(){
        this.app.listen(this.port, () => {
            console.log(`Example app listening at http://localhost:${this.port}`)
        })
    }
}

module.exports = Server;
