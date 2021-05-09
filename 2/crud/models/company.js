const { Schema, model } = require('mongoose')

const CompanySchema = Schema({
    name: {
        type: String,
        required: [true, 'Name is required']
    },
    nit: {
        type: String,
        required: [true, 'NIT is required'],
        unique: true
    },
    description: {
        type: String
    },
    enable:{
        type: Boolean,
        default: true
    }
})


module.exports = model('Company', CompanySchema)
