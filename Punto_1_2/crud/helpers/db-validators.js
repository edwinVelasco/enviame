const Company = require('../models/company')

const existCompany = async (nit='') => {
    const existcompany = await Company.findOne({ nit })
    if(existcompany){
        throw new Error(`this NIT ${nit}, is already registered...`)
    }
}

const existsCompanyId = async (id) => {
    const existscompany = await Company.findById(id)
    if(!existscompany){
        throw new Error(`this id ${id}, not exists...`);
    }
}

module.exports = {
    existCompany, existsCompanyId
}
